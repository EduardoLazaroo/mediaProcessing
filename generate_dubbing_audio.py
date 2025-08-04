import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

SCRIPT_PATH = "outputs/dubbing_script.txt"
AUDIO_OUTPUT_PATH = "outputs/dubbing_audio.mp3"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_audio(script_path, audio_output_path):
    if not os.path.exists(script_path):
        print("[ERRO] Script de dublagem não encontrado.")
        return

    with open(script_path, "r", encoding="utf-8") as f:
        texto = f.read()

    print("[INFO] Gerando áudio com TTS...")

    resposta = client.audio.speech.create(
        model="tts-1",
        voice="nova",  # Pode usar "echo", "onyx", "shimmer", etc.
        input=texto
    )

    with open(audio_output_path, "wb") as out_file:
        out_file.write(resposta.content)

    print(f"[SUCESSO] Áudio salvo em {audio_output_path}")

if __name__ == "__main__":
    gerar_audio(SCRIPT_PATH, AUDIO_OUTPUT_PATH)
