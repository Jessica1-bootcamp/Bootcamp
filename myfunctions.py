import numpy as np
import math

# asking the user for a large integer
def get_large_integer():
    """
    Prompts the user to input a large integer.

    Returns:
    int: The large integer input by the user.
    """
    while True:
        try:
            num = int(input("Please enter a large integer: "))
            return num
        except ValueError:
            print("That's not a valid integer. Please try again.")

# Function to check if a number is prime and print the result
def is_prime(n):
    """
    Checks if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# if not a prime, print what the largest prime factor is
def largest_prime_factor(n):
    """
    Finds the largest prime factor of a number.

    Parameters:
    n (int): The number to find the largest prime factor of.

    Returns:
    int: The largest prime factor of n.
    """
    if n <= 1:
        return None
    largest = None
    for i in range(2, int(np.sqrt(n)) + 1):
        while n % i == 0:
            largest = i
            n //= i
    if n > 1:
        largest = n
    return largest


