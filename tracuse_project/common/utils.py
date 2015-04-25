

def camel_to_underscore(camel_string):

    output = ""

    if camel_string:
        for letter in camel_string:
            if letter.isupper():
                output += "_" + letter.lower()
            else:
                output += letter

        output = output.replace(" ", "")

        if output[0] == "_":
            output = output[1:]

    return output

# tests = ["First Name", "FirstName", "firstName", "First", "firstname"]
#
# for test in tests:
#     result = camel_to_underscore(test)
#     print("{} --> {}".format(test, result))