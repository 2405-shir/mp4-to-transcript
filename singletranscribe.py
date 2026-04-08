import whisper
import os

# 👇 PUT YOUR EXACT FILE PATH HERE (MP4 or MP3)
INPUT_FILE = "/Users/shirinreh/Downloads/10_Min_Pilates.mp4"

MODEL_SIZE = "base"

def transcribe_file(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    print("⏳ Loading model...")
    model = whisper.load_model(MODEL_SIZE)

    # Output file (same name, .txt)
    output_path = os.path.splitext(file_path)[0] + ".txt"

    print(f"🎧 Transcribing: {os.path.basename(file_path)}")

    try:
        result = model.transcribe(file_path)

        with open(output_path, "w") as f:
            f.write(result["text"])

        print(f"✅ Saved: {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")

    print("🎉 Done!")

if __name__ == "__main__":
    transcribe_file(INPUT_FILE)