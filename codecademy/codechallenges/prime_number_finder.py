def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_finder(n):
    """Return a list of prime numbers from 1 to n (inclusive)."""
    return [num for num in range(2, n + 1) if is_prime(num)]

# Example usage:
print(prime_finder(11))  # This should return [2, 3, 5, 7, 11]
