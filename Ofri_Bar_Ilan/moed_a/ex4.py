def gematria(word):
    if len(word) == 0:
        return 0

    s = gematria(word[1:])

    a = word[0].lower()
    if 'a' <= a <= 'z':
        s += ord(a) - ord('a') + 1

    return s


print(gematria("ABBA!"))