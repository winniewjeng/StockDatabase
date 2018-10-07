
from Example import *
from ExampleException import *
import sys, traceback

if __name__ == "__main__":

    """Some Stocks Dictionaries"""
    # ========================================================================== #

    stocks_dict = {"10-10-2020": (2, 20.50), "10-11-2020": (1, 21.45)}

    more_stocks_dict = {"10-12-2020": (3, 11.00), "10-13-2020": (4, 22.00)}

    one_more_stock_dict = {"10-14-2020": (1, 10.20)}

    valid_stock_dict = {"10-15-2020": (1, 0.38)}

    invalid_stock_dict = {"10-16-2020": (-4, 0.85), "10-17-2020": (7, 0.55)}

    # ========================================================================== #

    # instantiate object
    stock_hold_1 = Useful("AMAZ", stocks_dict)

    stock_hold_1.add_purchase(more_stocks_dict, **one_more_stock_dict)

    # total value of the stocks is assigned to a float variable called value
    value = stock_hold_1.compute_value()

    print(stock_hold_1)

    # output the total stock value
    print("total value: ", round(value, 2))

    print()

    # create an invalid_stock_dict where the number of share is negative

    stock_hold_2 = Useful("TSLA", valid_stock_dict)
    stock_hold_2.add_purchase(invalid_stock_dict)

    try:
        val = stock_hold_2.compute_value()
        print(stock_hold_2)
        print("total value: ", round(val, 2))
    except ExampleException as e:
        print(stock_hold_2)
        print(repr(e.message))
