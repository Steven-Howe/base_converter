#! /usr/bin/env python3

import sys


def get_args():
    """Gets arguments from commandline"""
    num_type_1 = sys.argv[1]
    # if interactive mode will return placeholders
    if "i" in num_type_1:
        return num_type_1, "number", "num_type_2"

    # if help information will return placeholders
    elif "h" in num_type_1:
        return num_type_1, "number", "num_type_2"
    else:
        number = sys.argv[2]
        num_type_2 = sys.argv[3]

        return num_type_1, number, num_type_2


def check_help(num_type_1):
    """Will check if help flag is set"""
    if "help" in num_type_1:
        return True
    else:
        return False


def help():
    """Prints instructions for running program"""

    print(""""
    Name:
            base_converter.py

    Synopsis:
            python3 base_converter.py 

    Description:
            base_converter.py will convert decimal, binary, hexadecimal, and octal numbers
            interchangeably, either on the commandline or interactively.

            --help
                will display this help page and exit

            -i
                will run the program in interactive mode

            -d
                indicates a decimal number

            -b
                indicates a binary number

            -h
                indicates a hexadecimal number

            -o
                indicates an octal number

            -a
                will return all possible base conversions of a number

    Examples:
            python3 base_converter.py -d 6443 -b
            -will convert the decimal number 6443 into a binary number

            python3 base_converter.py -b 1001101101 -o
            -will convert the binary number 1001101101 into an octal number

            python3 base_converter.py -h 13f68c -a
            -will convert the hexadecimal number 13f68c into binary, octal, and decimal

            python3 base_converter.py -o "645 7221 363" -d
            -will convert the octal numbers 645, 7221, 363 into decimal

            Note: double quotation marks must be used if more than one number
                  is to be converted at a time

            python3 base_converter.py -d "1987 1622 153" -a
            -will convert the decimal numbers 1987, 1622, 153 into binary, octal,
            and hexadecimal 

    Author:
            Written by Steven Howe 

    """)
    exit()


def check_multiple_nums(number):
    """Checks if multiple numbers are given"""
    if " " in number:
        return True
    else:
        return False


def multiple_nums(num_type_1, number, num_type_2):
    """Will convert muliple numbers of the same base"""
    nums_lst = []

    # splits numbers
    number = number.replace("'", "")
    nums_lst = number.split(" ")

    # finds conversion for each number
    for num in nums_lst:
        converter(num_type_1, num, num_type_2)

    else:
        return


def check_interactive(num_type_1):
    """Checks if interactive mode has been set"""
    if "i" in num_type_1:
        return True
    else:
        return False


def interactive():
    """Gets arguments interactively from user if an -i flag is used"""
    num_type_1 = input("What is the type of number you are wishing to convert? \n")
    number = input("What is the number? \n")
    num_type_2 = input("What type of number are you wishing to convert it to? \n")

    return num_type_1, number, num_type_2


def converter(num_type_1, number, num_type_2):
    """Determines desired number conversion based on flags and outputs conversion"""

    num_type_1 = num_type_1.strip("-")
    num_type_2 = num_type_2.strip("-")
    # notifies if bases are the same
    if num_type_1 == num_type_2:
        print("The number is already in that base!")
        exit()

    # decimal to other base conversions
    elif "d" in num_type_1 and "b" in num_type_2:
        # converts decimal to binary
        return output(num_type_2, number, dec2bin(number))

    elif "d" in num_type_1 and "o" in num_type_2:
        # converts decimal to octal
        return output(num_type_2, number, dec2oct(number))

    elif "d" in num_type_1 and "h" in num_type_2:
        # converts decimal to hexadecimal
        return output(num_type_2, number, dec2hex(number))

    # decimal to all base conversion
    elif "d" in num_type_1 and "a" in num_type_2:
        # converts decimal to all other bases
        # must change variable before function call to avoid errors
        num_type_2 = "b"
        output(num_type_2, number, dec2bin(number))

        num_type_2 = "o"
        output(num_type_2, number, dec2oct(number))

        num_type_2 = "h"
        output(num_type_2, number, dec2hex(number))
        return

    # hexadecimal to other base conversions
    elif "h" in num_type_1 and "d" in num_type_2:
        # converts hexdecimal to decimal
        return output(num_type_2, number, hex2dec(number))

    elif "h" in num_type_1 and "b" in num_type_2:
        # converts hexdecimal to binary
        return output(num_type_2, number, hex2bin(number))

    elif "h" in num_type_1 and "o" in num_type_2:
        # converts hexdecimal to octal
        return output(num_type_2, number, hex2oct(number))

    # hexadecimal to all base conversion
    elif "h" in num_type_1 and "a" in num_type_2:
        # converts hexadecimal to all other bases
        # must change variable before function call to avoid errors
        num_type_2 = "b"
        output(num_type_2, number, hex2bin(number))

        num_type_2 = "o"
        output(num_type_2, number, hex2oct(number))

        num_type_2 = "d"
        output(num_type_2, number, hex2dec(number))
        return

    # binary to other base conversions
    elif "b" in num_type_1 and "d" in num_type_2:
        # converts binary to decimal
        return output(num_type_2, number, bin2dec(number))

    elif "b" in num_type_1 and "h" in num_type_2:
        # converts binary to hexadecimal
        return output(num_type_2, number, bin2hex(number))

    elif "b" in num_type_1 and "o" in num_type_2:
        # converts binary to octal
        return output(num_type_2, number, bin2oct(number))

    # binary to all base conversion
    elif "b" in num_type_1 and "a" in num_type_2:
        # converts binary to all other bases
        # must change variable before function call to avoid errors
        num_type_2 = "d"
        output(num_type_2, number, bin2dec(number))

        num_type_2 = "h"
        output(num_type_2, number, bin2hex(number))

        num_type_2 = "o"
        output(num_type_2, number, bin2oct(number))
        return

    # octal to other base conversions
    elif "o" in num_type_1 and "d" in num_type_2:
        # converts octal to decimal
        return output(num_type_2, number, oct2dec(number))

    elif "o" in num_type_1 and "b" in num_type_2:
        # converts octal to binary
        return output(num_type_2, number, oct2bin(number))

    elif "o" in num_type_1 and "h" in num_type_2:
        # converts octal to hexadecimal
        return output(num_type_2, number, oct2hex(number))

    # octal to all base conversion
    elif "o" in num_type_1 and "a" in num_type_2:
        # converts octal to all other bases
        # must change variable before function call to avoid errors
        num_type_2 = "d"
        output(num_type_2, number, oct2dec(number))

        num_type_2 = "b"
        output(num_type_2, number, oct2bin(number))

        num_type_2 = "h"
        output(num_type_2, number, oct2hex(number))
        return

    else:
        print("You must enter a correct flag.")


# Decimal to other bases
def dec2bin(number):
    """Converts a decimal number to a binary number"""
    conversion = bin(int(number))
    conversion = conversion.split("0b")
    return conversion[1]


def dec2oct(number):
    """Converts a decimal number to a octal number"""
    conversion = oct(int(number))
    conversion = conversion.split("0o")
    return conversion[1]


def dec2hex(number):
    """Converts a decimal number to a hexadecimal number"""
    conversion = hex(int(number))
    conversion = conversion.split("0x")
    return conversion[1]


# Hexadecimal to other bases
def hex2dec(number):
    """Converts a hexadecimal number to a decimal number"""
    number = str(number)
    prefix_num = "0x{0}".format(number)
    conversion = int(prefix_num, 0)

    return int(conversion)


def hex2bin(number):
    """Converts a hexadecimal number to a binary number"""
    number = str(number)
    prefix_num = "0x{0}".format(number)
    conversion = bin(int(prefix_num, 16))
    conversion = conversion.replace("0b", "")

    return conversion


def hex2oct(number):
    """Converts a hexadecimal number to a binary number"""
    number = str(number)
    prefix_num = "0x{0}".format(number)
    conversion = oct(int(prefix_num, 16))
    conversion = conversion.replace("0o", "")

    return conversion


# Binary to other bases
def bin2dec(number):
    """Converts a binary number to decimal"""
    number = str(number)
    prefix_num = "0b{0}".format(number)
    conversion = int(prefix_num, 0)

    return int(conversion)


def bin2hex(number):
    """Converts a binary number to hexadecimal"""
    number = str(number)
    prefix_num = "0b{0}".format(number)
    conversion = hex(int(prefix_num, 0))
    conversion = conversion.replace("0x", "")

    return conversion


def bin2oct(number):
    """Converts a binary number to octal"""
    number = str(number)
    prefix_num = "0b{0}".format(number)
    conversion = oct(int(prefix_num, 0))
    conversion = conversion.replace("0o", "")

    return conversion


# Octal to other bases
def oct2dec(number):
    """Converts an octal number to decimal"""
    number = str(number)
    prefix_num = "0o{0}".format(number)
    conversion = int(prefix_num, 0)

    return int(conversion)


def oct2bin(number):
    """Converts an octal number to a binary number"""
    number = str(number)
    prefix_num = "0o{0}".format(number)
    conversion = bin(int(prefix_num, 8))
    conversion = conversion.replace("0b", "")

    return conversion


def oct2hex(number):
    """Converts an octal number to a hexadecimal number"""
    number = str(number)
    prefix_num = "0o{0}".format(number)
    conversion = hex(int(prefix_num, 8))
    conversion = conversion.replace("0x", "")

    return conversion


def output(num_type_2, number, conversion):
    """Shows output of specified number conversion"""
    if num_type_2 == "d":
        print(f"The value of {number} in decimal is: {conversion}")
    elif num_type_2 == "b":
        print(f"The value of {number} in binary is: {conversion}")
    elif num_type_2 == "o":
        print(f"The value of {number} in octal is: {conversion}")
    elif num_type_2 == "h":
        print(f"The value of {number} in hexadecimal is: {conversion}")
    else:
        print("You have entered an incorrect number type to convert to.")


# Test cases for program
def main():
    # Gets arguments from the commandline
    num_type_1, number, num_type_2 = get_args()

    # will run interactive mode if -i flag set
    if check_interactive(num_type_1):
        num_type_1, number, num_type_2 = interactive()

        # if there's multiple numbers in interactive mode will convert them all
        if check_multiple_nums(number):
            multiple_nums(num_type_1, number, num_type_2)
        else:
            converter(num_type_1, number, num_type_2)

    # will run help mode if -h flag set
    elif check_help(num_type_1):
        help()

    # will convert multiple numbers if present
    elif check_multiple_nums(number):
        multiple_nums(num_type_1, number, num_type_2)

    else:
        converter(num_type_1, number, num_type_2)


if __name__ == '__main__':
    main()