
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
        # then traverse through the dictionary's tuples.
        # items[0] is _number_of_shares and item[1] is _price inside the tuple
        for items in list(self.stocks.values()):
            # if _number_of_shares is negative, raise Exception
            try:
                product = items[0] * items[1]
                if items[0] < 0:
                    raise ExampleException("Invalid number of shares!")
            except ExampleException as error:
                print(error.message)
            # sum up each term of the stock tuple
            sum += product
        return sum

    # string method overriding the one from base class
    # outputs a table of stock dictionary and total stock value
    def __str__(self):
        for numbers_of_shares, price in self.stocks.items():
            print("On", numbers_of_shares, price[0], "stocks are purchased at $", price[1])

        return "Company's Symbol " + self.company_name
