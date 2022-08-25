def remove_vowels(s):
    res = ""

    for i in range(len(s)):
        if s[i].lower() not in ["a", "e", "i", "o", "u"]:
            res += s[i]

    return res


print(remove_vowels("Israel Elections 2022."))