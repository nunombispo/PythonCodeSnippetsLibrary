from PIL import Image
import os


def create_animated_gif(image_folder, output_path, duration=500):
    frames = []
    # Collect image files and sort them to maintain order
    for file in sorted(os.listdir(image_folder)):
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            frame = Image.open(os.path.join(image_folder, file))
            frames.append(frame)

    if frames:
        frames[0].save(
            output_path,
            format='GIF',
            append_images=frames[1:],
            save_all=True,
            duration=duration,
            loop=0
        )
        print(f"Animated GIF saved as '{output_path}'")
    else:
        print("No images found in the specified folder.")


# Example usage:
# Place your images in a folder named 'images'
create_animated_gif('images', 'animated.gif', duration=300)


# Why? This snippet uses Pillow to compile multiple images into an animated GIF. It's a creative way to generate
# dynamic visuals—perfect for presentations, social media, or marketing materials!

