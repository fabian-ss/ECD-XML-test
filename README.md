# Technical Test for Developers
This is my solved test.

## Description
The following program was written in Python and follows the structure below:

No additional library needs to be installed, nor any virtual environment needs to be set up. This script was made with Python version 3.10.12, but I believe it can work for version 3 in general.

## Instructions
To execute the program, there are 2 ways:

    1) Place a terminal in the directory of the "main.py" file and execute it using the command "python3 main.py".
    2) Execute the file ./run_program.sh

The config.json file serves as the program's configuration file, but its presence is not essential for script execution.

    1) custom_dir: Used to change the location of the XML files folder.
    2) xml_dir: The name of the XML folder, in this case, is "xml repo" because that's how it was specified in the instructions.
    3) liquidacion_num: It is a parameter that represents the field "<liquidacion num_liq="0">" that exists within the XML file. By default, it is 0 because that was required, but this field serves to automate other searches such as "num_liq=1" or "num_liq=2", etc.

## Repository
Gitlab: https://gitlab.com/randommusicd/ecd-xml-test-jf (only need LogIn)
