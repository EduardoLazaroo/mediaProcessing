import os
import json
import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

TRANSCRIPTION_PATH = "outputs/transcription.txt"
FRAMES_ANALYSIS_PATH = "outputs/frames_analysis.json"
OUTPUT_PATH = "outputs/multimodal_understanding.json"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def carregar_dados():
    with open(TRANSCRIPTION_PATH, "r", encoding="utf-8") as f:
        transcricao = f.read()
    with open(FRAMES_ANALYSIS_PATH, "r", encoding="utf-8") as f:
        frames = json.load(f)
    return transcricao, frames

def gerar_compreensao(transcricao, frames):
    frames_descricao = "\n\n".join(
        f"{nome}:\n{descricao}" for nome, descricao in frames.items()
    )
    prompt = (
        "A seguir temos a transcrição de um vídeo e a descrição visual de seus frames. "
        "Faça uma análise combinada do conteúdo, identificando o contexto, intenções dos personagens, mensagens implícitas e possíveis interpretações.\n\n"
        f"Transcrição:\n{transcricao}\n\nDescrição dos frames:\n{frames_descricao}"
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )

    return response.choices[0].message.content.strip()

def main():
    transcricao, frames = carregar_dados()
    analise_combinada = gerar_compreensao(transcricao, frames)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump({"compreensao_multimodal": analise_combinada}, f, ensure_ascii=False, indent=2)
    print(f"Análise multimodal salva em {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
