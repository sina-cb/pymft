from enum import Enum

from pymft.src.constants import constants


class KnobSettings:
    """
    Represents the configuration settings for a knob.
    """

    class KnobType(Enum):
        UNIPOLAR = "unipolar"
        BIPOLAR = "bipolar"

    def __init__(
        self,
        knob_type: KnobType | None = None,
        min_threshold: float | None = None,
        max_threshold: float | None = None,
        movement_type: int | None = None, # Use values from constants.EncoderSettings.MOVEMENTTYPE_*
        switch_action_type: int | None = None, # Use values from constants.EncoderSettings.SWACTION_*
        encoder_midi_type: int | None = None, # Use values from constants.EncoderSettings.MIDITYPE_*
        led_color: int | None = None, # Use values from constants.ColorValues
        detent_color: int | None = None, # Use values from constants.DetentColorValues
        indicator_display_type: int | None = None, # Use values from constants.EncoderSettings.INDICATORTYPE_*
    ):

        # Internal setting values and modification flag
        self._knob_type = knob_type

        # Set default detent based on knob_type
        if knob_type == self.KnobType.BIPOLAR:
            self._detent = constants.SysExValues.TRUE
        else:
            self._detent = constants.SysExValues.FALSE

        self._min = min_threshold if min_threshold is not None else (-1 if knob_type == self.KnobType.BIPOLAR else 0)
        self._max = max_threshold if max_threshold is not None else (1 if knob_type == self.KnobType.BIPOLAR else 1)
        assert self._min < self._max, "min must be less than max"

        self._movement_type = movement_type
        self._switch_action_type = switch_action_type
        self._switch_midi_channel = 2
        self._switch_midi_number = (
            None  # Needs to be initialized by the default config
        )
        self._switch_midi_type = 0
        self._encoder_midi_channel = 1
        self._encoder_midi_number = (
            None  # Needs to be initialized by the default config
        )
        self._encoder_midi_type = encoder_midi_type
        self._active_color = led_color
        self._inactive_color = led_color
        self._detent_color = detent_color
        self._indicator_display_type = indicator_display_type
        self._is_super_knob = (
            False  # Super knobs are not supported in this version
        )
        self._encoder_shift_midi_channel = 0
        self._is_modified = False

    @property
    def knob_type(self) -> KnobType | None:
        return self._knob_type

    @knob_type.setter
    def knob_type(self, value: KnobType | None):
        if self._knob_type != value:
            self._knob_type = value
            self._is_modified = True

    @property
    def min(self) -> float | None:
        return self._min

    @min.setter
    def min(self, value: float | None):
        if self._min != value:
            self._min = value
            self._is_modified = True

    @property
    def max(self) -> float | None:
        return self._max

    @max.setter
    def max(self, value: float | None):
        if self._max != value:
            self._max = value
            self._is_modified = True

    # Properties for accessing and setting values
    @property
    def detent(self) -> bool | None:
        return self._detent

    @detent.setter
    def detent(self, value: bool | None):
        if self._detent != value:
            self._detent = value
            self._is_modified = True

    @property
    def movement_type(self) -> int | None:
        return self._movement_type

    @movement_type.setter
    def movement_type(self, value: int | None):
        if self._movement_type != value:
            self._movement_type = value
            self._is_modified = True

    @property
    def switch_action_type(self) -> int | None:
        return self._switch_action_type

    @switch_action_type.setter
    def switch_action_type(self, value: int | None):
        if self._switch_action_type != value:
            self._switch_action_type = value
            self._is_modified = True

    @property
    def switch_midi_channel(self) -> int | None:
        return self._switch_midi_channel

    @switch_midi_channel.setter
    def switch_midi_channel(self, value: int | None):
        if self._switch_midi_channel != value:
            self._switch_midi_channel = value
            self._is_modified = True

    @property
    def switch_midi_number(self) -> int | None:
        return self._switch_midi_number

    @switch_midi_number.setter
    def switch_midi_number(self, value: int | None):
        if self._switch_midi_number != value:
            self._switch_midi_number = value
            self._is_modified = True

    @property
    def switch_midi_type(self) -> int | None:
        return self._switch_midi_type

    @switch_midi_type.setter
    def switch_midi_type(self, value: int | None):
        if self._switch_midi_type != value:
            self._switch_midi_type = value
            self._is_modified = True

    @property
    def encoder_midi_channel(self) -> int | None:
        return self._encoder_midi_channel

    @encoder_midi_channel.setter
    def encoder_midi_channel(self, value: int | None):
        if self._encoder_midi_channel != value:
            self._encoder_midi_channel = value
            self._is_modified = True

    @property
    def encoder_midi_number(self) -> int | None:
        return self._encoder_midi_number

    @encoder_midi_number.setter
    def encoder_midi_number(self, value: int | None):
        if self._encoder_midi_number != value:
            self._encoder_midi_number = value
            self._is_modified = True

    @property
    def encoder_midi_type(self) -> int | None:
        return self._encoder_midi_type

    @encoder_midi_type.setter
    def encoder_midi_type(self, value: int | None):
        if self._encoder_midi_type != value:
            self._encoder_midi_type = value
            self._is_modified = True

    @property
    def active_color(self) -> int | None:
        return self._active_color

    @active_color.setter
    def active_color(self, value: int | None):
        if self._active_color != value:
            self._active_color = value
            self._is_modified = True

    @property
    def inactive_color(self) -> int | None:
        return self._inactive_color

    @inactive_color.setter
    def inactive_color(self, value: int | None):
        if self._inactive_color != value:
            self._inactive_color = value
            self._is_modified = True

    @property
    def detent_color(self) -> int | None:
        return self._detent_color

    @detent_color.setter
    def detent_color(self, value: int | None):
        if self._detent_color != value:
            self._detent_color = value
            self._is_modified = True

    @property
    def indicator_display_type(self) -> int | None:
        return self._indicator_display_type

    @indicator_display_type.setter
    def indicator_display_type(self, value: int | None):
        if self._indicator_display_type != value:
            self._indicator_display_type = value
            self._is_modified = True

    @property
    def is_super_knob(self) -> bool | None:
        return self._is_super_knob

    @is_super_knob.setter
    def is_super_knob(self, value: bool | None):
        if self._is_super_knob != value:
            self._is_super_knob = value
            self._is_modified = True

    @property
    def encoder_shift_midi_channel(self) -> int | None:
        return self._encoder_shift_midi_channel

    @encoder_shift_midi_channel.setter
    def encoder_shift_midi_channel(self, value: int | None):
        if self._encoder_shift_midi_channel != value:
            self._encoder_shift_midi_channel = value
            self._is_modified = True

    def is_modified(self) -> bool:
        """
        Returns True if any setting has been modified.
        """
        return self._is_modified
