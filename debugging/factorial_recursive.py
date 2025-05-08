#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    # Check if a command-line argument is given
    if len(sys.argv) != 2:
        print("Usage: ./factorial_recursive.py <non-negative integer>")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Error: Please enter a non-negative integer.")
            sys.exit(1)
        result = factorial(num)
        print(f"Factorial of {num} is: {result}")
    except ValueError:
        print("Error: Input must be an integer.")
        sys.exit(1)

