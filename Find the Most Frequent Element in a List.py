from collections import Counter


def most_frequent(lst):
    return Counter(lst).most_common(1)[0][0]


# Example usage
data = [1, 3, 2, 3, 4, 3, 5]
print(most_frequent(data))  # Output: 3


# Why?
# This snippet solves a common problem in data processing—finding the mode of a dataset.
# It uses Python's collections.Counter for efficiency and readability.
