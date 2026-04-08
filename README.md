
Prerequisites
Before running the scripts, you must set up your environment by installing the necessary package manager and media processing tools.

1. Install Homebrew
Open your terminal and paste the following command to install Homebrew, the package manager for macOS:

Bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
2. Install FFmpeg
Once Homebrew is installed, use it to install FFmpeg, which is required for media conversion:

Bash
brew install ffmpeg
Step 1: MP4 to MP3 Conversion
Open convert single mp4.py in your code editor.

Edit the file location within the script to point to the specific MP4 file you wish to convert.

Save the file and run it using the following command in your terminal:

Bash
python3 "convert single mp4.py"
Step 2: Audio to Transcript
This process uses the OpenAI Whisper model to transcribe your audio file into text.

Ensure you have the Whisper library available in your environment.

Run the transcription script:

Bash
python3 "singletranscribe.py"
