# class Bank:
#     def __init__(self, amount=0):
#         self.amount = amount
#
#     def deposit(self, amount):
#         self.amount += amount
#
#
# b = Bank()
# b.deposit(1000)
#
# b2 = Bank(1000)
# b2.deposit(1000)  # 2000
#
#
#
#
#
# class Wallet:
#     def __init__(self):
#         self._5_cent = 0
#         self._10_cent = 0
#
#
# w = Wallet()
#
# # w2 = Wallet(10, 3)
#
#
#
#


class A:
    amount = {1: 0, 5: 1, 10: 3, 25: 0, 50: 0}

    def __repr__(self):
        res = []
        for c, a in sorted(self.amount.items(), key=lambda x: x[0]):
            if a > 0:
                res.append(str(c) + "x" + str(a))

        return ",".join(res)

    def value(self):
        v = 0
        for c, a in self.amount.items():
            v += (a * c/100)

        return v


a = A()
print(a.value())
