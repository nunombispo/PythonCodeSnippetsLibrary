import sys


def get_size(obj):
    size = sys.getsizeof(obj)
    if isinstance(obj, (dict, list, set, tuple)):
        size += sum(map(get_size, obj))
    elif isinstance(obj, dict):
        size += sum(map(get_size, obj.keys()))
        size += sum(map(get_size, obj.values()))
    return size


# Example usage
data = {"name": "Python", "version": 3.11, "features": ["fast", "easy", "popular"]}
print(f"Memory usage: {get_size(data)} bytes")

# Why? This snippet calculates the memory usage of any Python object, including nested structures like lists and
# dictionaries. It’s useful for performance optimization, debugging, and working with large datasets.
