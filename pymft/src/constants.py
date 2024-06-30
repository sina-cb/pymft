
class Constants:
    # MIDI Device Name 
    DEVICE_NAME = "Midi Fighter Twister"

    # Encoder Settings
    PART_SIZE_BYTES = 24

    # MIDI Channels
    CHANNEL_ROTARY_ENCODER = 0
    CHANNEL_SWITCH_AND_COLOR = 1
    CHANNEL_ANIMATIONS_AND_BRIGHTNESS = 2
    CHANNEL_SYSTEM = 3
    CHANNEL_SHIFT = 4
    CHANNEL_SWITCH_ANIMATION = 5
    CHANNEL_SEQUENCER = 7

    # MIDI ControlChanges on knob-related channels
    DEVICE_KNOB = 0
    DEVICE_BANK_NUM = 4
    DEVICE_KNOB_PER_BANK = 16
    DEVICE_KNOB_NUM = 64
    DEVICE_KNOB_MAX = DEVICE_KNOB + DEVICE_KNOB_NUM
    KNOB_DECREMENT_VERYFAST = 61
    KNOB_DECREMENT_FAST = 62
    KNOB_DECREMENT = 63
    KNOB_INCREMENT = 65
    KNOB_INCREMENT_FAST = 66
    KNOB_INCREMENT_VERYFAST = 67
    KNOB_TICKS_PER_DISCRETE_INCREMENT = 8

    # MIDI ControlChanges on System channel
    BANK1 = 0
    BANK2 = 1
    BANK3 = 2
    BANK4 = 3

    BANK1_LEFT1 = 8
    BANK1_LEFT2 = 9
    BANK1_LEFT3 = 10
    BANK1_RIGHT1 = 11
    BANK1_RIGHT2 = 12
    BANK1_RIGHT3 = 13

    BANK2_LEFT1 = 14
    BANK2_LEFT2 = 15
    BANK2_LEFT3 = 16
    BANK2_RIGHT1 = 17
    BANK2_RIGHT2 = 18
    BANK2_RIGHT3 = 19

    BANK3_LEFT1 = 20
    BANK3_LEFT2 = 21
    BANK3_LEFT3 = 22
    BANK3_RIGHT1 = 23
    BANK3_RIGHT2 = 24
    BANK3_RIGHT3 = 25

    BANK4_LEFT1 = 26
    BANK4_LEFT2 = 27
    BANK4_LEFT3 = 28
    BANK4_RIGHT1 = 29
    BANK4_RIGHT2 = 30
    BANK4_RIGHT3 = 31

    # MIDI Notes on Color channel
    RGB_INACTIVE_COLOR = 0
    RGB_ACTIVE_COLOR = 127
    # To set RGB to any color use values 1-126
    RGB_BLUE = 1
    RGB_GREEN = 50
    RGB_RED = 80
    RGB_YELLOW = 64
    RGB_PINK = 100

    RGB_PRIMARY = RGB_BLUE
    RGB_AUX = RGB_RED
    RGB_USER = RGB_GREEN

    # MIDI Notes on Animation channel
    RGB_ANIMATION_NONE = 0
    RGB_TOGGLE_EVERY_8_BEATS = 1
    RGB_TOGGLE_EVERY_4_BEATS = 2
    RGB_TOGGLE_EVERY_2_BEATS = 3
    RGB_TOGGLE_EVERY_BEAT = 4
    RGB_TOGGLE_EVERY_HALF_BEAT = 5
    RGB_TOGGLE_EVERY_QUARTER_BEAT = 6
    RGB_TOGGLE_EVERY_EIGTH_BEAT = 7
    RGB_TOGGLE_EVERY_SIXTEENTH_BEAT = 8
    RGB_PULSE_EVERY_8_BEATS = 10
    RGB_PULSE_EVERY_4_BEATS = 11
    RGB_PULSE_EVERY_2_BEATS = 12
    RGB_PULSE_EVERY_BEAT = 13
    RGB_PULSE_EVERY_HALF_BEAT = 14
    RGB_PULSE_EVERY_QUARTER_BEAT = 15
    RGB_PULSE_EVERY_EIGTH_BEAT = 16
    RGB_BRIGHTNESS_OFF = 17
    RGB_BRIGHTNESS_MID = 32
    RGB_BRIGHTNESS_MAX = 47
    # Note: All values between 17 and 47 can be used for RGB brightness
    
    INDICATOR_ANIMATION_NONE = 48
    INDICATOR_TOGGLE_EVERY_8_BEATS = 49
    INDICATOR_TOGGLE_EVERY_4_BEATS = 50
    INDICATOR_TOGGLE_EVERY_2_BEATS = 51
    INDICATOR_TOGGLE_EVERY_BEAT = 52
    INDICATOR_TOGGLE_EVERY_HALF_BEAT = 53
    INDICATOR_TOGGLE_EVERY_QUARTER_BEAT = 54
    INDICATOR_TOGGLE_EVERY_EIGTH_BEAT = 55
    INDICATOR_TOGGLE_EVERY_SIXTEENTH_BEAT = 56
    INDICATOR_PULSE_EVERY_8_BEATS = 57
    INDICATOR_PULSE_EVERY_4_BEATS = 58
    INDICATOR_PULSE_EVERY_2_BEATS = 59
    INDICATOR_PULSE_EVERY_BEAT = 60
    INDICATOR_PULSE_EVERY_HALF_BEAT = 61
    INDICATOR_PULSE_EVERY_QUARTER_BEAT = 62
    INDICATOR_PULSE_EVERY_EIGTH_BEAT = 63
    INDICATOR_PULSE_EVERY_SIXTEENTH_BEAT = 64
    INDICATOR_BRIGHTNESS_OFF = 65
    INDICATOR_BRIGHTNESS_25 = 72
    INDICATOR_BRIGHTNESS_MID = 80
    INDICATOR_BRIGHTNESS_MAX = 95
    # Note: All values between 65 and 95 can be used for Indicator brightness
    RAINBOW_CYCLE = 127

    # MIDI Notes on System Channel
    BANK_OFF = 0
    BANK_ON = 127

    # DJTT MIDI Constants
    MIDI_MFR_ID_0 = 0x00
    MIDI_MFR_ID_1 = 0x01
    MIDI_MFR_ID_2 = 0x79
    # public static final byte MANUFACTURER_ID = 0x0179;

    # DJTT SysEx Commands
    SYSEX_COMMAND_PUSH_CONF = 0x01
    SYSEX_COMMAND_PULL_CONF = 0x02
    SYSEX_COMMAND_SYSTEM = 0x03
    SYSEX_COMMAND_BULK_XFER = 0x04

    # DJTT Config Sizes
    CFG_COUNT_ENC = 15
    CFG_COUNT_GLOBAL = 12

    # DJTT Config Values
    CFG_FALSE = 0x00
    CFG_TRUE = 0x01

    # Global Side Switch Action Type Constants
    CFG_GLOBAL_SSACTION_CCHOLD = 0x00  # Side switch sends a CC message of value 127 when pressed and 0 when released.
    CFG_GLOBAL_SSACTION_CCTOGGLE = 0x01  # Side switch toggles between CC 127 and CC 0 with each press.
    CFG_GLOBAL_SSACTION_NOTEHOLD = 0x02  # Side switch sends a Note On with velocity 127 when pressed and Note Off with velocity 0 when released.
    CFG_GLOBAL_SSACTION_NOTETOGGLE = 0x03  # Side switch toggles between Note On and Note Off with each press.
    CFG_GLOBAL_SSACTION_SHIFTPAGE1 = 0x04  # Side switch activates a secondary 'Shift' page.  Refer to PDF appendix for details.
    CFG_GLOBAL_SSACTION_SHIFTPAGE2 = 0x05  # Side switch activates a secondary 'Shift' page.  Refer to PDF appendix for details.
    CFG_GLOBAL_SSACTION_BANKUP = 0x06  # Side switch increments the bank selection. 
    CFG_GLOBAL_SSACTION_BANKDOWN = 0x07  # Side switch decrements the bank selection.
    CFG_GLOBAL_SSACTION_BANK1 = 0x08  # Side switch selects Bank 1.
    CFG_GLOBAL_SSACTION_BANK2 = 0x09  # Side switch selects Bank 2.
    CFG_GLOBAL_SSACTION_BANK3 = 0x0A  # Side switch selects Bank 3.
    CFG_GLOBAL_SSACTION_BANK4 = 0x0B  # Side switch selects Bank 4.
    CFG_GLOBAL_SSACTION_CYCLE_BANK = 0x0C  # Side switch cycles through the banks (1, 2, 3, 4, 1, ...). 

    # Encoder Control Type Constants (Not currently used in the firmware - for future use)
    CFG_ENC_CONTROLTYPE_ENCODER = 0x00  # Encoder sends MIDI messages
    CFG_ENC_CONTROLTYPE_SWITCH = 0x01  # Switch sends MIDI messages
    CFG_ENC_CONTROLTYPE_SHIFT = 0x02  # Reserved for future functionality

    # Encoder Movement Type Constants
    CFG_ENC_MOVEMENTTYPE_DIRECT_HIGHRESOLUTION = 0x00  # The highest resolution movement available for the encoder.
    CFG_ENC_MOVEMENTTYPE_EMULATION_RESPONSIVE = 0x01  # Responsive movement. 270 degrees of rotation changes the CC by the full MIDI range of 127.
    CFG_ENC_MOVEMENTTYPE_VELOCITYSENSITIVE = 0x02  # Velocity-sensitive movement.  The faster the encoder is turned, the greater the CC change.

    # Encoder Switch Action Type Constants
    CFG_ENC_SWACTION_CCHOLD = 0x00  # Switch sends a CC message of value 127 when pressed and 0 when released.
    CFG_ENC_SWACTION_CCTOGGLE = 0x01  # Switch toggles between CC 127 and CC 0 with each press.
    CFG_ENC_SWACTION_NOTEHOLD = 0x02  # Switch sends a Note On with velocity 127 when pressed and Note Off with velocity 0 when released.
    CFG_ENC_SWACTION_NOTETOGGLE = 0x03  # Switch toggles between Note On and Note Off with each press.
    CFG_ENC_SWACTION_ENCRESETVALUE = 0x04  # Switch resets the encoder value to 0 (or 63 if Detent is enabled).
    CFG_ENC_SWACTION_ENCFINEADJUST = 0x05  # When pressed, the encoder sensitivity is reduced for fine adjustment.
    CFG_ENC_SWACTION_SHIFTHOLD = 0x06  # While the switch is pressed, the encoder sends a secondary value, allowing one encoder to control two knobs independently.
    CFG_ENC_SWACTION_SHIFTTOGGLE = 0x07  # When pressed, the switch toggles between primary and secondary (shift) encoder values.

    # Encoder MIDI Message Type Constants
    CFG_ENC_MIDITYPE_SENDNOTE = 0x00  # Encoder sends Note On messages where the velocity corresponds to the Encoder Value.
    CFG_ENC_MIDITYPE_SENDCC = 0x01  # Encoder sends Control Change messages with a value corresponding to the Encoder Value.
    CFG_ENC_MIDITYPE_SENDRELENC = 0x02  # Encoder sends relative Control Change messages.  65 for increment, 63 for decrement.
    CFG_ENC_MIDITYPE_SENDNOTEOFF = 0x03  # Encoder sends Note Off messages when the switch is pressed.
    CFG_ENC_MIDITYPE_SENDSWITCHVELCONTROL = 0x03  # Encoder sends a Note Off message with velocity corresponding to the encoder value.  Not currently used.
    CFG_ENC_MIDITYPE_SENDRELENCMOUSEEMUDRAG = 0x04  # Encoder sends relative Control Change messages to control mouse dragging.  Not currently used.
    CFG_ENC_MIDITYPE_SENDRELENCMOUSEEMUSCROLL = 0x05  # Encoder sends relative Control Change messages to control mouse scrolling.  Not currently used.

    # Encoder Indicator Display Type Constants
    CFG_ENC_INDICATORTYPE_DOT = 0x00  # Indicator displays a single LED (dot).
    CFG_ENC_INDICATORTYPE_BAR = 0x01  # Indicator displays a bar graph.
    CFG_ENC_INDICATORTYPE_BLENDEDBAR = 0x02  # Indicator displays a blended bar graph (the leading LED changes brightness).
    CFG_ENC_INDICATORTYPE_BLENDEDDOT = 0x03  # Indicator displays a blended dot (the dot's brightness changes).