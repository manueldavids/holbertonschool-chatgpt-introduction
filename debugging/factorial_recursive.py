#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    Parameters:
    n (int): The number for which the factorial is calculated. Must be a non-negative integer.

    Returns:
    int: The factorial of the input number. If n is 0, returns 1 as 0! is defined as 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    # Calculate the factorial of the number passed as a command-line argument
    f = factorial(int(sys.argv[1]))
    print(f)

