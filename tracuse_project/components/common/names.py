"""String Manipulation Utilities for Naming Entities"""

from string import capwords


def camel_to_spaced_lower(camel_string):
    output = ""

    if camel_string:
        for letter in camel_string:
            prior_letter = camel_string[camel_string.index(letter) - 1]
            if letter.isupper() and prior_letter is not " ":
                output += " " + letter.lower()
            else:
                output += letter.lower()

        if output[0] == " ":
            output = output[1:]

    return output


def camel_to_spaced_capital(camel_string):
    output = ""

    common_string = camel_to_spaced_lower(camel_string)

    output = capwords(common_string, " ")

    return output


def camel_to_underscore(camel_string):
    output = ""

    common_string = camel_to_spaced_lower(camel_string)

    output = common_string.replace(" ", "_")

    return output