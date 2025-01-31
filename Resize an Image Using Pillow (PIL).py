from PIL import Image


def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        img = img.resize(size, Image.LANCZOS)
        img.save(output_path)


# Example usage
resize_image("input.png", "output.png", (300, 300))

# Why?
# This snippet allows you to resize images efficiently using Pillow (PIL).
# It('s useful for automating image processing, reducing file sizes, and preparing images for web applications, '
#    'machine learning models, or thumbnails. 🖼️🚀)
