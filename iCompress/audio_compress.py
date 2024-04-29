import os
from pydub import AudioSegment

def compress_audio(input_dir, output_dir, target_bitrate):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    audio_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
    skipped_files = []

    for file in audio_files:
        if not file.lower().endswith((".mp3", ".wav", ".ogg", ".flac", ".aac")):
            skipped_files.append(file)
            continue

        audio = AudioSegment.from_file(os.path.join(input_dir, file))
        compressed_audio = audio.set_frame_rate(audio.frame_rate).set_channels(audio.channels).set_sample_width(audio.sample_width)
        output_file_path = os.path.join(output_dir, os.path.splitext(file)[0] + "_compressed.mp3")
        compressed_audio.export(output_file_path, format="mp3", bitrate=target_bitrate)
        print(f"{file} compressed successfully and saved as {os.path.basename(output_file_path)}")

    if skipped_files:
        print("\nSkipped files (not audio files):")
        for skipped_file in skipped_files:
            print(skipped_file)

if __name__ == "__main__":
    input_directory = "/path/to/your/input/directory"
    output_directory = "/path/to/your/output/directory"
    target_bitrate = "64k"
    compress_audio(input_directory, output_directory, target_bitrate)

