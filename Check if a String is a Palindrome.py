def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()  # Remove non-alphanumeric characters and convert to lowercase
    return s == s[::-1]


# Example usage
text = "A man, a plan, a canal: Panama"
print(is_palindrome(text))  # Output: True

#
# Why?
# This snippet efficiently checks whether a string is a palindrome, ignoring spaces, punctuation, and case differences.
# It's useful for text processing tasks and algorithm challenges.
