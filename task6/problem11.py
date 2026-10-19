# String Formatting
# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(n):
    width = len(bin(n)) - 2
    for i in range(1, n + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(decimal.rjust(width), octal.rjust(width), hexadecimal.rjust(width), binary.rjust(width))