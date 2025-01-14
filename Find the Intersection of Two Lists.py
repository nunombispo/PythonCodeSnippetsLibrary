def list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


# Example usage
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(list_intersection(list1, list2))  # Output: [3, 4]

# Why?
# This snippet finds the common elements between two lists using set operations, making it efficient and easy to
# understand. It’s particularly useful for data comparison tasks or filtering overlapping data.
