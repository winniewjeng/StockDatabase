#! /usr/bin/env python3
"""
File: Jeng_Winnie_Lab1.py

Author: Winnie Wei Jeng
Assignment: Lab 2
Professor: Phil Tracton
Date: 10/07/2018

This driver file tests the different methods inside the Example class
It uses the custom exception class, ExampleException, to handle errors
And it imports sys and traceback to output the error type and error location

"""

from Example import *
from ExampleException import *
import sys
import traceback

if __name__ == "__main__":

    """Some Stocks Dictionaries"""
    # ========================================================================== #

    stocks_dict = {"10-10-2020": (2, 20.50), "10-11-2020": (1, 21.45)}

    more_stocks_dict = {"10-12-2020": (3, 11.00), "10-13-2020": (4, 22.00)}

    one_more_stock_dict = {"10-14-2020": (1, 10.20)}

    valid_stock_dict = {"10-15-2020": (1, 0.38)}

    invalid_stock_dict = {"10-16-2020": (-4, 0.85), "10-17-2020": (7, 0.55)}

    more_valid_stock_dict = {"10-18-2020": (12, 10.58), "10-19-2020": (20, 11.00)}

    # ========================================================================== #

    """Testing Example Class by instantiating some objects and calling some functions"""

    # instantiate an object named AMAZ that has a stock dictionary
    stock_hold_1 = Useful("AMAZ", stocks_dict)

    # calling add_purchase method to expand the object's stock dictionary
    stock_hold_1.add_purchase(more_stocks_dict, **one_more_stock_dict)

    # call compute_value method to compute the total values of stocks in object's dictionary
    value_1 = stock_hold_1.compute_value()

    # print the object by implicitly calling the string method
    print(stock_hold_1)

    # output the total stock of the stock
    print("total value: $", round(value_1, 2))

    print()

    # create an object named TSLA
    stock_hold_2 = Useful("TSLA", valid_stock_dict)

    # call add_purchase function and pass in a dictionary with invalid number of shares
    stock_hold_2.add_purchase(invalid_stock_dict)

    # Apply custom exception handler to prevent program from crashing with invalid data
    try:
        value_2 = stock_hold_2.compute_value()
        print(stock_hold_2)
        print("total value: $", round(value_2, 2))
    except ExampleException as e:
        # prints the object dictionary as usual
        print(stock_hold_2)
        # outputs the error message
        print(repr(e.message))
        # sys outputs the nature of error--the error is an ExampleException
        print(sys.exc_info()[0])
        # traceback outputs the error location
        print("\nCall traceback:")
        print(traceback.format_exc())

    print()

    # End this program on a good note with a working object that does not throw exception
    stock_hold_3 = Useful("NVDA", more_valid_stock_dict)
    try:
        value_3 = stock_hold_3.compute_value()
        print(stock_hold_3)
        print("total value: $", round(value_3, 2))
    except ExampleException as e:
        print(stock_hold_3)
        print(repr(e.message))
        print(sys.exc_info()[0])
        print("Call traceback:")
        print(traceback.format_exc())

    print()
