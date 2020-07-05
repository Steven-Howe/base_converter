# base_converter
Program to convert numbers between binary, octal, decimal, and hexadecimal.

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
