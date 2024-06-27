

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(limit):
    """Find all prime numbers up to a given limit."""
    prime_numbers = []
    for number in range(2, limit + 1):
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers

if __name__ == "__main__":
    limit = 100  # Example: calculate prime numbers up to 100
    primes = find_primes(limit)
    print(f"Prime numbers up to {limit}: {primes}")
