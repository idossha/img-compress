import os

from PIL import Image


def resize_images(input_dir, output_dir, max_width, max_height):
    """
    Resize images in a directory while keeping their original aspect ratio.

    Args:
    - input_dir (str): Path to the input directory containing images.
    - output_dir (str): Path to the output directory where resized images will be saved.
    - max_width (int): Maximum width for resized images.
    - max_height (int): Maximum height for resized images.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    files = os.listdir(input_dir)
    skipped_files = []

    for file in files:
        input_path = os.path.join(input_dir, file)
        output_path = os.path.join(output_dir, file)
        try:
            with Image.open(input_path) as img:
                # Resize the image while preserving aspect ratio
                img.thumbnail((max_width, max_height))
                img.save(output_path)
                print(f"Resized {file}")
        except Exception as e:
            skipped_files.append(file)
            print(f"Skipping {file}: Not an image or unsupported image format.")

    if skipped_files:
        print("Skipped files:")
        for skipped_file in skipped_files:
            print(skipped_file)

if __name__ == "__main__":
    input_directory = "/path/to/your/input/directory"
    output_directory = "/path/to/your/output/directory"
    # Set default or prompt for user input
    max_width = int(input("Enter maximum width for images: "))
    max_height = int(input("Enter maximum height for images: "))
    resize_images(input_directory, output_directory, max_width, max_height)

