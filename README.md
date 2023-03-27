# Address Parser 

A simple program to extract the street name and street number from an input address string.

## Description

The Address Parser is a Python program that extracts the street name and street number from an input address string and returns them as a JSON object. The program can handle various formats of address strings, including those from different countries.

## Installation

This program requires Python 3.6 or later. To install the program and its dependencies, use the following commands:

bashCopy code

```
pip install poetry
git clone https://github.com/<username>/<repository-name>.git
cd <repository-name>
poetry install
```

## Usage

To use the program, run the following command:

bashCopy code

`poetry run python address_parser.py "input_address_string"`

Replace "input_address_string" with the address you want to parse. The program will output the parsed address as a JSON object.

## Testing

To run the unit tests for this program, use the following command:

bashCopy code

`poetry run pytest`

This will run all the tests in the `tests/` directory and output the results to the console.

## Contributing

If you find a bug or have a suggestion for this program, please open an issue or submit a pull request on the GitHub repository.

## License

This program is licensed under the MIT License. See the `LICENSE` file for more information.
