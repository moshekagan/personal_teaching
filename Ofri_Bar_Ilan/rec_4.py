def charecter_stats(s):
    count_letters = 0
    count_numbers = 0
    count_chars = 0

    if len(s) == 0:
        return count_letters, count_numbers, count_chars

    if s[0].isalpha():
        count_letters += 1
    elif s[0].isdigit():
        count_numbers += 1
    else:
        count_chars += 1

    c_letters, c_nums, c_chars = charecter_stats(s[1:])

    count_letters += c_letters
    count_numbers += c_nums
    count_chars += c_chars

    return count_letters, count_numbers, count_chars


print(charecter_stats(""))   # 0 0 0
print(charecter_stats("1"))  # 0 1 0
print(charecter_stats("12"))  # 0 2 0
print(charecter_stats("123"))  # 0 3 0
print(charecter_stats("abc"))  # 3 0 0
print(charecter_stats("!@#"))  # 0 0 3
print(charecter_stats("1!a@2b#3e"))  # 3 3 3
