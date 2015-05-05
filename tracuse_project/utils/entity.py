"""Functions for Naming and Sorting Entities"""

from string import capwords


def camel_to_spaced_lower(camel_string):
    """Example:
        CamelCase -> camel case
    """
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
    """Example:
        CamelCase -> Camel Case
    """
    common_string = camel_to_spaced_lower(camel_string)

    output = capwords(common_string, " ")

    return output


def camel_to_underscore(camel_string):
    """Example:
        CamelCase -> camel_case
    """
    common_string = camel_to_spaced_lower(camel_string)

    output = common_string.replace(" ", "_")

    return output


def sort_range_value(sort_prefix, sort_base_length=0, return_start=True):
    """Return sort range value based on sort prefix
    Used in last_sorted_value to search in sequence

    Arguments:
        sort_prefix (string):
        sort_base_length (integer):
        return_start (boolean, default=True):
            True - return starting value
            False - return ending value

    Return:
        sort value (integer)
    """
    if return_start:
        fill_character = "0"
    else:
        fill_character = "9"
    total_length = len(sort_prefix) + sort_base_length
    sort_string = sort_prefix.ljust(total_length, fill_character)
    return int(sort_string)