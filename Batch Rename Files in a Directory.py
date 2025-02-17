import os


def batch_rename(directory, prefix):
    for count, filename in enumerate(os.listdir(directory)):
        # Skip directories
        filepath = os.path.join(directory, filename)
        if os.path.isdir(filepath):
            continue

        # Extract file extension
        _, ext = os.path.splitext(filename)
        new_name = f"{prefix}_{count}{ext}"
        new_filepath = os.path.join(directory, new_name)

        os.rename(filepath, new_filepath)
        print(f"Renamed '{filename}' to '{new_name}'")


# Example usage: Renames all files in the current directory with the prefix "file"
if __name__ == "__main__":
    batch_rename(".", "file")


# Why? This snippet batch renames files in a specified directory by adding a custom prefix and a unique counter to
# each file. It's a practical tool for organizing files, cleaning up messy directories, or managing photo
# collections, and it demonstrates file I/O operations using Python's os module.
