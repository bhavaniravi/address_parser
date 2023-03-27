import re
import json
import sys

def split_by_character(address):
    """Split address by parts based on `split_by`

    Args:
        address (str): Address to be parsed
        split_by (str): The delimiter to split by

    Returns:
        (dict): Parsed address with street and housenumber
    """
    words = address.split()
    housenumber = ""
    street = ""
    i = 0

    while i < len(words) and not any(char.isdigit() for char in words[i]):
        i += 1

    street = " ".join(words[:i])
    housenumber = " ".join(words[i:])
    housenumber = housenumber.replace(",", "")
    return {"street": street.strip(), "housenumber": housenumber.strip()}


def split_and_parse(address, split_by):
    """Split address by parts based on `split_by`

    Args:
        address (str): Address to be parsed
        split_by (str): The delimiter to split by

    Returns:
        (dict): Parsed address with street and housenumber
    """
    parts = address.split(split_by)
    for i, part in enumerate(parts):
        part = part.strip()
        if part.strip().isdigit():
            if i < 1:
                return {
                    "housenumber": part,
                    "street": (" ".join(parts[i + 1 :]).strip()),
                }
            else:
                return {
                    "housenumber": (" ".join(parts[i:]).strip()),
                    "street": (" ".join(parts[:i]).strip()),
                }


def parse_address(address):

    if "," in address:
        response = split_and_parse(address, ",")
    elif "No" in address:
        response = split_and_parse(address, "No")
    else:
        response = split_and_parse(address, " ")

    if response:
        return response
    else:
        return split_by_character(address)


if __name__ == "__main__":
    # Test the program
    # addresses = [
    #     "Winterallee 3",
    #     "Musterstrasse 45",
    #     "Blaufeldweg 123B",
    #     "Am Bächle 23",
    #     "Auf der Vogelwiese 23 b",
    #     "4, rue de la revolution",
    #     "200 Broadway Av",
    #     "Calle Aduana, 29",
    #     "Calle 39 No 1540",
    # ]

    # for address in addresses:
    #     parsed = parse_address(address)
    #     print(address, "\n", parsed, "\n")
    try:
        parsed = parse_address(sys.argv[1])
        print(parsed)
    except IndexError:
        print("Empty address passed")
