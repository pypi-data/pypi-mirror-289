# Unical Symbol Count Package

This is a Python package for counting unique symbols in a string and 
processing input from the command line.
The package provides a class to count unique symbols and a command-line 
interface (CLI) to process strings and files.

## Features

- **Unique Symbol Count**: Count the number of unique symbols in a given string.
- **CLI Interface**: Process strings and files from the command line.
- **Error Handling**: Provides suggestions for invalid commands based on Levenshtein distance.


## Installation

Install package with PIP: 

    pip install task-5-rakitin-sergey

Upgrade package to the last version with PIP:

    pip install task-5-rakitin-sergey --upgrade

## How to use

You can use the package as a command on the command line:

    path_to_your_project> python -m task_5_Rakitin_Sergey.collection --string "your string"
    path_to_your_project> python -m task_5_Rakitin_Sergey.collection --file "path\to\file.txt"

Use as a library import and use the package functions in your Python code:

    # Examle:
    from task_5_Rakitin_Sergey import UniqueSymbolCounter

    counter = UniqueSymbolCounter()
    unique_count = counter.count_unique("your_string")
    print(f"Unique symbols: {unique_count}")

## Link to the package

https://pypi.org/project/task-5-Rakitin-Sergey/

