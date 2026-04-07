import subprocess
import os

input_file = os.path.expanduser("~/Downloads/Ali Abdaal – Part-Time Youtuber Academy/2.0.GuestWorkshops/29.06.2021.0 - 700k in 12 Videos - A Conversation with James Jani.mp4")
output_file = os.path.splitext(input_file)[0] + ".mp3"

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

print("Converting file...")
mp4_to_mp3(input_file, output_file)
print("✅ Done")