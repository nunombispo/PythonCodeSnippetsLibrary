from collections import Counter


def max_occurring_char(s):
    count = Counter(s)
    return max(count, key=count.get)


# Example usage
text = "hello world"
print(max_occurring_char(text))  # Output: "l"

# Why?
# This snippet identifies the character that appears most frequently in a string, using Python's collections.Counter.
# It's great for text analysis and showcases how to handle frequency counts efficiently.
