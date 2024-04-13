import os
import subprocess  # allows you to run command line tools


def compress_video(input_path, output_path, quality):
    # ffmpeg command to compress video
    command = f"ffmpeg -i '{input_path}' -vcodec libx264 -crf {quality} '{output_path}'"
    subprocess.run(command, shell=True)


def process_videos(input_dir, output_dir, quality):
    skipped_files = []

    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each file in the directory
    for file_name in os.listdir(input_dir):
        input_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, file_name)

        # Check if the file is a video (basic check)
        if file_name.lower().endswith((".mp4", ".avi", ".mov", ".mkv")):
            print(f"Compressing {file_name}...")
            compress_video(input_path, output_path, quality)
            print(f"Compression of {file_name} finished.")
        else:
            skipped_files.append(file_name)

    # Report skipped files
    if skipped_files:
        print("Skipped files (non-video or unsupported formats):")
        for file in skipped_files:
            print(file)


if __name__ == "__main__":
    # Define your parameters here
    input_dir = "/Users/idohaber/Desktop/in"
    output_dir = "/Users/idohaber/Desktop/out"
    quality = "35"

    """
    The higher the quality, the more you compress
     Example: use 23 for medium quality

    """

    process_videos(input_dir, output_dir, quality)
