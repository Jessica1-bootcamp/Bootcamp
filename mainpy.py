# main script for the prime functions
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