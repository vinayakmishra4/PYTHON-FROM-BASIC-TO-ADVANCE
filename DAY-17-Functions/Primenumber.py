def find_primes(start, end):
    """Returns a list of prime numbers between start and end (inclusive)."""
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

# Example usage
if __name__ == "__main__":
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    prime_numbers = find_primes(start, end)
    print("Prime numbers:", prime_numbers)