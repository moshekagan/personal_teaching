# def filter_teens(a=13, b=13, c=13):
#     a = fix_age(a)
#     b = fix_age(b)
#     c = fix_age(c)
#
#     return a + b + c
#
#
# def fix_age(age):
#     if 13 <= age <= 19 and not (age == 15 or age == 16):
#         age = 0
#
#     return age
#
#
# print(filter_teens())
# print(filter_teens(1, 2, 3))
# print(filter_teens(1, 15, 14))


m = [[1,2,3],
     [4,5,6],
     [7,8,9]]

for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end="")
    print()
