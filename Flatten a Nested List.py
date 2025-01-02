def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


# Example usage
data = [1, [2, [3, 4]], 5]
print(flatten_list(data))  # Output: [1, 2, 3, 4, 5]


# Why?
# Working with nested data structures is common, and this recursive function elegantly flattens any nested list,
# making it more manageable for further processing
