import rtmidi

from pymft.src.constants import Constants as constants

class MidiFighterTwister:
    """
    Represents a Midi Fighter Twister device.
    """

    def __init__(self):
        self._midi_in = rtmidi.MidiIn()
        self._midi_out = rtmidi.MidiOut()
        self._device_name = constants.DEVICE_NAME
        self._bank = constants.BANK1
        self._is_aux = False
        self._input_port = None
        self._output_port = None

    def discover(self):
        """
        Discovers the Midi Fighter Twister device and initializes input/output.
        """
        input_ports = self._midi_in.get_port_count()
        output_ports = self._midi_out.get_port_count()

        for i in range(input_ports):
            if self._device_name in self._midi_in.get_port_name(i):
                self._input_port = i
                break

        for i in range(output_ports):
            if self._device_name in self._midi_out.get_port_name(i):
                self._output_port = i
                break

        if self._input_port is not None and self._output_port is not None:
            try:
                self._midi_in.open_port(self._input_port)
                self._midi_out.open_port(self._output_port)
                return True
            except Exception as e:
                print(f"Error opening MIDI ports: {e}")
                return False
        return False

    def _send_midi_message(self, message):
        """
        Sends a MIDI message to the device.
        """
        if self._midi_out and self._output_port is not None:
            try:
                self._midi_out.send_message(message)
            except Exception as e:
                print(f"Error sending MIDI message: {e}")

    def _send_control_change(self, channel, cc, value):
        """
        Sends a control change message to the device.
        """
        message = [0xB0 + channel, cc, value]  # Control Change message format
        self._send_midi_message(message)

    def _send_note_on(self, channel, note, velocity):
        """
        Sends a note on message to the device.
        """
        message = [0x90 + channel, note, velocity]  # Note On message format
        self._send_midi_message(message)

    def _send_note_off(self, channel, note, velocity=0):
        """
        Sends a note off message to the device.
        """
        message = [0x80 + channel, note, velocity]  # Note Off message format
        self._send_midi_message(message)

    def set_bank(self, bank):
        """
        Sets the current bank on the device.
        """
        self._send_control_change(constants.CHANNEL_SYSTEM, bank, constants.BANK_ON)
        self._bank = bank

    def set_aux(self, is_aux):
        """
        Sets whether the device is controlling the primary or aux channel.
        """
        self._is_aux = is_aux

    def get_knob_value(self, knob_index):
        """
        Gets the current value of a knob.
        """
        raise NotImplementedError("Getting knob values is not yet implemented.")

    def get_switch_state(self, switch_index):
        """
        Gets the current state of a switch.
        """
        raise NotImplementedError("Getting switch states is not yet implemented.")

    def read_messages(self):
        """
        Reads incoming MIDI messages from the device.
        """
        if self._midi_in and self._input_port is not None:
            while True:
                try:
                    message = self._midi_in.get_message()  # Timeout of 100ms
                    if message:
                        yield message
                except Exception as e:
                    print(f"Error reading MIDI message: {e}")
                    break

    def close(self):
        """
        Closes the input and output ports.
        """
        if self._midi_in and self._input_port is not None:
            self._midi_in.close_port()
        if self._midi_out and self._output_port is not None:
            self._midi_out.close_port()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()