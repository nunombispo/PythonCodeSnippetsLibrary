def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:  # Prime numbers are greater than 1
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes


# Example usage
print(find_primes(10, 50))  # Output: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# Why?
# This snippet efficiently finds prime numbers within a given range, leveraging mathematical properties for
# optimization. It's great for teaching loops, conditional logic, and number theory basics.
