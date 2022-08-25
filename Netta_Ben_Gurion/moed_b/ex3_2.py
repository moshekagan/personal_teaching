def count_max_bottle(money, price, recy):
    total = 0
    have_bottles = int(money / price)
    total += have_bottles

    while have_bottles >= recy:
        recy_bottles = int(have_bottles / recy)
        rest_bottles = int(have_bottles % recy)
        total += recy_bottles
        have_bottles = recy_bottles + rest_bottles

    return total


if __name__ == '__main__':
    print(count_max_bottle(15, 1, 2))  # 26
    print(count_max_bottle(15, 1, 3))
    print(count_max_bottle(16, 2, 2))
    print(count_max_bottle(16, 2, 3))