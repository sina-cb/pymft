import rtmidi

from pymft.src.constants import Constants as constants
from pymft.src.encoder import Encoder

class Config:
    """
    Represents the configuration of a Midi Fighter Twister device.
    """

    def __init__(self, midi_out: rtmidi.MidiOut):
        self._midi_out = midi_out
        self._global_config = {}
        self._encoders = [Encoder(i, self._midi_out) for i in range(constants.DEVICE_KNOB_NUM)]

    def initialize_lx_defaults(self):
        """
        Initializes the configuration with LX-friendly defaults.
        """
        self._global_config = {
            0: 4,  # System MIDI channel
            1: 1,  # Bank Side Buttons
            2: constants.CFG_GLOBAL_SSACTION_CCTOGGLE,  # Left Button 1 Function
            3: constants.CFG_GLOBAL_SSACTION_BANKDOWN,  # Left Button 2 Function
            4: constants.CFG_GLOBAL_SSACTION_CCTOGGLE,  # Left Button 3 Function
            5: constants.CFG_GLOBAL_SSACTION_CCTOGGLE,  # Right Button 1 Function
            6: constants.CFG_GLOBAL_SSACTION_BANKUP,  # Right Button 2 Function
            7: constants.CFG_GLOBAL_SSACTION_CCTOGGLE,  # Right Button 3 Function
            8: 63,  # Super Knob Start Point
            9: 127,  # Super Knob End Point
            10: 0,  # 0a
            11: 0,  # 0b CFG_ENC_MOVEMENTTYPE_DIRECT_HIGHRESOLUTION?
            12: 0,  # 0c CFG_ENC_SWACTION_CCHOLD?
            13: 2,  # 0d
            14: 0,  # 0e
            15: 0,  # 0f
            16: 1,  # 10
            17: 0,  # 11
            18: constants.CFG_ENC_MIDITYPE_SENDRELENC,  # 12
            19: 51,  # 13
            20: 1,  # 14
            21: 63,  # 15
            22: constants.CFG_ENC_INDICATORTYPE_BLENDEDBAR,  # 16
            23: 0,  # 17
            24: 0,  # 18
            # Yes this gap matches the Midi Fighter Utility sysex
            31: 127,  # 1f  RGB LED Brightness
            32: 127,  # 20  Indicator Global Brightness
        }

        for i in range(constants.DEVICE_KNOB_NUM):
            self._encoders[i].set_detent(False)
            self._encoders[i].set("movement", constants.CFG_ENC_MOVEMENTTYPE_DIRECT_HIGHRESOLUTION)
            self._encoders[i].set("switch_action_type", constants.CFG_ENC_SWACTION_CCHOLD)
            self._encoders[i].set("switch_midi_channel", 2)
            self._encoders[i].set("switch_midi_number", i)
            self._encoders[i].set("switch_midi_type", 0)  # Appears no longer in use
            self._encoders[i].set("encoder_midi_channel", 1)
            self._encoders[i].set("encoder_midi_number", i)
            self._encoders[i].set("encoder_midi_type", constants.CFG_ENC_MIDITYPE_SENDRELENC)  # Important! must be relative type
            self._encoders[i].set("active_color", 51)  # MFT default 51
            self._encoders[i].set("inactive_color", 1)  # MFT default 1
            self._encoders[i].set("detent_color", 63)  # MFT default 63
            self._encoders[i].set("indicator_display_type", constants.CFG_ENC_INDICATORTYPE_BLENDEDBAR)
            self._encoders[i].set("is_super_knob", constants.CFG_FALSE)
            self._encoders[i].set("encoder_shift_midi_channel", 0)

    def initialize_defaults(self):
        """
        Initializes the configuration with LX-friendly defaults.
        """
        self._global_config = {
            0: 4,  # System MIDI channel
            1: 1,  # Bank Side Buttons
            2: constants.CFG_GLOBAL_SSACTION_CCTOGGLE,  # Left Button 1 Function
            3: constants.CFG_GLOBAL_SSACTION_BANKDOWN,  # Left Button 2 Function
            4: constants.CFG_GLOBAL_SSACTION_CCTOGGLE,  # Left Button 3 Function
            5: constants.CFG_GLOBAL_SSACTION_CCTOGGLE,  # Right Button 1 Function
            6: constants.CFG_GLOBAL_SSACTION_BANKUP,  # Right Button 2 Function
            7: constants.CFG_GLOBAL_SSACTION_CCTOGGLE,  # Right Button 3 Function
            8: 63,  # Super Knob Start Point
            9: 127,  # Super Knob End Point
            10: 0,  # 0a
            11: 0,  # 0b CFG_ENC_MOVEMENTTYPE_DIRECT_HIGHRESOLUTION?
            12: 0,  # 0c CFG_ENC_SWACTION_CCHOLD?
            13: 2,  # 0d
            14: 0,  # 0e
            15: 0,  # 0f
            16: 1,  # 10
            17: 0,  # 11
            18: constants.CFG_ENC_MIDITYPE_SENDRELENC,  # 12
            19: 51,  # 13
            20: 1,  # 14
            21: 63,  # 15
            22: constants.CFG_ENC_INDICATORTYPE_BLENDEDBAR,  # 16
            23: 0,  # 17
            24: 0,  # 18
            # Yes this gap matches the Midi Fighter Utility sysex
            31: 127,  # 1f  RGB LED Brightness
            32: 127,  # 20  Indicator Global Brightness
        }

        for bank in range(constants.DEVICE_BANK_NUM):
            if bank == constants.BANK1:
                bank_deactive_color = constants.RGB_BLUE
                bank_active_color = constants.RGB_RED
            elif bank == constants.BANK2:
                bank_deactive_color = constants.RGB_PINK
                bank_active_color = constants.RGB_BLUE
            elif bank == constants.BANK3:
                bank_deactive_color = constants.RGB_YELLOW
                bank_active_color = constants.RGB_PINK
            elif bank == constants.BANK4:
                bank_deactive_color = constants.RGB_RED
                bank_active_color = constants.RGB_YELLOW

            for bank_knob in range(constants.DEVICE_KNOB_PER_BANK):
                i = bank_knob + (constants.DEVICE_KNOB_PER_BANK * bank)
                self._encoders[i].set_detent(False)
                self._encoders[i].set("movement", constants.CFG_ENC_MOVEMENTTYPE_DIRECT_HIGHRESOLUTION)
                self._encoders[i].set("switch_action_type", constants.CFG_ENC_SWACTION_CCHOLD)
                self._encoders[i].set("switch_midi_channel", 2)
                self._encoders[i].set("switch_midi_number", i)
                self._encoders[i].set("switch_midi_type", 0)  # Appears no longer in use
                self._encoders[i].set("encoder_midi_channel", 1)
                self._encoders[i].set("encoder_midi_number", i)
                self._encoders[i].set("encoder_midi_type", constants.CFG_ENC_MIDITYPE_SENDRELENC)  # Important! must be relative type
                self._encoders[i].set("active_color", bank_active_color)
                self._encoders[i].set("inactive_color", bank_deactive_color)
                self._encoders[i].set("detent_color", 63)  # MFT default 63
                self._encoders[i].set("indicator_display_type", constants.CFG_ENC_INDICATORTYPE_BLENDEDBAR)
                self._encoders[i].set("is_super_knob", constants.CFG_FALSE)
                self._encoders[i].set("encoder_shift_midi_channel", 0)

    def send_all(self):
        """
        Sends the entire configuration to the device.
        """
        self._send_encoders(force_all=True)
        self._send_global()

    def send_modified(self):
        """
        Sends only the modified configuration values to the device.
        """
        if self._send_encoders(force_all=False):
            self._send_global()

    def _send_encoders(self, force_all: bool):
        """
        Sends the encoder configurations to the device.
        """
        modified = False
        for encoder in self._encoders:
            if encoder.is_modified or force_all:
                encoder.send(force_all)
                modified = True
        return modified

    def _send_global(self):
        """
        Sends the global configuration values to the device.
        """
        sysex = [0xF0] + [constants.MIDI_MFR_ID_0, constants.MIDI_MFR_ID_1, constants.MIDI_MFR_ID_2] + [constants.SYSEX_COMMAND_PUSH_CONF]
        for address, value in self._global_config.items():
            sysex.extend([address, value])
        sysex.append(0xF7)

        self._send_sysex(sysex)

    def _send_sysex(self, sysex: list):
        """
        Sends a SysEx message to the device.
        """
        try:
            self._midi_out.send_message(sysex)
        except Exception as e:
            print(f"Error sending SysEx message: {e}")