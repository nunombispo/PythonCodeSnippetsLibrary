# pip install requests tqdm

import requests
from tqdm import tqdm


def download_file(url, output_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kilobyte per block
    with open(output_path, 'wb') as file, tqdm(total=total_size, unit='B', unit_scale=True, desc=output_path) as pbar:
        for data in response.iter_content(block_size):
            file.write(data)
            pbar.update(len(data))


# Example usage
if __name__ == "__main__":
    file_url = "https://example.com/file.zip"  # Replace with a valid URL
    download_file(file_url, "file.zip")


# Why?
# This snippet downloads a file from a given URL and uses tqdm to display a live progress bar.
# It’s perfect for automating downloads, giving users visual feedback during long transfers, and
# enhancing command-line utilities.
