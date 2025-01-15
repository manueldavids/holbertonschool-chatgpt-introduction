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
    try:
        # Convert input to integer
        num = int(sys.argv[1])
        if num < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            f = factorial(num)
            print(f)
    except IndexError:
        print("Error: Please provide a number as a command-line argument.")
    except ValueError:
        print("Error: Please provide a valid integer.")

