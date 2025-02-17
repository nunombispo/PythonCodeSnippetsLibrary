import zipfile
import os


def compress_files(directory, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                # Add file to the zip, preserving folder structure
                zipf.write(file_path, os.path.relpath(file_path, directory))
    print(f"Files compressed into '{output_zip}'")


def decompress_file(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        zipf.extractall(extract_to)
    print(f"Files extracted to '{extract_to}'")


# Example usage:
# Compress all files in the 'data' directory
compress_files('data', 'archive.zip')

# Decompress the 'archive.zip' into the 'extracted' folder
decompress_file('archive.zip', 'extracted')


# Why? This snippet allows you to compress and decompress files using Python's built-in zipfile module. It keeps
# directory structures intact and is perfect for file backups, data sharing, or organizing multiple files into a
# single archive.
