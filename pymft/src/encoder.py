from pymft.src.constants import Constants as constants
import rtmidi

class Setting:
    """
    Represents a single configuration setting for an encoder.
    """

    def __init__(self, address: int):
        self._address = address
        self._value = 0
        self._is_modified = False

    def set_value(self, value: int):
        """
        Sets the value of the setting and marks it as modified.
        """
        if self._value != value:
            self._value = value
            self._is_modified = True
        return self._is_modified

class Encoder:
    """
    Represents a single encoder on the Midi Fighter Twister device.
    """

    def __init__(self, encoder_index: int, midi_out: rtmidi.MidiOut = None):
        self._encoder_index = encoder_index
        self._midi_out = midi_out
        self._sysex_tag = encoder_index + 1
        self._settings = {
            "has_detent": Setting(10),
            "movement": Setting(11),
            "switch_action_type": Setting(12),
            "switch_midi_channel": Setting(13),
            "switch_midi_number": Setting(14),
            "switch_midi_type": Setting(15),
            "encoder_midi_channel": Setting(16),
            "encoder_midi_number": Setting(17),
            "encoder_midi_type": Setting(18),
            "active_color": Setting(19),
            "inactive_color": Setting(20),
            "detent_color": Setting(21),
            "indicator_display_type": Setting(22),
            "is_super_knob": Setting(23),
            "encoder_shift_midi_channel": Setting(24),
        }
        self._is_modified = False

    def set_detent(self, value: bool):
        """
        Sets whether the encoder has a detent.
        """
        self.set("has_detent", constants.CFG_TRUE if value else constants.CFG_FALSE)

    def set(self, setting_name: str, value: int):
        """
        Sets the value of a specific setting and marks it as modified.
        """
        self._is_modified = self._settings[setting_name].set_value(value) or self._is_modified

    def send(self, force_all: bool):
        """
        Sends the encoder configuration to the device.
        """
        if not self._is_modified and not force_all:
            return

        config_data = []
        for setting in self._settings.values():
            if setting._is_modified or force_all:
                config_data.extend([setting._address, setting._value])

        if config_data:
            # Use MFT sysex Bulk Transfer protocol
            bytes_remaining = len(config_data)
            total_parts = (bytes_remaining + constants.PART_SIZE_BYTES - 1) // constants.PART_SIZE_BYTES
            for part in range(1, total_parts + 1):
                size = bytes_remaining if bytes_remaining <= constants.PART_SIZE_BYTES else constants.PART_SIZE_BYTES
                bytes_remaining -= constants.PART_SIZE_BYTES

                payload = [0xF0] + [constants.MIDI_MFR_ID_0, constants.MIDI_MFR_ID_1, constants.MIDI_MFR_ID_2] + [
                    constants.SYSEX_COMMAND_BULK_XFER, 0x00, self._sysex_tag, part, total_parts, size
                ] + config_data[:size] + [0xF7]
                config_data = config_data[size:]

                self._send_sysex(payload)

        self._is_modified = False
        for setting in self._settings.values():
            setting._is_modified = False

    def _send_sysex(self, sysex: list):
        """
        Sends a SysEx message to the device.
        """
        try:
            self._midi_out.send_message(sysex)
        except Exception as e:
            print(f"Error sending SysEx message: {e}")


    def is_modified(self):
        return self._is_modified