import re


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


# Example usage
print(is_valid_email("test@example.com"))  # Output: True
print(is_valid_email("invalid-email"))  # Output: False

# Why?
# This snippet validates email addresses using a regular expression, making it handy for form validation or
# user input processing. It’s a practical demonstration of regex and input validation in Python.
