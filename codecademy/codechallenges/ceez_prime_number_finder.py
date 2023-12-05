def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(upper_limit):
    """Find all prime numbers up to a given limit."""
    return [n for n in range(2, upper_limit + 1) if is_prime(n)]

def main():
    while True:
        try:
            number = int(input("Enter a number (up to 50,000): "))
            if number > 50000:
                print("Please keep the number under 50,000.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    primes = find_primes(number)
    print(f"Prime numbers from 1 to {number}: {primes}")

if __name__ == "__main__":
    main()
