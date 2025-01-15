import random
import string


def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


# Example usage
print(generate_password(12))  # Output: A randomly generated 12-character password

# Why? This snippet generates a secure random password with a customizable length, using a mix of letters, numbers,
# and symbols. It's practical for enhancing security and a great example of Python's random module in action.
