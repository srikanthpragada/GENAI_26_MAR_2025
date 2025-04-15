# Function to take a number and return true if it is prime
def is_prime(num):
    """
    Check if a number is prime.
    A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
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

