#!/usr/bin/python3
# 1-number_of_lines.py
# Aliyu haruna <harunaaliyu6449@gmail.com>
"""Defines a text file line-counting function."""


def number_of_lines(filename=""):
    """Return the number of lines in a text file."""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
<<<<<<< HEAD

=======
>>>>>>> 5bb7c6617563c4ce144c7932f7bc2d580523c2d5
