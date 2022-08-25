def sum_of_non_negative_recursive(l):
    if len(l) == 0:
        return 0

    s = sum_of_non_negative_recursive(l[1:])

    if l[0] > 0:
        s += l[0]

    return s


print(sum_of_non_negative_recursive([]))
print(sum_of_non_negative_recursive([0, 1, -2, 3, -4, 5]))
