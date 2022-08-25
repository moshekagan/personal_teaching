# 14 16 ....
# 1 2 3 4 5 6 7  8  9  10 ... (n)


def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    res1 = fibo(n - 1)
    res2 = fibo(n - 2)

    return res1 + res2


print(fibo(1))  # 1
print(fibo(2))  # 1
print(fibo(3))  # 2
print(fibo(6))  # 8
print(fibo(10))  # f9 + f8


def ofrinatzi(n, n1=1, n2=1):
    if n == 1:
        return n1
    if n == 2:
        return n2

    return ofrinatzi(n-1, n1, n2) + ofrinatzi(n-2, n1, n2)


print(ofrinatzi(1, 13, 7))  # 1
print(ofrinatzi(2, 13, 7))  # 1
print(ofrinatzi(3, 13, 7))  # 2
print(ofrinatzi(6, 13, 7))  # 8
print(ofrinatzi(10, 13, 7))  # f9 + f8