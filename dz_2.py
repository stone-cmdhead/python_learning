test_strings = ["kawabunga", "metro2013", "moon", "orange"]


def shwalengthimeter(test_strings):
    result_strings = []

    for string in test_strings:
        result_string = string[1:]

        if result_string[0] in ["a", "e", "o", "i", "u", "y"]:
            result_string = result_string[1:]

        result_string = "shwa" + result_string
        result_string = result_string + " "
        result_string = result_string + str(len(string))

        result_strings.append(result_string)

    return result_strings


print(shwalengthimeter(test_strings))
