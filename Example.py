
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
        value_sum = 0
        for item in list(self.stocks.values()):
            # compute the value of the stocks
            product = item[0] * item[1]
            value_sum += product
            # if the number of share is negative, raise a custom exception
            if item[0] < 0:
                raise ExampleException("ERROR: Invalid number of shares!!")
        return value_sum

    # string method overriding the one from base class
    # outputs a table of stock dictionary and total stock value
    def __str__(self):
        print("Company's Symbol " + self.company_name)
        for date, item in self.stocks.items():
            if item[0] == 1:
                print("On {} {} share is purchased at ${}".format(date, item[0], item[1]))
            elif item[0] > 1:
                print("On {} {} shares are purchased at ${}".format(date, item[0], item[1]))
            else:
                e = ExampleException("!INVALID!")
                print("On {} {} shares are purchased at ${}".format(date, e, item[1]))

        return "------------------------------------------------------"

