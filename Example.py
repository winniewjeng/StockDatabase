
from ExampleException import *


# Base Class
class ExampleBase:

    # constructor takes care of instantiating member variables of the class
    def __init__(self, my_company_name, my_stocks_dict, **kwargs):
        self.company_name = my_company_name
        self.stocks = my_stocks_dict

    # string method prints the company's name
    def __str__(self):
        return self.company_name

    # this fxn expands stock purchases by adding more entries to the dictionary
    def add_purchase(self, other, **kwargs):
        self.stocks.update(other, **kwargs)
        return


# Derived Class
class Useful(ExampleBase):

    # constructor calls base class' constructor
    def __init__(self, my_company_name, my_stocks_dict, **kwargs):
        ExampleBase.__init__(self, my_company_name, my_stocks_dict, **kwargs)

    # go through the self.stocks dictionary and calculate total value
    # as summation of shared purchase values multiplied by stock price
    def compute_value(self):
        # initializes value of the total stock value to 0
        sum = 0
        # turn the dictionary's tuple into list in order to perform arithmetic
        # then traverse through the dictionary's tuples
        for tuple_values in list(self.stocks.values()):
            product = 1
            # traverse through the values inside tuples
            for element in tuple_values:
                # calculate the value of each stock as the product of share times price
                product = product * element
            # sum up each term of the stock tuple
            sum += product
        return sum

    # string method overriding the one from base class
    # outputs a table of stock dictionary and total stock value
    def __str__(self):
        for numbers, price in self.stocks.items():
            print("On", numbers, price[0], "stocks are purchased at $", price[1])

        return "Company's Symbol " + self.company_name


# # Main --commented out and chucked into lab2_classes.py
# if __name__ == "__main__":
#     # stock dictionary, key string date, value tuple (shares,price)
#     stocks_dict = {
#         "10-10-2020": (2, 2),
#         "10-11-2020": (1, 2),
#     }
#
#     # instantiate object stock
#     example = ExampleBase("GOOG", stocks_dict)
#
#     # output
#     print(example.stocks)
#
#     # second stock dictionary to demonstrate other in add_purchase()
#     more_stocks_dict = {
#         "10-12-2020": (3, 2),
#         "10-13-2020": (4, 2)
#     }
#
#     # one stock dictionary to demonstrate **kwargs in add_purchase()
#     one_stock = {"10-14-2020": (5, 2)}
#
#     # demonstrate add_purchase()
#     example.add_purchase(more_stocks_dict, **one_stock)
#     print(example.stocks)
#
#     calc = Useful("AMAZ", stocks_dict)
#
#     # output the total stock value
#     print(calc.compute_value())
#
#     print(calc)
