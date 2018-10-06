
from Example import *

if __name__ == "__main__":

    # stock dictionary, key string date, value tuple (shares,price)
    stocks_dict = {
        "10-10-2020": (2, 20.50),
        "10-11-2020": (1, 21.45),
    }

    # instantiate object stock
    stock_holds1 = Useful("GOOG", stocks_dict)

    # second stock dictionary to demonstrate other in add_purchase()
    more_stocks_dict = {
        "10-12-2020": (3, 11.00),
        "10-13-2020": (4, 22.00)
    }

    # one stock dictionary to demonstrate **kwargs in add_purchase()
    one_stock = {"10-14-2020": (1, 10.20)}

    # demonstrate add_purchase()
    stock_holds1.add_purchase(more_stocks_dict, **one_stock)

    # print(example.stocks)

    stock_holds2 = Useful("AMAZ", stocks_dict)
    print(stock_holds2)

    # output the total stock value
    print("total value: ", stock_holds2.compute_value())