import json
import threading
import traceback

import rtmidi

from pymft.src.config import Config
from pymft.src.constants import constants
from pymft.src.knob_settings import KnobSettings


class MidiFighterTwister:
    """
    Represents a Midi Fighter Twister device.
    """

    def __init__(self, device_id: int = None):
        self._midi_in = rtmidi.MidiIn()
        self._midi_out = rtmidi.MidiOut()
        self._device_name = constants.DEVICE_NAME
        self._bank = constants.SystemMessages.BANK1
        self._is_aux = False
        self._input_port = None
        self._output_port = None
        self._device_id = device_id
        self._config = Config(self._midi_out)
        self._knob_subscriptions = {}
        self._reading_thread = None
        self._reading_thread_active = False
        self.value_changed_callback = None

    def discover(self, device_id: int = None):
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

    @property
    def config(self):
        return self._config

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

    def set_bank(self, bank: int):
        """
        Sets the current bank on the device.
        """
        self._send_control_change(
            constants.MidiChannels.SYSTEM,
            bank,
            constants.SystemMessages.BANK_ON,
        )
        self._bank = bank

    def set_aux(self, is_aux: bool):
        """
        Sets whether the device is controlling the primary or aux channel.
        """
        self._is_aux = is_aux

    def configure(self):
        """
        Sends the current configuration to the device.
        """
        self._config.send_all()

    def start(self):
        """
        Starts the thread listening for MIDI messages.
        """
        self._start_reading_thread()

    def set_value_changed_callback(self, callback):
        self.value_changed_callback = callback

    def subscribe(self, encoder: int, knob_settings: KnobSettings):
        """
        Subscribes to the value changes of a specific encoder, applies
        the knob settings.
        """
        knob_index = encoder
        if knob_index not in range(constants.Encoders.DEVICE_KNOB_NUM):
            raise ValueError("Invalid knob index. Valid range is 0-63")

        self._knob_subscriptions[knob_index] = knob_settings

        # Apply knob settings to the encoder in the config
        encoder_obj = self._config._encoders[knob_index]

        # Set detent directly using the constants
        encoder_obj.set_detent(knob_settings._detent)

        # Set other values using the set method
        for setting_name in vars(knob_settings):  # Get all attributes
            setting_value = getattr(knob_settings, setting_name)
            if setting_value is not None:
                encoder_obj.set(
                    setting_name[1:], setting_value
                )  # Remove "_" prefix from setting name

        # Hack to turn on the LED lights with default colors if the user did not set a specific color
        if (
            knob_settings.active_color is None
            and knob_settings.inactive_color is None
        ):
            encoder_obj.knob_settings.inactive_color = (
                encoder_obj.knob_settings.active_color
            )

    def load_config(self, config_path: str):
        """
        Loads knob configurations from a JSON file.

        Args:
            config_path: Path to the JSON configuration file.
        """
        try:
            with open(config_path, "r") as f:
                config_data = json.load(f)
                self._load_config_from_data(config_data)
        except FileNotFoundError:
            print(f"Config file not found: {config_path}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e}")

    def _load_config_from_data(self, config_data: dict):
        """
        Loads knob configurations from the parsed JSON data.

        Args:
            config_data: A dictionary containing the knob configuration.
        """
        for knob_config in config_data:
            encoder_index = self._get_encoder_index_from_config(knob_config)
            knob_settings = self._create_knob_settings_from_config(knob_config)
            self.subscribe(encoder_index, knob_settings)

    def _get_encoder_index_from_config(self, knob_config: dict) -> int:
        """
        Extracts the encoder index from the knob configuration.

        Args:
            knob_config: A dictionary containing the knob configuration.

        Returns:
            The encoder index as an integer.
        """
        bank_name = knob_config["bank"]
        encoder_name = knob_config["encoder"]

        if bank_name == "Bank1":
            bank = constants.Encoders.Bank1
        elif bank_name == "Bank2":
            bank = constants.Encoders.Bank2
        elif bank_name == "Bank3":
            bank = constants.Encoders.Bank3
        elif bank_name == "Bank4":
            bank = constants.Encoders.Bank4
        else:
            raise ValueError(f"Invalid bank name: {bank_name}")

        if hasattr(bank, encoder_name):
            return getattr(bank, encoder_name)
        else:
            raise ValueError(f"Invalid encoder name: {encoder_name}")

    def _create_knob_settings_from_config(
        self, knob_config: dict
    ) -> KnobSettings:
        """
        Creates a KnobSettings object from the knob configuration.

        Args:
            knob_config: A dictionary containing the knob configuration.

        Returns:
            A KnobSettings object.
        """
        knob_type = KnobSettings.KnobType[knob_config["knob_type"]]
        led_color = getattr(constants.ColorValues, knob_config["led_color"])
        min_threshold = float(knob_config["min_threshold"])
        max_threshold = float(knob_config["max_threshold"])
        movement_type = getattr(
            constants.EncoderSettings,
            knob_config.get(
                "movement_type", "MOVEMENTTYPE_DIRECT_HIGHRESOLUTION"
            ),
        )
        encoder_midi_type = getattr(
            constants.EncoderSettings,
            knob_config.get("encoder_midi_type", "MIDITYPE_SENDCC"),
        )
        detent_color = getattr(
            constants.DetentColorValues, knob_config.get("detent_color", "PINK")
        )
        indicator_display_type = getattr(
            constants.EncoderSettings,
            knob_config.get(
                "indicator_display_type", "INDICATORTYPE_BLENDEDBAR"
            ),
        )

        return KnobSettings(
            knob_type=knob_type,
            led_color=led_color,
            min_threshold=min_threshold,
            max_threshold=max_threshold,
            movement_type=movement_type,
            encoder_midi_type=encoder_midi_type,
            detent_color=detent_color,
            indicator_display_type=indicator_display_type,
        )

    def _start_reading_thread(self):
        """
        Starts a background thread to continuously read MIDI messages.
        """
        if self._reading_thread is None:
            self._reading_thread_active = True
            self._reading_thread = threading.Thread(
                target=self._read_messages_loop
            )
            self._reading_thread.daemon = True  # Allow main thread to exit even if reading thread is running
            self._reading_thread.start()

    def _read_messages_loop(self):
        """
        Continuously reads MIDI messages in a loop until stopped.
        """
        while self._reading_thread_active:
            self._read_messages()

    def read_all(self) -> dict:
        """
        Returns the current values of all knobs.
        """
        return {
            encoder_index: encoder.mapped_value
            for encoder_index, encoder in enumerate(self._config._encoders)
        }

    def read_all_changed(self) -> dict:
        """
        Returns the values of all knobs that have changed since the last read.
        """
        changed_values = {}
        for encoder_index, encoder in enumerate(self._config._encoders):
            if encoder.has_changed():
                changed_values[encoder_index] = encoder.mapped_value
        return changed_values

    def read_active(self) -> dict:
        """
        Returns the values of only the active (subscribed) knobs.
        """
        return {
            encoder_index: encoder.mapped_value
            for encoder_index, encoder in enumerate(self._config._encoders)
            if encoder_index in self._knob_subscriptions
        }

    def read_active_changed(self) -> dict:
        """
        Returns the values of active knobs that have changed since the last read.
        """
        changed_values = {}
        for encoder_index, encoder in enumerate(self._config._encoders):
            if (
                encoder_index in self._knob_subscriptions
                and encoder.has_changed()
            ):
                changed_values[encoder_index] = encoder.mapped_value
        return changed_values

    def _read_messages(self):
        """
        Reads a single MIDI message from the device and updates encoder states.
        """
        if self._midi_in and self._input_port is not None:
            try:
                message = self._midi_in.get_message()
                if message:
                    self._handle_midi_message(message)
            except Exception as e:
                print(traceback.format_exc())

    def _handle_midi_message(self, message):
        """
        Handles incoming MIDI messages from the device.
        """
        msg = message[0]
        if len(msg) == 3:
            channel = msg[0] & 0xF
            cc = msg[1]
            value = msg[2]

            # Update encoder value if the message is from an encoder
            if channel == constants.MidiChannels.ROTARY_ENCODER:
                self._config._encoders[cc].value = value
                self._config._encoders[
                    cc
                ].update_mapped_value()  # Update mapped value

                if (
                    self.value_changed_callback
                    and cc in self._knob_subscriptions.keys()
                ):
                    self.value_changed_callback(
                        f"ENCODER_{cc + 1}",
                        self._config._encoders[cc].mapped_value,
                    )

    def close(self):
        """
        Closes the input and output ports and stops the reading thread.
        """
        self._reading_thread_active = False  # Signal thread to stop
        if self._reading_thread is not None:
            self._reading_thread.join()  # Wait for thread to finish
            self._reading_thread = None

        if self._midi_in and self._input_port is not None:
            self._midi_in.close_port()
        if self._midi_out and self._output_port is not None:
            self._midi_out.close_port()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def set_encoder_value(self, encoder: int, value: float):
        """
        Sets the value of a specific encoder.

        Args:
            encoder: The encoder index (0-63)
            value: The value to set. This should be within the min/max range defined for the encoder.
        """
        if encoder not in range(constants.Encoders.DEVICE_KNOB_NUM):
            raise ValueError("Invalid encoder index. Valid range is 0-63")

        encoder_obj = self._config._encoders[encoder]

        # Convert the value to the 0-127 MIDI range based on the encoder's min/max settings
        normalized_value = (value - encoder_obj.knob_settings.min) / (
            encoder_obj.knob_settings.max - encoder_obj.knob_settings.min
        )
        midi_value = int(normalized_value * 127)
        midi_value = max(0, min(127, midi_value))  # Clamp to valid MIDI range

        # Update the internal state
        encoder_obj.value = midi_value
        encoder_obj.mapped_value = value

        # Send the value to the device
        self._send_control_change(
            constants.MidiChannels.ROTARY_ENCODER, encoder, midi_value
        )
