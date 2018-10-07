
from Example import *
from ExampleException import *
import sys, traceback

if __name__ == "__main__":

    # stock dictionary, key string date, value tuple (shares,price)
    stocks_dict = {
        "10-10-2020": (2, 20.50),
        "10-11-2020": (1, 21.45),
    }

    # instantiate object stock GOOG
    stock_hold1 = Useful("GOOG", stocks_dict)

    # more_stock_dict to demonstrate input argument other in add_purchase()
    more_stocks_dict = {
        "10-12-2020": (3, 11.00),
        "10-13-2020": (4, 22.00)
    }

    # one_stock dict to demonstrate input argument **kwargs in add_purchase()
    one_more_stock_dict = {"10-14-2020": (1, 10.20)}

    # demonstrate add_purchase()
    stock_hold1.add_purchase(more_stocks_dict, **one_more_stock_dict)

    # print(example.stocks)

    stock_hold2 = Useful("AMAZ", stocks_dict)
    print(stock_hold2)

    # total value of the stocks is assigned to a float variable called value
    value = stock_hold2.compute_value()

    # output the total stock value
    print("total value: ", round(value, 2))

    print()

    # create an invalid_stock_dict where the number of share is negative
    valid_stock_dict = {"10-14-2020": (-1, 0.38)}
    invalid_stock_dict = {"10-15-2020": (-4, 0.85),
                          "10-16-2020": (-7, 0.55),
                          "10-17-2020": (-3, 0.15)}
    stock_hold3 = Useful("TSLA", valid_stock_dict)

    try:
        # add the invalid_stock_dict to the constructor's dictionary self.stocks
        stock_hold3.add_purchase(invalid_stock_dict)
    except ExampleException as e:
        # print(e.message)
        print("hihihhihihihihi")
        print(repr(e.message))

    print(stock_hold3)
    val = stock_hold3.compute_value()
    print("total value: ", round(val, 2))
