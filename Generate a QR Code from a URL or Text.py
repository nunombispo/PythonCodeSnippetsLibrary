# pip install qrcode[pil]

import qrcode


def generate_qr(data, filename="qrcode.png"):
    # Create a QR Code instance with specific parameters
    qr = qrcode.QRCode(
        version=1,  # Version 1: 21x21 matrix
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
        box_size=10,  # Size of each box in pixels
        border=4,  # Thickness of the border (boxes)
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR Code generated and saved as {filename}")


# Example usage
generate_qr("https://example.com", "example_qr.png")


# Why?
# This snippet uses the qrcode library to generate a QR code from a given text or URL.
# It’s practical for creating quick links, sharing information offline, or integrating QR codes into
# web apps and marketing materials.