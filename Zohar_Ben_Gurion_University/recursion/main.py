def one_except_identity_helper(str1, str2, count):
    if count > 1:
        return False

    if len(str1) == 0 or len(str2) == 0:
        return count == 1

    if str1[0] != str2[0]:
        return one_except_identity_helper(str1[1:], str2[1:], count+1)
    else:
        return one_except_identity_helper(str1[1:], str2[1:], count)


def one_except_identity(str1, str2):
    return one_except_identity_helper(str1, str2, 0)


def ordered_subset(str1, str2):
    if len(str2) == 0:
        return True

    if len(str1) == 0:
        return False

    if str1[0] == str2[0]:
        if len(str1) > 1 and len(str2) > 1 and str1[1] == str2[1]:
            return False
        else:
            return ordered_subset(str1[1:], str2[1:])

    return ordered_subset(str1[1:], str2)


def subsets_size_k_helper(super_set, k, idx, current, res):
    if len(current) == k:
        res.append(current)
        return

    for i in range(idx, len(super_set)):
        x = super_set[i]
        current.append(x)
        subsets_size_k_helper(super_set, k, i+1, current, res)
        current = current[:-1]


def subsets_size_k(n, k):
    super_set = list(range(1, n+1))
    res = []
    subsets_size_k_helper(super_set, k, 0, [], res)
    print(res)


def linear_sum(x, result):
    if len(x) == 0:
        return result == 0

    current = x[-1]

    res1 = linear_sum(x[:-1], result - current)
    res2 = linear_sum(x[:-1], result + current)
    res3 = linear_sum(x[:-1], result)

    return res1 or res2 or res3


if __name__ == '__main__':
    print(one_except_identity("001", "011"))  # True
    print(one_except_identity("011", "011"))  # False
    print(one_except_identity("011", "0110"))  # False
    print()

    print(ordered_subset("ladbcfe", "abc"))  # False
    print(ordered_subset("ladbxcfe", "abc"))  # True
    print(ordered_subset("ladbxcfe", ""))  # True
    print(ordered_subset("ladbxcfe", "a"))  # True
    print(ordered_subset("e", "a"))  # False
    print()

    # print(subsets_size_k(5, 3)) # [‘123’, ‘124’, ‘125’, ‘134’, ‘135’, ‘145’, ‘234’, ‘235’, ‘245’, ‘345’]
    # print(subsets_size_k(5, 0))  # [‘’]
    # print()

    print(linear_sum([2, 3, 6, 7, 10], 15))
    print(linear_sum([5, 14, 7, 3], 20))