# Initial set up
This is a step by step guide to get the library set up on your machine.

 1. Install virtualenvwrapper
    **For Windows:**
    > python.exe -m pip  install virtualenvwrapper-win

    **For Linux:**
    > sudo python3.11.9 -m pip install virtualenvwrapper
    > export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.11.9
    > source /usr/local/bin/virtualenvwrapper.sh 
 2. Make the virtual environment
    > mkvirtualenv -p python3.11.9 mft_py_lib
 3. Activate the virtual environment
    > workon mft_py_lib
- **Note:** You can select the environemnt by pressing CTRL+SHIFT+P in VSCode and Type "Python: Select Interpreter" and select your newly created environment.
 4. Install dependencies
   > poetry install
   > poetry run demo_main


# Debug Steps With VSCode
 1. Launch the .vscode/launch.json

# Run the demo using python command
 1. Run
   > poetry install
 2. Activate poetry shell
   > poetry shell
 3. Run the main file
   > python .\pymft\pymft\main.py