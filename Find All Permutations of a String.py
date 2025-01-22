from itertools import permutations


def string_permutations(s):
    return [''.join(p) for p in permutations(s)]


# Example usage
result = string_permutations("abc")
print(result)  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# Why?
# This snippet generates all possible permutations of a string using Python’s itertools.permutations.
# It’s useful for solving combinatorial problems, testing cases, or understanding fundamental algorithm concepts.
