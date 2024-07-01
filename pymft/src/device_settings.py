from pymft.src.constants import constants


class DeviceSettings:
    """
    Represents the global configuration settings for a Midi Fighter Twister.
    """

    def __init__(self):
        self._settings = {
            0: constants.MidiChannels.SYSTEM,  # System MIDI channel (default: 4)
            1: constants.SysExValues.TRUE,  # Bank Side Buttons (default: 1/True)
            2: constants.GlobalSideSwitchAction.CCTOGGLE,  # Left Button 1 Function (default: CC Toggle)
            3: constants.GlobalSideSwitchAction.BANKDOWN,  # Left Button 2 Function (default: Bank Down)
            4: constants.GlobalSideSwitchAction.CCTOGGLE,  # Left Button 3 Function (default: CC Toggle)
            5: constants.GlobalSideSwitchAction.CCTOGGLE,  # Right Button 1 Function (default: CC Toggle)
            6: constants.GlobalSideSwitchAction.BANKUP,  # Right Button 2 Function (default: Bank Up)
            7: constants.GlobalSideSwitchAction.CCTOGGLE,  # Right Button 3 Function (default: CC Toggle)
            8: 63,  # Super Knob Start Point (default: 63)
            9: 127,  # Super Knob End Point (default: 127)
            10: 0,  # Not defined in the PDF
            11: 0,  # Not defined in the PDF
            12: 0,  # Not defined in the PDF
            13: 2,  # Not defined in the PDF
            14: 0,  # Not defined in the PDF
            15: 0,  # Not defined in the PDF
            16: 1,  # Not defined in the PDF
            17: 0,  # Not defined in the PDF
            18: constants.EncoderSettings.MIDITYPE_SENDCC,  # Encoder MIDI Type (default: Send CC)
            19: constants.ColorValues.ACTIVE,  # Default Encoder Active Color (default: 51)
            20: constants.ColorValues.BLUE,  # Default Encoder Inactive Color (default: 1)
            21: 63,  # Default Encoder Detent Color (default: 63)
            22: constants.EncoderSettings.INDICATORTYPE_BLENDEDBAR,  # Default Encoder Indicator Type (default: Blended Bar)
            23: 0,  # Not defined in the PDF
            24: 0,  # Not defined in the PDF
            # Yes this gap matches the Midi Fighter Utility sysex
            31: 127,  # RGB LED Brightness (default: 127)
            32: 127,  # Indicator Global Brightness (default: 127)
        }
        self._is_modified = False

    def __getitem__(self, key):
        return self._settings[key]

    def __setitem__(self, key, value):
        if self._settings[key] != value:
            self._settings[key] = value
            self._is_modified = True

    def is_modified(self) -> bool:
        """
        Returns True if any global setting has been modified.
        """
        return self._is_modified
