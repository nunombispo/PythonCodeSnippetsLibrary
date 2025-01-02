def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}


# Example usage
a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print(merge_dicts(a, b))  # Output: {'x': 1, 'y': 3, 'z': 4}


# Why?
# Merging dictionaries is a frequent task, and this snippet highlights the modern and concise way to merge them
# using dictionary unpacking (Python 3.5+).
