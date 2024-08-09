# -*- coding: utf-8 -*-
"""Driver implementation for the MCP40 17/18/19 digital potentiometers.

More information on the functionality of the chip can be found at
the microchip's site for the 18 series chip with download for data sheet of all three chips:
https://www.microchip.com/en-us/product/MCP4018
"""
__author__ = "Carl Bellgardt"
__version__ = "0.1"
__all__ = ["MCP40"]

from .potentiometer import Potentiometer
from .serialbus import SerialBusDevice
from .systypes import ErrorCode
from .primitives import Percentage

class MCP40( SerialBusDevice, Potentiometer ):
    """MCP40 family and MCP40D family driver implementation.\
    This implementation was tested using a MCP40D18T-104E/LT. It should also work for any other specified chip.

    The MCP40 and MCP40D family's chips are digital potentiometers that are controlled via an I2C interface. Their difference lies in their terminal configurations.
    The all come in different resistances of 5kOhm, 10kOhm, 50kOhm and 100kOhm. Read more under https://www.microship.com/en-us/product/MCP4017
    """
    
    ADDRESSES_ALLOWED = [0x2E, 0x3E, 0x2F]
    _potentiometer_digital_max = 128 # should apply for all MCP40xx boards
    _potentiometer_resistance_max = None

    def __init__(self):
        # Create instance attributes and initialize parent classes and interfaces
        SerialBusDevice.__init__(self)

    #
    # Module API
    #

    @classmethod
    def Params_init(cls, paramDict):
        """Initializes configuration parameters with defaults.
        
        The following settings are supported:
        
        =============================    ==========================================================================================================
        Key name                         Value type, meaning and default
        =============================    ==========================================================================================================
        SerialBusDevice.address          ``int`` I2C serial device address; default is :attr:`ADDRESSES_ALLOWED` [0].
        Potentiometer.resistance.max     ``int`` Maximum resistance in Ohm; :attr:`DEFAULT_RESISTANCE_MAX`.
        ===========================================================================================================================================
        
        Also see: :meth:`.SerialBusDevice.Params_init`, :meth:`.Potentiometer.Params_init`. 
        """
        defaults = dict()
        SerialBusDevice.Params_init( paramDict )
        Potentiometer.Params_init( paramDict )
        defaults.update( paramDict )
        paramDict = defaults
        return None

    def open(self, paramDict):
        """Initialize an instance and prepare it for use.

        Also see: :meth:`.Module.open`.
        
        :param dict(str, object) paramDict: Configuration parameters as\
        possibly obtained from :meth:`Params_init`.
        :return: An error code indicating either success or the reason of failure.
        :rtype: ErrorCode
        """
        # Get default parameters
        MCP40.Params_init( paramDict )
        # Open the bus device
        ret = SerialBusDevice.open(self, paramDict)
        # Store potentiometer properties
        self._potentiometer_resistance_max = paramDict["Potentiometer.resistance.max"]
        return ret


    def close(self):
        """Close this instance and release hardware resources.
        
        Also see: :meth:`.Module.close`.
        
        :return: An error code indicating either success or the reason of failure.
        :rtype: ErrorCode
        """
        ret = SerialBusDevice.close(self)
        return ret
    
    def _digitalize_resistance_value(self, percentage=None, absolute=None, digital=None): 
        """Converts an either digital, absolute or relative resistance value into a digital value. It also checks for it's validity.\
        There must only be one parameter given.

        Also see: :meth:`.potentiometer._digitalize_resistance_value`.
        
        :param percentage percentage: Resistance value, interpreted as percentage (0 to 100).
        :param int absolute: Resistance value in Ohms. Must be between 0 and the set maximum value.
        :param int digital: Digital resistance value to be sent directly to the potentiometer without conversion.
        :return: An error code indicating either success or the reason of failure.
        :rtype: Tuple(ErrorCode, data)
        """
        return Potentiometer._digitalize_resistance_value(percentage, absolute, digital, self._potentiometer_digital_max, self._potentiometer_resistance_max)
    
    def set(self, percentage=None, absolute=None, digital=None):
        """Set resistance of potentiometer to a relative (percentage), absolute (ohms), or digital value.\
        There must only be one parameter given.
        
        Also see: :meth:`.Potentiometer.set`.
        
        :param percentage percentage: Resistance value, interpreted as percentage (0 to 100).
        :param int absolute: Resistance value in Ohms. Must be between 0 and the set maximum value.
        :param int digital: Digital resistance value to be sent directly to the potentiometer without conversion.
        :return: An error code indicating either success or the reason of failure.
        :rtype: ErrorCode
        """
        value, err = self._digitalize_resistance_value(percentage, absolute, digital)
        if err.isOk():
            err = SerialBusDevice.writeByteRegister(self, 0x00, value)
        return err
    
    def get(self, asPercentage=False, asAbsolute=False, asDigital=False):
        """Get current resistance setting of potentiometer as ative (percentage), absolute (ohms), or digital value via I2C.\
        There must only be one parameter set to true.
        
        Also see: :meth:`.Potentiometer.get`.
        
        :param bool asPercentage: Set true to convert value into a relative percent valued.
        :param bool asAblsolute: Set true to convert value into ohms.
        :param bool asDigital: Set true to return value as digital value.
        :return: The resistance value and an error code indicating either success or the reason of failure.
        :rtype: Tuple(ErrorCode, data)
        """
        data = None
        if asPercentage ^ asAbsolute ^ asDigital: # check if exactly one parameter is given
            data, err = SerialBusDevice.readByteRegister(self, 0x00)
            if err.isOk():
                # convert data into percentage or ohms (or digital value)
                if asPercentage:
                    data = Percentage(data * 100 / self._potentiometer_digital_max)
                elif asAbsolute:
                    data = data * self._potentiometer_resistance_max / self._potentiometer_digital_max
                elif asDigital:
                    pass # nothing to do here
        else:
            err = ErrorCode.errInvalidParameter
        return data, err
    
