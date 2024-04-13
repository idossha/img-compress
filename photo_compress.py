import os

from PIL import Image


def resize_images(input_dir, output_dir, max_width=3200, max_height=2400):
    """
    Resize images in a directory while keeping their original aspect ratio.

    Args:
    - input_dir (str): Path to the input directory containing images.
    - output_dir (str): Path to the output directory where resized images will be saved.
    - max_width (int): Maximum width for resized images.
    - max_height (int): Maximum height for resized images.
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List all files in the input directory
    files = os.listdir(input_dir)
    skipped_files = []

    # Process each file in the input directory
    for file in files:
        input_path = os.path.join(input_dir, file)
        output_path = os.path.join(output_dir, file)

        try:
            # Open the file and check if it's an image
            with Image.open(input_path) as img:
                # Resize the image while preserving aspect ratio
                img.thumbnail((max_width, max_height))

                # Save the resized image
                img.save(output_path)

                print(f"Resized {file}")
        except Exception as e:
            skipped_files.append(file)
            print(f"Skipping {file}: Not an image.")

    print("Image resizing complete.")
    if skipped_files:
        print("Skipped files:")
        for skipped_file in skipped_files:
            print(skipped_file)


# Example usage
input_directory = "/Users/idohaber/Desktop/Website assets/02_assets_photos"
output_directory = "/Users/idohaber/Desktop/02_assets_photos"
resize_images(input_directory, output_directory)
