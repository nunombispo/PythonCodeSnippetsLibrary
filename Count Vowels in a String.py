def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


# Example usage
text = "Hello World from Python"
print(count_vowels(text))  # Output: 5

# Why?
# This snippet efficiently counts the number of vowels in a string using a generator expression.
# It’s a simple yet practical example for learning loops, conditionals, and string operations.
