# pip install pillow

from PIL import Image
from PIL.ExifTags import TAGS


def extract_exif(image_path):
    """Extracts and returns EXIF metadata from an image."""
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if not exif_data:
            print("No EXIF data found.")
            return {}

        # Decode EXIF tags
        exif = {}
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            exif[tag_name] = value
        return exif
    except Exception as e:
        print(f"Error extracting EXIF data: {e}")
        return {}


# Example usage:
if __name__ == "__main__":
    image_path = "sample.jpg"  # Replace with your image file
    exif = extract_exif(image_path)
    for key, value in exif.items():
        print(f"{key}: {value}")

# Why? This snippet leverages the Pillow library to extract and decode EXIF metadata from an image. It's useful for
# analyzing camera settings, geolocation data, and other metadata embedded in digital photos—ideal for photographers,
# digital forensics, and data enthusiasts!
