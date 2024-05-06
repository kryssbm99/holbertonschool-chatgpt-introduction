#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description:
    Calculate the factorial of a non-negative integer.

    Parameters:
    n (int): The integer for which the factorial is to be computed.

    Returns:
    int: The factorial of the input integer n. The factorial of n is defined
         2 n * (n-1) * (n-2) * ... * 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
f = factorial(int(sys.argv[1]))
print(f)
