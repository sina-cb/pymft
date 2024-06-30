import argparse

from pymft import MidiFighterTwister, Config, constants

def handle_midi_message(msg):
    """
    Example function to process incoming MIDI messages.
    This is a basic example - you'll need to tailor it to your project.
    """
    if msg is not None:  # Check if msg is not empty
        # Access individual bytes of the message
        channel = msg[0][0] & 0xF  # Get channel from the first byte
        cc = msg[0][1]
        data = msg[0][2]

        if channel == 3:
            print(f"Channel: {channel}, Bank: {cc}")
        else:
            print(f"Channel: {channel}, CC: {cc}, Value: {data}")

        # Example: Handle encoder value changes
        if channel == 0:  # Encoder Channel
            if cc >= constants.DEVICE_KNOB and cc <= constants.DEVICE_KNOB_MAX:
                knob_index = cc - constants.DEVICE_KNOB
                
                # Process knob values based on their configuration
                if knob_index < 4:
                    # First 4 knobs: 0-1 (Unipolar)
                    # Relative CC: 65 = increment, 63 = decrement
                    value = (data - 64) / 127  # Normalize to 0-1
                    print(f"Knob {knob_index + 1}: {value:.2f}")  # Print normalized value
                elif knob_index < 8:
                    # Next 4 knobs: -1 to 1 (Bipolar)
                    # Relative CC: 65 = increment, 63 = decrement
                    value = (data - 64) / 63.5  # Normalize to -1 to 1
                    print(f"Knob {knob_index + 1}: {value:.2f}")  # Print bipolar value
                elif knob_index < 12:
                    # Next 4 knobs: Directional (Negative/Positive)
                    if data == 65:
                        print(f"Knob {knob_index + 1}: Positive")
                    elif data == 63:
                        print(f"Knob {knob_index + 1}: Negative")
                else:
                    # Last 4 knobs: 0-255 (Absolute CC)
                    print(f"Knob {knob_index + 1}: {data}")

def run():
    """
    Demo usage of the pymft library.
    """
    with MidiFighterTwister() as mft:
        if mft.discover():
            print("Midi Fighter Twister found!")

            # Configure the device
            mft.set_bank(constants.BANK1)  # Set the bank to 1
            mft.set_aux(False)              # Set to primary channel

            # Create a Config object
            config = Config(mft._midi_out)

            # Initialize with defaults
            config.initialize_defaults()
            # config.initialize_lx_defaults()

            # Customize Encoder Settings
            # First 4: 0-1 (Unipolar)
            for i in range(4):
                config._encoders[i].set("encoder_midi_type", constants.CFG_ENC_MIDITYPE_SENDRELENC)  # Use Relative CC
                config._encoders[i].set_detent(False)
                config._encoders[i].set("encoder_midi_channel", 0)  # Set channel to 0

            # Next 4: -1 to 1 (Bipolar)
            for i in range(4, 8):
                config._encoders[i].set("encoder_midi_type", constants.CFG_ENC_MIDITYPE_SENDRELENC)  # Use Relative CC
                config._encoders[i].set_detent(False)
                config._encoders[i].set("encoder_midi_channel", 0)  # Set channel to 0

            # Next 4: Directional (Negative/Positive)
            for i in range(8, 12):
                # Use Note On/Off for directional control
                config._encoders[i].set("encoder_midi_type", constants.CFG_ENC_MIDITYPE_SENDNOTE)
                config._encoders[i].set_detent(False)
                config._encoders[i].set("switch_action_type", constants.CFG_ENC_SWACTION_NOTETOGGLE)
                config._encoders[i].set("encoder_midi_channel", 0)  # Set channel to 0

            # Last 4: 0-255 (Absolute CC)
            for i in range(12, 16):
                config._encoders[i].set("encoder_midi_type", constants.CFG_ENC_MIDITYPE_SENDCC)
                config._encoders[i].set("switch_action_type", constants.CFG_ENC_SWACTION_ENCRESETVALUE)
                config._encoders[i].set_detent(False)
                config._encoders[i].set("encoder_midi_channel", 0)  # Set channel to 0

            # Send the configuration
            config.send_all()

            while True:
                # Read incoming messages
                for msg in mft.read_messages():
                    handle_midi_message(msg)

        else:
            print("Midi Fighter Twister not found.")

def version():
    """
    Prints the pymft library version
    """
    from pymft import __version__
    print(__version__)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Midi Fighter Twister demo')
    parser.add_argument('--test', type=str, default=constants.BANK1,
                        help='Test Argument with no real use')
    args = parser.parse_args()
    print("Test argument: ", args.test)

    run()