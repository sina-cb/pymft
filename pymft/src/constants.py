from dataclasses import dataclass

# General Constants
DEVICE_NAME: str = "Midi Fighter Twister"  # The name of the MIDI device
PART_SIZE_BYTES: int = (
    24  # Maximum size of a single SysEx message part (in bytes)
)

# DJTT MIDI Constants
MIDI_MFR_ID_0: int = 0x00
MIDI_MFR_ID_1: int = 0x01
MIDI_MFR_ID_2: int = 0x79


@dataclass
class MidiChannels:
    """
    MIDI channels used for different message types.
    Refer to the "Encoder Settings" section in the PDF.
    """

    ROTARY_ENCODER: int = 0  # Channel for rotary encoder messages (knob twists)
    SWITCH_AND_COLOR: int = 1  # Channel for encoder switch and color messages
    ANIMATIONS_AND_BRIGHTNESS: int = (
        2  # Channel for encoder animations and brightness messages
    )
    SYSTEM: int = (
        3  # Channel for system messages (bank changes, side button actions)
    )
    SHIFT: int = 4  # Channel for shift encoder messages
    SWITCH_ANIMATION: int = 5  # Channel for switch animation messages
    SEQUENCER: int = 7  # Channel for sequencer messages


@dataclass
class EncoderControl:
    """
    Control Change (CC) values used for specific encoder actions.
    Refer to the "Encoder Settings" section in the PDF.
    """

    KNOB_DECREMENT_VERYFAST: int = (
        61  # Value sent for very fast counter-clockwise knob rotation
    )
    KNOB_DECREMENT_FAST: int = (
        62  # Value sent for fast counter-clockwise knob rotation
    )
    KNOB_DECREMENT: int = 63  # Value sent for counter-clockwise knob rotation
    KNOB_INCREMENT: int = 65  # Value sent for clockwise knob rotation
    KNOB_INCREMENT_FAST: int = 66  # Value sent for fast clockwise knob rotation
    KNOB_INCREMENT_VERYFAST: int = (
        67  # Value sent for very fast clockwise knob rotation
    )


@dataclass
class SystemMessages:
    """
    Control Change (CC) values used for system messages.
    Refer to the "Virtual Bank Operation" section in the PDF.
    """

    BANK_OFF: int = 0  # Value sent to turn off a bank
    BANK_ON: int = 127  # Value sent to turn on a bank

    BANK1: int = 0  # CC value for Bank 1
    BANK2: int = 1  # CC value for Bank 2
    BANK3: int = 2  # CC value for Bank 3
    BANK4: int = 3  # CC value for Bank 4

    # CC values for side buttons in each bank
    BANK1_LEFT1: int = 8
    BANK1_LEFT2: int = 9
    BANK1_LEFT3: int = 10
    BANK1_RIGHT1: int = 11
    BANK1_RIGHT2: int = 12
    BANK1_RIGHT3: int = 13

    BANK2_LEFT1: int = 14
    BANK2_LEFT2: int = 15
    BANK2_LEFT3: int = 16
    BANK2_RIGHT1: int = 17
    BANK2_RIGHT2: int = 18
    BANK2_RIGHT3: int = 19

    BANK3_LEFT1: int = 20
    BANK3_LEFT2: int = 21
    BANK3_LEFT3: int = 22
    BANK3_RIGHT1: int = 23
    BANK3_RIGHT2: int = 24
    BANK3_RIGHT3: int = 25

    BANK4_LEFT1: int = 26
    BANK4_LEFT2: int = 27
    BANK4_LEFT3: int = 28
    BANK4_RIGHT1: int = 29
    BANK4_RIGHT2: int = 30
    BANK4_RIGHT3: int = 31


@dataclass
class ColorValues:
    """
    MIDI values for setting RGB colors on the encoders.
    Refer to the "Encoders Push Switches" section in the PDF.
    """

    INACTIVE: int = 0  # Typically blue
    ACTIVE: int = 127  # Typically red

    BLUE: int = 1
    GREEN: int = 50
    RED: int = 80
    YELLOW: int = 64
    PINK: int = 100

    PRIMARY: int = BLUE  # Default color for primary channel
    AUX: int = RED  # Default color for aux channel
    USER: int = GREEN  # Default color for user-defined color


class DetentColorValues:
    """
    MIDI values for setting the detent color on the encoders.
    """

    RED = 0
    PINK = 63
    BLUE = 127


@dataclass
class AnimationValues:
    """
    MIDI values for setting different animation effects for the encoders.
    Refer to the "Setting RGB / Indicator Segment Animation State" section.
    """

    NONE: int = 0  # No animation

    # RGB Strobe Animations
    RGB_TOGGLE_8_BEATS: int = 1  # Toggle RGB color every 8 beats
    RGB_TOGGLE_4_BEATS: int = 2  # Toggle RGB color every 4 beats
    RGB_TOGGLE_2_BEATS: int = 3  # Toggle RGB color every 2 beats
    RGB_TOGGLE_1_BEAT: int = 4  # Toggle RGB color every beat
    RGB_TOGGLE_HALF_BEAT: int = 5  # Toggle RGB color every half beat
    RGB_TOGGLE_QUARTER_BEAT: int = 6  # Toggle RGB color every quarter beat
    RGB_TOGGLE_EIGHTH_BEAT: int = 7  # Toggle RGB color every eighth beat
    RGB_TOGGLE_SIXTEENTH_BEAT: int = 8  # Toggle RGB color every sixteenth beat

    # RGB Pulse Animations
    RGB_PULSE_8_BEATS: int = 10  # Pulse RGB color every 8 beats
    RGB_PULSE_4_BEATS: int = 11  # Pulse RGB color every 4 beats
    RGB_PULSE_2_BEATS: int = 12  # Pulse RGB color every 2 beats
    RGB_PULSE_1_BEAT: int = 13  # Pulse RGB color every beat
    RGB_PULSE_HALF_BEAT: int = 14  # Pulse RGB color every half beat
    RGB_PULSE_QUARTER_BEAT: int = 15  # Pulse RGB color every quarter beat
    RGB_PULSE_EIGHTH_BEAT: int = 16  # Pulse RGB color every eighth beat

    # RGB Brightness Values
    RGB_BRIGHTNESS_OFF: int = 17  # Turn off RGB brightness
    RGB_BRIGHTNESS_MID: int = 32  # Set RGB brightness to mid level
    RGB_BRIGHTNESS_MAX: int = 47  # Set RGB brightness to maximum level

    # Indicator Strobe Animations
    INDICATOR_TOGGLE_8_BEATS: int = 49  # Toggle indicator LED every 8 beats
    INDICATOR_TOGGLE_4_BEATS: int = 50  # Toggle indicator LED every 4 beats
    INDICATOR_TOGGLE_2_BEATS: int = 51  # Toggle indicator LED every 2 beats
    INDICATOR_TOGGLE_1_BEAT: int = 52  # Toggle indicator LED every beat
    INDICATOR_TOGGLE_HALF_BEAT: int = 53  # Toggle indicator LED every half beat
    INDICATOR_TOGGLE_QUARTER_BEAT: int = (
        54  # Toggle indicator LED every quarter beat
    )
    INDICATOR_TOGGLE_EIGHTH_BEAT: int = (
        55  # Toggle indicator LED every eighth beat
    )
    INDICATOR_TOGGLE_SIXTEENTH_BEAT: int = (
        56  # Toggle indicator LED every sixteenth beat
    )

    # Indicator Pulse Animations
    INDICATOR_PULSE_8_BEATS: int = 57  # Pulse indicator LED every 8 beats
    INDICATOR_PULSE_4_BEATS: int = 58  # Pulse indicator LED every 4 beats
    INDICATOR_PULSE_2_BEATS: int = 59  # Pulse indicator LED every 2 beats
    INDICATOR_PULSE_1_BEAT: int = 60  # Pulse indicator LED every beat
    INDICATOR_PULSE_HALF_BEAT: int = 61  # Pulse indicator LED every half beat
    INDICATOR_PULSE_QUARTER_BEAT: int = (
        62  # Pulse indicator LED every quarter beat
    )
    INDICATOR_PULSE_EIGHTH_BEAT: int = (
        63  # Pulse indicator LED every eighth beat
    )
    INDICATOR_PULSE_SIXTEENTH_BEAT: int = (
        64  # Pulse indicator LED every sixteenth beat
    )

    # Indicator Brightness Values
    INDICATOR_BRIGHTNESS_OFF: int = 65  # Turn off indicator brightness
    INDICATOR_BRIGHTNESS_25: int = 72  # Set indicator brightness to 25%
    INDICATOR_BRIGHTNESS_MID: int = 80  # Set indicator brightness to mid level
    INDICATOR_BRIGHTNESS_MAX: int = (
        95  # Set indicator brightness to maximum level
    )

    # Rainbow Cycle Animation
    RAINBOW_CYCLE: int = 127  # Set RGB segment to a rainbow cycle animation


@dataclass
class EncoderSettings:
    """
    Values used for configuring the encoder settings.
    Refer to the "Encoder Settings" section in the PDF.
    """

    # Encoder Control Type Constants (Not currently used in the firmware - for future use)
    CONTROLTYPE_ENCODER: int = 0x00  # Encoder sends MIDI messages
    CONTROLTYPE_SWITCH: int = 0x01  # Switch sends MIDI messages
    CONTROLTYPE_SHIFT: int = 0x02  # Reserved for future functionality

    # Encoder Movement Type Constants
    MOVEMENTTYPE_DIRECT_HIGHRESOLUTION: int = (
        0x00  # The highest resolution movement available
    )
    MOVEMENTTYPE_RESPONSIVE: int = 0x01  # Responsive movement.
    MOVEMENTTYPE_VELOCITYSENSITIVE: int = 0x02  # Velocity-sensitive movement.

    # Encoder Switch Action Type Constants
    SWACTION_CCHOLD: int = 0x00  # Switch sends a CC message
    SWACTION_CCTOGGLE: int = 0x01  # Switch toggles CC
    SWACTION_NOTEHOLD: int = 0x02  # Switch sends a Note On
    SWACTION_NOTETOGGLE: int = 0x03  # Switch toggles Note On/Off
    SWACTION_ENCRESETVALUE: int = 0x04  # Switch resets the encoder value
    SWACTION_ENCFINEADJUST: int = (
        0x05  # Encoder sensitivity reduced for fine adjustment
    )
    SWACTION_SHIFTHOLD: int = 0x06  # Encoder sends a secondary value
    SWACTION_SHIFTTOGGLE: int = (
        0x07  # Switch toggles between primary/secondary values
    )

    # Encoder MIDI Message Type Constants
    MIDITYPE_SENDNOTE: int = 0x00  # Encoder sends Note On messages
    MIDITYPE_SENDCC: int = 0x01  # Encoder sends Control Change messages
    MIDITYPE_SENDRELENC: int = 0x02  # Encoder sends relative CC messages
    MIDITYPE_SENDNOTEOFF: int = 0x03  # Encoder sends Note Off messages
    MIDITYPE_SENDSWITCHVELCONTROL: int = 0x03  # Not currently used
    MIDITYPE_SENDRELENCMOUSEEMUDRAG: int = 0x04  # Not currently used
    MIDITYPE_SENDRELENCMOUSEEMUSCROLL: int = 0x05  # Not currently used

    # Encoder Indicator Display Type Constants
    INDICATORTYPE_DOT: int = 0x00  # Indicator displays a single LED
    INDICATORTYPE_BAR: int = 0x01  # Indicator displays a bar graph
    INDICATORTYPE_BLENDEDBAR: int = (
        0x02  # Indicator displays a blended bar graph
    )
    INDICATORTYPE_BLENDEDDOT: int = 0x03  # Indicator displays a blended dot


@dataclass
class SysExCommands:
    """
    SysEx commands used for configuring the MFT.
    Refer to the "Encoder Settings" section in the PDF.
    """

    PUSH_CONF: int = 0x01  # Command to push configuration to the MFT
    PULL_CONF: int = 0x02  # Command to pull configuration from the MFT
    SYSTEM: int = 0x03  # Command for system-related SysEx messages
    BULK_XFER: int = 0x04  # Command for bulk transfer of encoder settings


@dataclass
class SysExValues:
    """
    Values used in SysEx messages.
    Refer to the "Encoder Settings" section in the PDF.
    """

    FALSE: int = 0x00  # Value for false
    TRUE: int = 0x01  # Value for true


@dataclass
class GlobalSideSwitchAction:
    """
    Actions for side switch buttons.
    Refer to the "Global Settings" section in the PDF.
    """

    CCHOLD: int = 0x00  # Side switch sends a CC message
    CCTOGGLE: int = 0x01  # Side switch toggles CC
    NOTEHOLD: int = 0x02  # Side switch sends a Note On
    NOTETOGGLE: int = 0x03  # Side switch toggles Note On/Off
    SHIFTPAGE1: int = 0x04  # Side switch activates a secondary 'Shift' page
    SHIFTPAGE2: int = 0x05  # Side switch activates a secondary 'Shift' page
    BANKUP: int = 0x06  # Side switch increments the bank selection
    BANKDOWN: int = 0x07  # Side switch decrements the bank selection
    BANK1: int = 0x08  # Side switch selects Bank 1
    BANK2: int = 0x09  # Side switch selects Bank 2
    BANK3: int = 0x0A  # Side switch selects Bank 3
    BANK4: int = 0x0B  # Side switch selects Bank 4
    CYCLE_BANK: int = 0x0C  # Side switch cycles through the banks


@dataclass
class Encoders:
    """
    Encoder constants for the MFT device.
    Refer to the "Midi Fighter Twister Hardware" section in the PDF.
    """

    DEVICE_KNOB_PER_BANK: int = 16  # Number of encoders per bank
    DEVICE_KNOB_NUM: int = 64  # Total number of encoders
    DEVICE_KNOB_MAX: int = DEVICE_KNOB_NUM  # Maximum encoder index
    DEVICE_BANK_NUM: int = 4  # Number of banks

    @dataclass
    class Bank1:
        ENCODER_1: int = 0
        ENCODER_2: int = 1
        ENCODER_3: int = 2
        ENCODER_4: int = 3
        ENCODER_5: int = 4
        ENCODER_6: int = 5
        ENCODER_7: int = 6
        ENCODER_8: int = 7
        ENCODER_9: int = 8
        ENCODER_10: int = 9
        ENCODER_11: int = 10
        ENCODER_12: int = 11
        ENCODER_13: int = 12
        ENCODER_14: int = 13
        ENCODER_15: int = 14
        ENCODER_16: int = 15

    @dataclass
    class Bank2:
        ENCODER_1: int = 16
        ENCODER_2: int = 17
        ENCODER_3: int = 18
        ENCODER_4: int = 19
        ENCODER_5: int = 20
        ENCODER_6: int = 21
        ENCODER_7: int = 22
        ENCODER_8: int = 23
        ENCODER_9: int = 24
        ENCODER_10: int = 25
        ENCODER_11: int = 26
        ENCODER_12: int = 27
        ENCODER_13: int = 28
        ENCODER_14: int = 29
        ENCODER_15: int = 30
        ENCODER_16: int = 31

    @dataclass
    class Bank3:
        ENCODER_1: int = 32
        ENCODER_2: int = 33
        ENCODER_3: int = 34
        ENCODER_4: int = 35
        ENCODER_5: int = 36
        ENCODER_6: int = 37
        ENCODER_7: int = 38
        ENCODER_8: int = 39
        ENCODER_9: int = 40
        ENCODER_10: int = 41
        ENCODER_11: int = 42
        ENCODER_12: int = 43
        ENCODER_13: int = 44
        ENCODER_14: int = 45
        ENCODER_15: int = 46
        ENCODER_16: int = 47

    @dataclass
    class Bank4:
        ENCODER_1: int = 48
        ENCODER_2: int = 49
        ENCODER_3: int = 50
        ENCODER_4: int = 51
        ENCODER_5: int = 52
        ENCODER_6: int = 53
        ENCODER_7: int = 54
        ENCODER_8: int = 55
        ENCODER_9: int = 56
        ENCODER_10: int = 57
        ENCODER_11: int = 58
        ENCODER_12: int = 59
        ENCODER_13: int = 60
        ENCODER_14: int = 61
        ENCODER_15: int = 62
        ENCODER_16: int = 63


class Constants:
    def __init__(self):
        self.MidiChannels = MidiChannels()
        self.EncoderControl = EncoderControl()
        self.SystemMessages = SystemMessages()
        self.ColorValues = ColorValues()
        self.DetentColorValues = DetentColorValues()
        self.AnimationValues = AnimationValues()
        self.EncoderSettings = EncoderSettings()
        self.SysExCommands = SysExCommands()
        self.SysExValues = SysExValues()
        self.GlobalSideSwitchAction = GlobalSideSwitchAction()
        self.Encoders = Encoders()

        # Add the missing attributes
        self.DEVICE_NAME = DEVICE_NAME
        self.PART_SIZE_BYTES = PART_SIZE_BYTES
        self.MIDI_MFR_ID_0 = MIDI_MFR_ID_0
        self.MIDI_MFR_ID_1 = MIDI_MFR_ID_1
        self.MIDI_MFR_ID_2 = MIDI_MFR_ID_2


constants = Constants()
