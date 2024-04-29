import os
import subprocess


def compress_video(input_path, output_path, quality):
    command = f"ffmpeg -i '{input_path}' -vcodec libx264 -crf {quality} '{output_path}'"
    subprocess.run(command, shell=True)

def process_videos(input_dir, output_dir, quality):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    skipped_files = []

    for file_name in os.listdir(input_dir):
        input_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, file_name)
        if file_name.lower().endswith((".mp4", ".avi", ".mov", ".mkv")):
            print(f"Compressing {file_name}...")
            compress_video(input_path, output_path, quality)
            print(f"Compression of {file_name} finished.")
        else:
            skipped_files.append(file_name)

    if skipped_files:
        print("Skipped files (non-video or unsupported formats):")
        for file in skipped_files:
            print(file)

if __name__ == "__main__":
    input_dir = "/path/to/your/input/directory"
    output_dir = "/path/to/your/output/directory"
    quality = "35"
    process_videos(input_dir, output_dir, quality)

