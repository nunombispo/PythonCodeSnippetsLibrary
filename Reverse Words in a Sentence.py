def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])


# Example usage
text = "Hello World from Python"
print(reverse_words(text))  # Output: "Python from World Hello"

# Why?
# This snippet reverses the order of words in a sentence, making it useful for text processing tasks.
# It demonstrates string manipulation, splitting, and joining, which are essential Python skill
