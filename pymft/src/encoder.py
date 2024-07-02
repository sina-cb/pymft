import rtmidi

from pymft.src.constants import constants
from pymft.src.knob_settings import KnobSettings


class Encoder:
    """
    Represents a single encoder on the Midi Fighter Twister device.
    """

    _SETTING_ADDRESSES = {
        "detent": 10,
        "movement_type": 11,
        "switch_action_type": 12,
        "switch_midi_channel": 13,
        "switch_midi_number": 14,
        "switch_midi_type": 15,
        "encoder_midi_channel": 16,
        "encoder_midi_number": 17,
        "encoder_midi_type": 18,
        "active_color": 19,
        "inactive_color": 20,
        "detent_color": 21,
        "indicator_display_type": 22,
        "is_super_knob": 23,
        "encoder_shift_midi_channel": 24,
    }

    def __init__(self, encoder_index: int, midi_out: rtmidi.MidiOut = None):
        self._encoder_index = encoder_index
        self._midi_out = midi_out
        self._sysex_tag = encoder_index + 1
        self.knob_settings = KnobSettings()
        self.value = 0  # Store the current encoder value
        self.mapped_value = 0  # Store the mapped value
        self._last_value = 0

    def set_detent(self, value: bool):
        """
        Sets whether the encoder has a detent.
        """
        self.knob_settings.detent = value

    def set(self, setting_name: str, value: int):
        """
        Sets the value of a specific setting.
        """
        if setting_name in self._SETTING_ADDRESSES or setting_name in {
            "max",
            "min",
        }:
            setattr(self.knob_settings, setting_name, value)

    def update_mapped_value(self):
        """
        Updates the mapped value based on the current value and the min/max range.
        """
        # Calculate the normalized value from 0 to 1
        normalized_value = self.value / 127

        # Map the normalized value to the min/max range
        self.mapped_value = (
            normalized_value * (self.knob_settings.max - self.knob_settings.min)
            + self.knob_settings.min
        )

    def has_changed(self) -> bool:
        """
        Returns True if the encoder value has changed since the last check.
        """
        changed = self.value != self._last_value
        self._last_value = self.value
        return changed

    def send(self, force_all: bool):
        """
        Sends the encoder configuration to the device.
        """
        if not self.knob_settings.is_modified() and not force_all:
            return

        config_data = []
        for setting_name, address in self._SETTING_ADDRESSES.items():
            setting_value = getattr(self.knob_settings, setting_name)
            if setting_value is not None:
                config_data.extend([address, setting_value])

        if config_data:
            bytes_remaining = len(config_data)
            total_parts = (
                bytes_remaining + constants.PART_SIZE_BYTES - 1
            ) // constants.PART_SIZE_BYTES
            for part in range(1, total_parts + 1):
                size = (
                    bytes_remaining
                    if bytes_remaining <= constants.PART_SIZE_BYTES
                    else constants.PART_SIZE_BYTES
                )
                bytes_remaining -= constants.PART_SIZE_BYTES

                payload = (
                    [0xF0]
                    + [
                        constants.MIDI_MFR_ID_0,
                        constants.MIDI_MFR_ID_1,
                        constants.MIDI_MFR_ID_2,
                    ]
                    + [
                        constants.SysExCommands.BULK_XFER,
                        0x00,
                        self._sysex_tag,
                        part,
                        total_parts,
                        size,
                    ]
                    + config_data[:size]
                    + [0xF7]
                )
                config_data = config_data[size:]

                self._send_sysex(payload)

        # Reset the modified flag after sending
        self.knob_settings._is_modified = False

    def _send_sysex(self, sysex: list):
        """
        Sends a SysEx message to the device.
        """
        try:
            self._midi_out.send_message(sysex)
        except Exception as e:
            print(f"Error sending SysEx message: {e}")

    def is_modified(self):
        """
        Returns True if any setting has been modified.
        """
        return self.knob_settings.is_modified()
