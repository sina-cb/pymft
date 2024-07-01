# pymft: Python Midi Fighter Twister Library

This library provides a simple and easy-to-use interface for interacting with the [Midi Fighter Twister](https://djtechtools.com/product/midifighter-twister/) controller in Python. 

The code in this library is inspired from the [Chromatik MidiFighterTwister library](https://github.com/heronarts/LX/blob/dev/src/main/java/heronarts/lx/midi/surface/MidiFighterTwister.java).

## Features

- **Easy Configuration:** Define knob configurations using the `MidiFighterTwister` class. This library is trying to asbtract the complexity of the Midi Fighter Twister controller interface out of the client code.
- **Knob Configuration:** Define knob settings (type, range, color, detent, movement, MIDI type, etc.) using the `KnobSettings` class.
- **Easy Subscription:** Subscribe to knob changes using `mft.subscribe()`, which automatically applies the defined knob settings to the device.
- **Efficient Reading:**  The library handles reading knob values in the background, allowing you to efficiently query changes using functions like `read_all_changed()`, `read_active_changed()`, `read_all()`, and `read_active()`.
- **JSON Configuration:** Load knob configurations from JSON files, allowing you to define and manage settings easily.

Future developments include:
- **Non-linear Mapping:** Support non-linear min-max mapping for knob values
- **2-way Communication:** Send new knob values to the device to allow 2-way communication between the client code and the hardware
 - **Multiple MFT Devices:** Test with more than 1 MFT device and see if it works

## Installtion
This package is avialable on PyPI: https://pypi.org/project/pymft/

```cmd
  > pip install pymft
```

## Development
This is a step by step guide to get the library set up on your machine.

 1. Install virtualenvwrapper
    **For Windows:**
    ```cmd
      > python.exe -m pip  install virtualenvwrapper-win
    ```
    

    **For Linux:**
    ```cmd
      > sudo python3.11.9 -m pip install virtualenvwrapper
      > export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.11.9
      > source /usr/local/bin/virtualenvwrapper.sh 
    ```
 2. Make the virtual environment
    ```cmd
      > mkvirtualenv -p python3.11.9 mft_py_lib
    ```
 3. Activate the virtual environment
    ```cmd
      > workon mft_py_lib
    ```
- **Note:** You can select the environemnt by pressing CTRL+SHIFT+P in VSCode and Type "Python: Select Interpreter" and select your newly created environment.
 4. Install dependencies
    ```cmd
      > poetry install
      > poetry run demo_main
    ```

### Debug Steps With VSCode
 1. Launch the .vscode/launch.json

### Run the demo using python command
 1. Run
   ```cmd
     > poetry install
   ```
 2. Activate poetry shell
   ```cmd
     > poetry shell
   ```
 3. Run the main file
   ```cmd
     > python .\pymft\pymft\main.py
   ```

### Run utilities
 1. Run black on the project
   ```cmd
     > poetry run black .
   ```
 2. Run isort on the project
   ```cmd
     > poetry run isort .
   ```

# Release to PyPi
 1. Build the distribution
   ```cmd
     > python setup.py sdist
   ```
  2. Install twine and set up credentials
    ```cmd
      > python -m install twine
      > vim ~/.pypirc  # Paste your credentials from pypi
    ```
  3. Publish to PyPi
    ```cmd
      > python -m twine upload dist/*
    ```

# Usage example

  ```python
  from pymft import KnobSettings, MidiFighterTwister, constants

  with MidiFighterTwister() as mft:
      if not mft.discover():
          raise RuntimeError("Could not discover a device")

      # Configure the device
      mft.set_bank(constants.SystemMessages.BANK1)
      mft.set_aux(False)
      mft.config.initialize_defaults()

      # Subscribe to knobs
      mft.subscribe(
          constants.Encoders.Bank1.ENCODER_1,
          KnobSettings(
              knob_type=KnobSettings.KnobType.BIPOLAR,
              color=constants.ColorValues.RED,
              min=-1,
              max=1,
          ),
      )
      mft.subscribe(
          constants.Encoders.Bank1.ENCODER_2,
          KnobSettings(
              knob_type=KnobSettings.KnobType.UNIPOLAR,
              color=constants.ColorValues.PINK,
          ),
      )
      # ... subscribe to more knobs ...

      mft.start()  # Start the reading thread

      while True:
          # Read only active changed knob values
          active_changed_knob_values = mft.read_active_changed()
          if active_changed_knob_values:
              print("Active changed knob values:", active_changed_knob_values)

          # Read all active knob values
          active_knob_values = mft.read_active()
          if active_knob_values:
              print("Active knob values:", active_knob_values)

          time.sleep(0.01)  # Add a small delay
  ```

# Contributing
Contributions are welcome!
Please submit pull requests for new features, bug fixes, or improvements.

# License
This library is licensed under the GNU GENERAL PUBLIC License.

# Contact
If you have any questions or feedback, please open an issue on the GitHub repository.