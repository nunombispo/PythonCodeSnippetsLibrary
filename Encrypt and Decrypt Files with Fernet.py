# pip install cryptography

from cryptography.fernet import Fernet


def generate_key():
    """Generate a new Fernet key."""
    return Fernet.generate_key()


def save_key(key, filename="secret.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)


def load_key(filename="secret.key"):
    with open(filename, "rb") as key_file:
        return key_file.read()


def encrypt_file(input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, "rb") as file:
        data = file.read()
    encrypted = fernet.encrypt(data)
    with open(output_file, "wb") as file:
        file.write(encrypted)


def decrypt_file(input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, "rb") as file:
        encrypted_data = file.read()
    decrypted = fernet.decrypt(encrypted_data)
    with open(output_file, "wb") as file:
        file.write(decrypted)


# Example usage:
if __name__ == "__main__":
    # Generate and save a key (do this once)
    key = generate_key()
    save_key(key)

    # Load the key for encryption/decryption
    key = load_key()

    # Encrypt a file
    encrypt_file("plain.txt", "encrypted.txt", key)

    # Decrypt the file
    decrypt_file("encrypted.txt", "decrypted.txt", key)


# Why?
# This snippet uses Python's cryptography library to encrypt and decrypt files using the Fernet
# symmetric encryption.
# It’s essential for protecting sensitive data, secure file storage, and can be easily integrated
# into larger security-focused applications.
