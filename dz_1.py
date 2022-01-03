string_1 = "Invert me please"


def method_1(string_1):
    return string_1[::-1]


def method_2(string_1):
    return "".join(reversed(string_1))


def method_3(string_1):
    result = ""
    for char in string_1:
        result = char + result
    return result


print("1->", method_1(string_1))
print("2->", method_2(string_1))
print("3->", method_3(string_1))