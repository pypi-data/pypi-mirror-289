"""A module for the FastGait system management implementation.
"""
__author__ = "Oliver Maye"
__version__ = "0.1"
__all__ = ["systemManagement",]

from threading import Thread, Lock
import time, logging

from pymitter import EventEmitter

from philander.battery import Status as BatStatus, Level
from philander.ble import Event as BleEvent, ConnectionState
from philander.button import Button
from philander.charger import Charger, TemperatureRating, DCStatus, Status as ChgStatus
from philander.gpio import GPIO
from philander.led import LED
from philander.max77960 import MAX77960 as ChgDriver
from philander.module import Module
from philander.systypes import ErrorCode

from .actorunit import ActorUnit


class SystemManagement( Module, EventEmitter ):
    """The fastGait power management and user interface.
    """
    
    #
    # Public class attributes
    #
    EVT_DELIMITER           = '.'
    EVT_MASK                = 'SystemManagement'
    EVT_BLE_CONNECTED       = EVT_MASK + EVT_DELIMITER + 'ble' + EVT_DELIMITER + 'connected'
    EVT_BLE_DISCONNECTED    = EVT_MASK + EVT_DELIMITER + 'ble' + EVT_DELIMITER + 'disconnected'
    EVT_DC_PLUGGED          = EVT_MASK + EVT_DELIMITER + 'dc' + EVT_DELIMITER + 'plugged'
    EVT_DC_UNPLUGGED        = EVT_MASK + EVT_DELIMITER + 'dc' + EVT_DELIMITER + 'unplugged'
    EVT_BUTTON_PRESSED      = EVT_MASK + EVT_DELIMITER + 'ui' + EVT_DELIMITER + 'button' + EVT_DELIMITER + 'pressed'
    EVT_TEMP_CRITICAL       = EVT_MASK + EVT_DELIMITER + 'temp' + EVT_DELIMITER + 'critical'
    EVT_TEMP_NORMAL         = EVT_MASK + EVT_DELIMITER + 'temp' + EVT_DELIMITER + 'normal'
    EVT_POWER_CRITICAL      = EVT_MASK + EVT_DELIMITER + 'power' + EVT_DELIMITER + 'critical'
    EVT_POWER_NORMAL        = EVT_MASK + EVT_DELIMITER + 'power' + EVT_DELIMITER + 'normal'

    # Battery durations for level transitions
    BAT_WARN_TIME_FULL2LOW    = 21600    # Full to Low time in seconds
    BAT_WARN_TIME_LOW2EMPTY   = 3600     # Low to empty time in seconds
    
    
    #
    # Private class attributes
    #
    
    _SYSJOB_NONE      = 0x00
    _SYSJOB_AU_COUPLE = 0x01
    _SYSJOB_ANY       = 0xFFFF
    
    _LED_SETTING_PREFIXES   = ("UI.tmp.LED", "UI.bat.LED", "UI.ble.LED",\
                               "UI.dc.LED", "UI.chg.LED", "UI.aux0.LED",\
                               "UI.aux1.LED", )
    _BUTTON_SETTING_PREFIXES= ("UI.cmd.Button", )
    
    def __init__(self):
        # Call super class constructor(s)
        EventEmitter.__init__( self, wildcard=True, delimiter=SystemManagement.EVT_DELIMITER)
        # Create instance attributes
        self._systemJob = SystemManagement._SYSJOB_NONE
        self._sysjobLock = Lock()
        self.done = False
        self.charger = ChgDriver()
        self.actorUnit = ActorUnit()
        self.tmpLED = None
        self.batLED = None
        self.bleLED = None
        self.dcLED = None
        self.chgLED = None
        self.aux0LED = None
        self.aux1LED = None
        self.cmdBtn = None
        self.sysPowerStatusGPIO = None
        self.monitor = Thread( target=self._manageSystem, name='System Management' )

    #
    # Module API
    #

    @classmethod
    def Params_init(cls, paramDict):
        """Initializes configuration parameters with defaults.
        
        The following settings are supported:
        
        =======================    ==========================================================================================================
        Key name                   Value type, meaning and default
        =======================    ==========================================================================================================
        UI.tmp.LED.*               charger, battery or board temperature status LED; settings as documented at :meth:`.LED.Params_init`.
        UI.bat.LED.*               battery level/status LED; see :meth:`.LED.Params_init`.
        UI.ble.LED.*               BLE connection status LED; see :meth:`.LED.Params_init`.
        UI.dc.LED.*                DC supply status LED; see :meth:`.LED.Params_init`.
        UI.chg.LED.*               charger status LED; see :meth:`.LED.Params_init`.
        UI.aux0.LED.*              aux #0 LED, semantics is defined by the application; see :meth:`.LED.Params_init`.
        UI.aux1.LED.*              aux #1 LED, semantics is defined by the application; see :meth:`.LED.Params_init`.
        UI.cmd.Button.*            user command button; see :meth:`.Button.Params_init`.
        Sys.power.status.gpio.*    System power good indicator, e.g. LDO's PG output; see :meth:`.GPIO.Params_init`.
        Charger.*                  as documented at the charger implementation.
        ActorUnit.*                as documented at :meth:`.ActorUnit.Params_init`.
        =======================    ==========================================================================================================
        
        Also see: :meth:`.LED.Params_init`, :meth:`.Button.Params_init`, :meth:`.GPIO.Params_init`, :meth:`.MAX77960.Params_init`. 

        :param dict(str, object) paramDict: Dictionary mapping option\
        names to their respective values.
        :returns: none
        :rtype: None
        """
        # All LED settings
        dflt = {}
        LED.Params_init( dflt )
        # Explicit settings
        for p in SystemManagement._LED_SETTING_PREFIXES:
            if not (p+".label") in paramDict:
                paramDict[p+".label"] = p.replace("UI.", "")
            paramDict[p + ".gpio.direction"] = dflt.get("LED.gpio.direction")
        # Common routine
        for key, value in dflt.items():
            if key.startswth("LED."):
                keyBase = key.replace("LED.", ".")
                for p in SystemManagement._LED_SETTING_PREFIXES:
                    newKey = p + keyBase
                    if not newKey in paramDict:
                        paramDict[newKey] = value
        # Button settings
        dflt = {}
        Button.Params_init( dflt )
        # Explicit settings
        for p in SystemManagement._BUTTON_SETTING_PREFIXES:
            if not (p+".label") in paramDict:
                paramDict[p+".label"] = p.replace("UI.", "")
            paramDict[p + ".gpio.direction"] = dflt.get("Button.gpio.direction")
        # Common routine
        for key, value in dflt.items():
            if key.startswth("Button."):
                keyBase = key.replace("Button.", ".")
                for p in SystemManagement._BUTTON_SETTING_PREFIXES:
                    newKey = p + keyBase
                    if not newKey in paramDict:
                        paramDict[newKey] = value
        # GPIO settings for the separate LDO's PowerGood pin.
        dflt = {}
        GPIO.Params_init( dflt )
        paramDict["Sys.power.status.gpio.direction"] = GPIO.DIRECTION_IN
        for key, value in dflt.items():
            newKey = "Sys.power.status." + key
            if not newKey in paramDict:
                paramDict[newKey] = value
        # Charger settings
        ChgDriver.Params_init( paramDict )
        # ActorUnit settings
        ActorUnit.Params_init( paramDict )
        return None
    
    def open(self, paramDict):
        result = ErrorCode.errOk

        # LEDs first:
        if "UI.tmp.LED.gpio.pinDesignator" in paramDict:
            tmpParams = dict( [(k.replace("UI.tmp.", ""),v) for k,v in paramDict.items() if k.startswith("UI.tmp.LED.")] )
            self.tmpLED = LED()
            result = self.tmpLED.open( tmpParams )
        if "UI.bat.LED.gpio.pinDesignator" in paramDict:
            tmpParams = dict( [(k.replace("UI.bat.", ""),v) for k,v in paramDict.items() if k.startswith("UI.bat.LED.")] )
            self.batLED = LED()
            result = self.batLED.open( tmpParams )
        if "UI.ble.LED.gpio.pinDesignator" in paramDict:
            tmpParams = dict( [(k.replace("UI.ble.", ""),v) for k,v in paramDict.items() if k.startswith("UI.ble.LED.")] )
            self.bleLED = LED()
            result = self.bleLED.open( tmpParams )
        if "UI.dc.LED.gpio.pinDesignator" in paramDict:
            tmpParams = dict( [(k.replace("UI.dc.", ""),v) for k,v in paramDict.items() if k.startswith("UI.dc.LED.")] )
            self.dcLED = LED()
            result = self.dcLED.open( tmpParams )
        if "UI.chg.LED.gpio.pinDesignator" in paramDict:
            tmpParams = dict( [(k.replace("UI.chg.", ""),v) for k,v in paramDict.items() if k.startswith("UI.chg.LED.")] )
            self.chgLED = LED()
            result = self.chgLED.open( tmpParams )
        if "UI.aux0.LED.gpio.pinDesignator" in paramDict:
            tmpParams = dict( [(k.replace("UI.aux0.", ""),v) for k,v in paramDict.items() if k.startswith("UI.aux0.LED.")] )
            self.aux0LED = LED()
            result = self.aux0LED.open( tmpParams )
        if "UI.aux1.LED.gpio.pinDesignator" in paramDict:
            tmpParams = dict( [(k.replace("UI.aux1.", ""),v) for k,v in paramDict.items() if k.startswith("UI.aux1.LED.")] )
            self.aux1LED = LED()
            result = self.aux1LED.open( tmpParams )
        # Button
        if "UI.cmd.Button.gpio.pinDesignator" in paramDict:
            tmpParams = dict( [(k.replace("UI.cmd.", ""),v) for k,v in paramDict.items() if k.startswith("UI.cmd.Button.")] )
            self.cmdBtn = Button()
            result = self.cmdBtn.open( tmpParams )
            self.cmdBtn.on( Button.EVENT_PRESSED, func=self.uiHandleButtonPressed )
            #self.cmdBtn.asyncWait4Press()
        # System power status pin (GPIO)
        if "Sys.power.status.gpio.pinDesignator" in paramDict:
            tmpParams = dict( [(k.replace("Sys.power.status.", ""),v) for k,v in paramDict.items() if k.startswith("Sys.power.status.gpio.")] )
            self.sysPowerStatusGPIO = GPIO()
            result = self.sysPowerStatusGPIO. open( tmpParams )
        # Charger
        if (result == ErrorCode.errOk):
            result = self.charger.open( paramDict )
        # ActorUnit
        if (result == ErrorCode.errOk):
            result = self.actorUnit.open( paramDict )

        # Event registration, monitor thread and coupling
        if (result == ErrorCode.errOk):
            self.actorUnit.registerInterruptHandler( onEvent = BleEvent.bleDiscovering, handler=self.handleBleDiscovering )
            self.actorUnit.registerInterruptHandler( onEvent = BleEvent.bleConnected, handler=self.handleBleConnected )
            self.actorUnit.registerInterruptHandler( onEvent = BleEvent.bleDisconnected, handler=self.handleBleDisconnected )
            self.monitor.start()
            result = self.actorUnit.couple()
            
        return result

    def close(self):
        result = ErrorCode.errOk
        self.done = True
        if self.monitor.is_alive():
            self.monitor.join()
        # Remove event subscriptions
        self.off_all()
        # Close all module-like attributes
        for mod in (self.charger, self.actorUnit, \
                    self.tmpLED, self.batLED, self.bleLED, self.dcLED,\
                    self.chgLED, self.aux0LED, self.aux1LED, \
                    self.cmdBtn, \
                    self.sysPowerStatusGPIO, ):
            if mod:
                err = mod.close()
                if (err != ErrorCode.errOk):
                    result = err
        self.tmpLED = None
        self.batLED = None
        self.bleLED = None
        self.dcLED = None
        self.chgLED = None
        self.aux0LED = None
        self.aux1LED = None
        self.cmdBtn = None
        self.sysPowerStatusGPIO = None
        return result
    
    #
    # Private helper
    #
            
    def _manageSystem( self ):
        logging.info('Management thread is running.')
        self._sysjobLock.acquire()
        self._systemJob = SystemManagement._SYSJOB_NONE
        self._sysjobLock.release()

        oldStatus = None   # Note that the BLE status is maintained in a separate loop
        batStatus = None
        batLevel = None     # Run-Time based level estimation
        chgStatus = None
        dcStatus  = None
        tmpStatus = None    # chg + bat temperature rating
        ldoStatus = None
        startTime = time.time()

        while not self.done:
            try:
                # Battery status is not available during battery-only mode.
                # So this is not a helpful battery level information.
                val = self.charger.getBatStatus()
                if val != batStatus:
                    batStatus = val
                    self._displayBatStatus( batStatus )
                
                val = self.charger.getChargerTempStatus()
                if batStatus != BatStatus.removed:
                    val1 = self.charger.getBatteryTempStatus()
                    val = self._combineTempStatus( val, val1 )
                if val != tmpStatus:
                    oldStatus = tmpStatus
                    tmpStatus = val
                    self._displayTempStatus( tmpStatus )
                    if tmpStatus.value & TemperatureRating.coldOrHot.value:
                        self.emit( SystemManagement.EVT_TEMP_CRITICAL )
                    elif (not (oldStatus is None)) and (oldStatus.value & TemperatureRating.coldOrHot.value):
                        self.emit( SystemManagement.EVT_TEMP_NORMAL )
                
                val  = self.charger.getDCStatus()
                if val != dcStatus:
                    oldStatus = dcStatus
                    dcStatus = val
                    self._displayDcStatus( dcStatus )
                    if dcStatus == DCStatus.valid:
                        self.emit( SystemManagement.EVT_DC_PLUGGED )
                    elif (oldStatus is None) or (oldStatus == DCStatus.valid):
                        startTime = time.time()
                        self.emit( SystemManagement.EVT_DC_UNPLUGGED )
                        
                val = self.charger.getChgStatus()
                if val != chgStatus:
                    chgStatus = val
                    self._displayChgStatus( chgStatus )
                
                if self.sysPowerStatusGPIO:
                    val = self.sysPowerStatusGPIO.get()
                    if val != ldoStatus:
                        ldoStatus = val
                        self._displayLdoStatus( ldoStatus )
                        if ldoStatus:
                            self.emit( SystemManagement.EVT_POWER_CRITICAL )
                        else:
                            self.emit( SystemManagement.EVT_POWER_NORMAL )

                # Estimate battery level based on elapsed run time
                if dcStatus != DCStatus.valid:   # Battery only
                    now = time.time()
                    dur = now - startTime 
                    if batLevel == Level.empty:
                        val = Level.empty
                    elif batLevel == Level.low:
                        if dur >= SystemManagement.BAT_WARN_TIME_LOW2EMPTY:
                            val = Level.empty
                            startTime = now
                        else:
                            val = Level.low
                    else:
                        if dur >= SystemManagement.BAT_WARN_TIME_FULL2LOW:
                            val = Level.low
                            startTime = now
                        else:
                            val = Level.full
                elif (batStatus & BatStatus.removed):
                    val = Level.invalid
                elif (batStatus & BatStatus.empty):
                    val = Level.empty
                elif (batStatus & BatStatus.low):
                    val = Level.low
                else:
                    val = Level.full
                if val != batLevel:
                    batLevel = val
                    self._displayBatLevel( batLevel )
                    
                self._executeSystemJobs()
            except RuntimeError as exc:
                logging.exception(exc)
            time.sleep(0.5)
        logging.info('Management thread stopped.')
    
    
    def _combineTempStatus( self, chgTemp: TemperatureRating, batTemp: TemperatureRating ):
        ret = TemperatureRating.unknown
        # Prioritize battery temperature information
        if batTemp != TemperatureRating.unknown:
            if batTemp in [TemperatureRating.cold, TemperatureRating.hot, TemperatureRating.coldOrHot]:
                ret = batTemp
            elif chgTemp in [TemperatureRating.unknown, TemperatureRating.ok]:
                ret = batTemp
            else:
                ret = chgTemp
        else:
            ret = chgTemp
        return ret
        
    def _displayTempStatus( self, newStatus: TemperatureRating ):
        logging.info('TMP state: %s', str(newStatus) )
        if self.tmpLED:
            if newStatus == TemperatureRating.ok:
                self.tmpLED.off()
            elif newStatus in (TemperatureRating.cool,\
                               TemperatureRating.warm,\
                               TemperatureRating.coolOrWarm):
                self.tmpLED.blink()
            else:
                self.tmpLED.on()
        return None

    def _displayBatStatus( self, newStatus: BatStatus ):
        logging.info('BAT state: %s', str(newStatus))
        return None
        
    def _displayBatLevel( self, newStatus: Level ):
        logging.info('BAT Level: %s', str(newStatus) )
        if self.batLED:
            if newStatus in (Level.min, Level.empty, ):
                self.batLED.blink( cycle_length=LED.CYCLEN_FAST )
            elif newStatus in (Level.low, Level.medium, ):
                self.batLED.blink( cycle_length=LED.CYCLEN_SLOW )
            elif newStatus in (Level.good, Level.full, Level.max, ):
                self.batLED.off()
            else:   # Errors
                self.batLED.on()
        return None

    def _displayBleStatus( self, newStatus: ConnectionState ):
        logging.info('BLE state: %s', str(newStatus) )
        if self.bleLED:
            if newStatus == ConnectionState.connected:
                self.bleLED.on()
            elif newStatus == ConnectionState.discovering:
                self.bleLED.blink( cycle_length=LED.CYCLEN_NORMAL )
            else:
                self.bleLED.off()
        return None
        
    def _displayDcStatus( self, newStatus: DCStatus ):
        logging.info(' DC state: %s', str(newStatus) )
        if self.dcLED:
            if newStatus == DCStatus.valid:
                self.dcLED.on()
            elif newStatus == DCStatus.off:
                self.dcLED.off()
            else:
                self.dcLED.blink()
        return None
        
    def _displayChgStatus( self, newStatus: ChgStatus ):
        logging.info('CHG state: %s', str(newStatus) )
        if self.chgLED:
            if newStatus in (ChgStatus.done, ChgStatus.topOff, ):
                self.chgLED.on()
            elif newStatus in (ChgStatus.fastCharge, ChgStatus.fastChargeConstCurrent, ChgStatus.fastChargeConstVoltage, ):
                self.chgLED.blink( cycle_length=LED.CYCLEN_FAST )
            elif newStatus in (ChgStatus.preCharge, ChgStatus.trickle, ):
                self.chgLED.blink()
            else:
                self.chgLED.off()
        return None
        
    def _displayLdoStatus( self, newStatus: int ):
        logging.info('LDO state: %d', newStatus )
        return None
        

    def _executeSystemJobs( self ):
        if self._systemJob & SystemManagement._SYSJOB_AU_COUPLE:
            self.actorUnit.couple()
            self._sysjobLock.acquire()
            self._systemJob &= ~SystemManagement._SYSJOB_AU_COUPLE
            self._sysjobLock.release()
            
        
    def handleBleDiscovering( self, *args ):
        self._displayBleStatus( ConnectionState.discovering )
        
    def handleBleConnected( self, *args ):
        self._displayBleStatus( ConnectionState.connected )
        self.emit( SystemManagement.EVT_BLE_CONNECTED )
        
    def handleBleDisconnected( self, *args ):
        self._displayBleStatus( ConnectionState.disconnected )
        self.emit( SystemManagement.EVT_BLE_DISCONNECTED )
        # Start re-discovering
        if not self.done:
            self._sysjobLock.acquire()
            self._systemJob = self._systemJob | SystemManagement._SYSJOB_AU_COUPLE
            self._sysjobLock.release()
            
    def uiHandleButtonPressed( self, label, *_unused ):
        logging.info('UI button pressed.')
        self.emit( SystemManagement.EVT_BUTTON_PRESSED, label )
        
        
        