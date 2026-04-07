import whisper
import os

# 👇 PUT YOUR EXACT FOLDER PATH HERE
INPUT_FOLDER = "/Users/shirinreh/Downloads/Matt D Avella - Master YouTube"

MODEL_SIZE = "base"

def transcribe_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return

    print("⏳ Loading model...")
    model = whisper.load_model(MODEL_SIZE)

    files = [f for f in os.listdir(folder_path) if f.lower().endswith(".mp3")]

    if not files:
        print("⚠️ No MP3 files found.")
        return

    print(f"🎧 Found {len(files)} MP3 files\n")

    for i, file in enumerate(files, 1):
        file_path = os.path.join(folder_path, file)
        output_path = os.path.join(folder_path, file.replace(".mp3", ".txt"))

        print(f"[{i}/{len(files)}] Transcribing: {file}")

        try:
            result = model.transcribe(file_path)

            with open(output_path, "w") as f:
                f.write(result["text"])

            print(f"✅ Saved: {output_path}\n")

        except Exception as e:
            print(f"❌ Error with {file}: {e}\n")

    print("🎉 Done!")

if __name__ == "__main__":
    transcribe_folder(INPUT_FOLDER)
