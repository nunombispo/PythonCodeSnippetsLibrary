def remove_duplicates(lst):
    return list(set(lst))


# Example usage
data = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(data))  # Output: [1, 2, 3, 4, 5]

# Why?
# This snippet removes duplicate elements from a list by converting it into a set and then back to a list.
# It's a quick and efficient way to handle redundancy in data and is useful in data preprocessing tasks.
