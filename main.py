# main script for the prime functions
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from myfunctions import get_large_integer, is_prime, largest_prime_factor
def main():
    # Get a large integer from the user
    num = get_large_integer()
    
    # Check if the number is prime
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        largest_factor = largest_prime_factor(num)
        print(f"{num} is not a prime number. The largest prime factor is {largest_factor}.")

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from PrimalityTest import is_prime

def get_large_integer():
    while True:
        try:
            num = int(input("Enter a large integer: "))
            return num
        except ValueError:
            print("That's not a valid integer. Please try again.")

def main():
    num = get_large_integer()

    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

if __name__ == "__main__":
    main()