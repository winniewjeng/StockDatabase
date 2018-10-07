#! /usr/bin/env python3
"""
File: Jeng_Winnie_Lab1.py

Author: Winnie Wei Jeng
Assignment: Lab 1
Professor: Phil Tracton
Date: 10/07/2018

This driver file demonstrates the various different methods inside the Example class

"""


from Example import *

if __name__ == "__main__":

    # stock dictionary, key string date, value tuple (shares,price)
    stocks_dict = {
        "10-10-2020": (2, 20.50),
        "10-11-2020": (1, 21.45),
    }

    # second stock dictionary to demonstrate other in add_purchase()
    more_stocks_dict = {
        "10-12-2020": (3, 11.00),
        "10-13-2020": (4, 22.00)
    }

    # one stock dictionary to demonstrate **kwargs in add_purchase()
    one_stock = {"10-14-2020": (1, 10.20)}

    stock_holds = Useful("AMAZ", stocks_dict)

    # demonstrate add_purchase()
    stock_holds.add_purchase(more_stocks_dict, **one_stock)

    print(stock_holds)

    # total value of the stocks is assigned to a float variable called value
    value = stock_holds.compute_value()

    # output the total stock value, rounding to 2 decimal places
    print("total value: ", round(value, 2))
