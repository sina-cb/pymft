import argparse
import time

from pymft import KnobSettings, MidiFighterTwister, constants


def value_changed_callback(encoder, value):
    print(f"Encoder {encoder} changed to {value}")


def run():
    """
    Demo usage of the pymft library.
    """
    with MidiFighterTwister() as mft:
        if not mft.discover():
            raise RuntimeError("Could not discover a device")

        # Configure the device
        mft.set_bank(constants.SystemMessages.BANK1)
        mft.set_aux(False)
        mft.config.initialize_defaults()

        # Load configuration from JSON file
        config_path = (
            "./pymft/sample_config.json"  # Path to your JSON config file
        )
        mft.load_config(config_path)

        # Maybe even fruther customize the loaded config for a specific encoder
        mft.subscribe(
            constants.Encoders.Bank1.ENCODER_5,
            KnobSettings(
                knob_type=KnobSettings.KnobType.BIPOLAR,
                led_color=constants.ColorValues.YELLOW,
                min_threshold=-10,
                max_threshold=10,
                movement_type=constants.EncoderSettings.MOVEMENTTYPE_DIRECT_HIGHRESOLUTION,
                detent_color=constants.DetentColorValues.BLUE,
            ),
        )

        mft.set_value_changed_callback(value_changed_callback)

        mft.configure()
        mft.start()  # Start the reading thread

        while True:
            # Read only active changed knob values
            active_changed_knob_values = mft.read_active_changed()
            if active_changed_knob_values:
                print("Active changed knob values:", active_changed_knob_values)

            # Or read all active knob values
            active_knob_values = mft.read_active()
            if active_changed_knob_values:
                print("Active knob values:", active_knob_values)

            time.sleep(0.01)  # Add a small delay


def version():
    """
    Prints the pymft library version
    """
    from pymft import __version__

    print(__version__)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Midi Fighter Twister demo")

    run()
