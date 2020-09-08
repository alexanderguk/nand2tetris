import re


def parse(line):
    splitResult = re.split("//|\n", line)
    element = splitResult[0].replace(" ", "")

    if (len(element) == 0):
        return

    fields = re.split("=|;", element)

    return fields
