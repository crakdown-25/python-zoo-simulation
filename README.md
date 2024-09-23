# Zoo Simulation

## Overview

This project allows to run a simplified simulation of Plant/Animal life in a ZooPark's paddock.

## Files

- **README.md** : This file
- **Makefile** : File to automatically run tests. Targets : all, mypy, pytest.
- **requirements.txt** : List of libraries needed by the project.
- **Dockerfile** : File needed by docker to create an image for this project.
- **main.py** : Main Python file to run the project (using _python main.py_)
- **zoo_simulation** : Directory with all Python files to manage zoo simulation
- **tests** : Directory with all Python test files

## Launching Unit tests / Flake8 / Type hint checking

```
make
```

## Launching simulation

For information, this project was tested with Python 3.10.12 on Ubuntu 22.04.5 (Jammy Jellyfish)

```
python main.py
```

## Simulation Usage

When script is launched, user needs to enter commands to initialize paddock. When initilization is done, user enter 'q' to finish this step.

Then, user can simulate life is the paddock during X days. Paddock informations will be displayed after each day. Once again, user has to enter 'q' to finish this step



