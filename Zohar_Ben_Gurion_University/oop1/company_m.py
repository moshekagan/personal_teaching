def is_name_valid(name):
    if not isinstance(name, str):
        return False

    if len(name) < 2:
        return False

    if not name[0].isupper():
        return False

    split_name = name.split(" ")
    for n in split_name:
        if len(n) < 2 or not n.isalpha():
            return False

    return True


def is_valid_stock_num(stocks_num):
    return isinstance(stocks_num, int) or stocks_num < 0


class Company:
    # you can add methods for your usage

    def __init__(self, name, stocks_num, stock_price, comp_type):
        if not is_name_valid(name):
            raise ValueError('The name does not fit the criteria')
        if not is_valid_stock_num(stocks_num):
            raise ValueError('The stocks_num does not fit the criteria')
        if not ((isinstance(stock_price, int) or isinstance(stock_price, float)) or stock_price < 0):
            raise ValueError('The stocks_price does not fit the criteria')
        if not is_name_valid(comp_type):
            raise ValueError('The comp_type does not fit the criteria')
        else:
            self.name = name
            self.stock_price = stock_price
            self.stock_num = stocks_num
            self.comp_type = comp_type

    # write here your answer

    def net_worth(self):
        return self.stock_price * self.stock_num

    def set_name(self, name):
        if not is_name_valid(name):
            return False

        self.name = name
        return True

#     def set_stocks_num(self, stocks_num):
#
#     # write here your answer
#
#     def set_stock_price(self, stock_price):
#
#     # write here your answer
#
#     def set_comp_type(self, comp_type):
#
#     # write here your answer
#
#     def update_net_worth(self, net_worth):
#
#     # write here your answer
#
#     def add_stocks(self, number):
#
#     # write here your answer
#
    def __repr__(self):
        return f"{self.name}, {self.stock_num} stocks, Price {self.stock_price}, {self.comp_type}, {self.net_worth()}"
#
#     def __lt__(self, other):
#
#     # write here your answer
#
#     def __gt__(self, other):
#
#     # write here your answer
#
    def __eq__(self, other):
        return self.net_worth() == other.net_worth()

    def __add__(self, other):
        stocks_num = self.stock_num + other.stock_num
        stock_price = (self.net_worth() + other.net_worth()) / stocks_num
        new_comp = Company(self.name, stocks_num, stock_price, self.comp_type)
        return new_comp
