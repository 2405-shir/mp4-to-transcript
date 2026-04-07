import subprocess
import os

folder = os.path.expanduser("~/Downloads/Matt D Avella - Master YouTube")

def mp4_to_mp3(input_file, output_file):
    command = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-ab", "192k",
        "-ar", "44100",
        "-y",
        output_file
    ]
    subprocess.run(command)

for file in os.listdir(folder):
    if file.endswith(".mp4"):
        input_path = os.path.join(folder, file)
        output_path = os.path.join(folder, os.path.splitext(file)[0] + ".mp3")

        print(f"Converting: {file}")
        mp4_to_mp3(input_path, output_path)

print("✅ Done converting all files.")
