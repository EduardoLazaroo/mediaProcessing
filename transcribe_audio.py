import whisper
import os

def transcribe(audio_path, output_path=None, language="pt"):
    print("🔍 Carregando modelo Whisper...")
    model = whisper.load_model("base")  # ou "small", "medium", "large" conforme necessidade

    print(f"🗣️ Transcrevendo áudio: {audio_path}")
    result = model.transcribe(audio_path, language=language)

    transcription = result["text"]
    print("\n📝 Transcrição:\n", transcription)

    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(transcription)
        print(f"\n💾 Transcrição salva em: {output_path}")

    return transcription
