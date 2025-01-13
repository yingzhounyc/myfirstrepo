import whisper

def transcribe_audio(audio_file, output_file):
    # Load the Whisper model
    print("Loading Whisper model...")
    model = whisper.load_model("base")  # Use "tiny", "small", "medium", or "large" as needed

    # Transcribe the audio file
    print(f"Transcribing {audio_file}...")
    result = model.transcribe(audio_file)

    # Save transcription to a file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(result["text"])

    print(f"Transcription saved to {output_file}")

if __name__ == "__main__":
    audio_file = "your_audio_file.wav"  # Replace with your WAV file name
    output_file = "transcription.txt"
    transcribe_audio(audio_file, output_file)
