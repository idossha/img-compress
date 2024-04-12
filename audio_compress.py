import os

from pydub import AudioSegment


def compress_audio(input_dir, output_dir, target_bitrate):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get list of audio files in the input directory
    audio_files = [
        f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))
    ]

    skipped_files = []

    for file in audio_files:
        # Check if the file is an audio file
        if not file.lower().endswith((".mp3", ".wav", ".ogg", ".flac", ".aac")):
            skipped_files.append(file)
            continue

        # Load audio file
        audio = AudioSegment.from_file(os.path.join(input_dir, file))

        # Compress audio with specified target bitrate
        compressed_audio = (
            audio.set_frame_rate(audio.frame_rate)
            .set_channels(audio.channels)
            .set_sample_width(audio.sample_width)
        )

        # Determine output file path
        output_file_path = os.path.join(
            output_dir, os.path.splitext(file)[0] + "_compressed.mp3"
        )

        # Export compressed audio
        compressed_audio.export(output_file_path, format="mp3", bitrate=target_bitrate)

        print(
            f"{file} compressed successfully and saved as {os.path.basename(output_file_path)}"
        )

    if skipped_files:
        print("\nSkipped files (not audio files):")
        for skipped_file in skipped_files:
            print(skipped_file)


input_directory = "/Users/idohaber/Desktop/Website assets/04_assets_music_audio"
output_directory = "/Users/idohaber/Desktop/audio_output"
target_bitrate = "128k"  # Adjust the target bitrate as needed

compress_audio(input_directory, output_directory, target_bitrate)
