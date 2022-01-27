def is_anagram(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    anagram = all(str_2.lower().count(x) == str_1.lower().count(x) for x in str_1)
    return (anagram)


print(is_anagram("AAABB", "AABBB"))