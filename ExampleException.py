#! /usr/bin/env python3
"""
File: Jeng_Winnie_Lab1.py

Author: Winnie Wei Jeng
Assignment: Lab 1
Professor: Phil Tracton
Date: 9/30/2018

This custom exception class outputs itself in an error message

"""

# ExampleException class inherits from the Exception class and has an error message


class ExampleException(Exception):

    def __init__(self, message=" "):
        self.message = message

    def __str__(self):
        return self.message


