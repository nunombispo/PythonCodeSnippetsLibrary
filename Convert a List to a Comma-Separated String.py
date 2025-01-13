def list_to_string(lst):
    return ', '.join(map(str, lst))


# Example usage
data = [1, 2, 3, 4, 5]
print(list_to_string(data))  # Output: "1, 2, 3, 4, 5"

# Why?
# This snippet converts a list of items into a single comma-separated string, a common task when working with
# text-based data or preparing outputs for reports or logs. It’s simple, versatile, and a great demonstration of string
# manipulation.
