# Function to take a number and return true if it is prime
def is_prime(num):

    """
    Parameters:
        num (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
    """
   
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num**0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def is_perfect(num):
    """
    Check if a number is perfect.
    A perfect number is a positive integer that is equal to the sum of its proper positive divisors, excluding the number itself.
    """
    if num < 2:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

