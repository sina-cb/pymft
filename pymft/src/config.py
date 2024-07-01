import rtmidi

from pymft.src.constants import constants
from pymft.src.device_settings import DeviceSettings
from pymft.src.encoder import Encoder


class Config:
    """
    Represents the configuration of a Midi Fighter Twister device.
    """

    def __init__(
        self,
        midi_out: rtmidi.MidiOut,
        device_settings: DeviceSettings = DeviceSettings(),
    ):
        self._midi_out = midi_out
        self._device_settings = device_settings
        self._encoders = [
            Encoder(i, self._midi_out)
            for i in range(constants.Encoders.DEVICE_KNOB_NUM)
        ]

    def initialize_defaults(self):
        """
        Initializes the configuration with the new defaults.
        """
        for bank in range(constants.Encoders.DEVICE_BANK_NUM):
            if bank == constants.SystemMessages.BANK1:
                bank_inactive_color = constants.ColorValues.INACTIVE
                bank_active_color = constants.ColorValues.PINK
            elif bank == constants.SystemMessages.BANK2:
                bank_inactive_color = constants.ColorValues.INACTIVE
                bank_active_color = constants.ColorValues.YELLOW
            elif bank == constants.SystemMessages.BANK3:
                bank_inactive_color = constants.ColorValues.INACTIVE
                bank_active_color = constants.ColorValues.RED
            elif bank == constants.SystemMessages.BANK4:
                bank_inactive_color = constants.ColorValues.INACTIVE
                bank_active_color = constants.ColorValues.BLUE

            for bank_knob in range(constants.Encoders.DEVICE_KNOB_PER_BANK):
                i = bank_knob + (constants.Encoders.DEVICE_KNOB_PER_BANK * bank)
                self._encoders[
                    i
                ].knob_settings.detent = constants.SysExValues.FALSE
                self._encoders[i].set(
                    "movement",
                    constants.EncoderSettings.MOVEMENTTYPE_DIRECT_HIGHRESOLUTION,
                )
                self._encoders[i].set(
                    "switch_action_type",
                    constants.EncoderSettings.SWACTION_ENCRESETVALUE,
                )
                self._encoders[i].set("switch_midi_channel", 2)
                self._encoders[i].set("switch_midi_number", i)
                self._encoders[i].set("switch_midi_type", 0)  # Not used
                self._encoders[i].set("encoder_midi_channel", 1)
                self._encoders[i].set("encoder_midi_number", i)
                self._encoders[i].set(
                    "encoder_midi_type",
                    constants.EncoderSettings.MIDITYPE_SENDCC,
                )
                self._encoders[i].set("active_color", bank_active_color)
                self._encoders[i].set("inactive_color", bank_inactive_color)
                self._encoders[i].set(
                    "detent_color", constants.ColorValues.PINK
                )
                self._encoders[i].set(
                    "indicator_display_type",
                    constants.EncoderSettings.INDICATORTYPE_BLENDEDBAR,
                )
                self._encoders[i].set(
                    "is_super_knob", constants.SysExValues.FALSE
                )
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
        sysex = (
            [0xF0]
            + [
                constants.MIDI_MFR_ID_0,
                constants.MIDI_MFR_ID_1,
                constants.MIDI_MFR_ID_2,
            ]
            + [constants.SysExCommands.PUSH_CONF]
        )

        for key, value in self._device_settings._settings.items():
            sysex.extend([key, value])

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
