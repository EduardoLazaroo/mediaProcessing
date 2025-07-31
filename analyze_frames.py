import os
import openai
import json
import base64
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

FRAMES_DIR = "outputs/frames"
OUTPUT_PATH = "outputs/frames_analysis.json"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analisar_frame(frame_path):
    print(f"🖼️ Analisando {frame_path}...")

    with open(frame_path, "rb") as img_file:
        imagem_bytes = img_file.read()
        imagem_base64 = base64.b64encode(imagem_bytes).decode("utf-8")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Descreva o que você vê nesta imagem. Liste objetos, contexto da cena e possíveis emoções envolvidas."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{imagem_base64}"}}
                ],
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content.strip()

def analisar_frames_em_diretorio(diretorio):
    analises = {}

    for nome_arquivo in sorted(os.listdir(diretorio)):
        if nome_arquivo.lower().endswith(".jpg"):
            caminho = os.path.join(diretorio, nome_arquivo)
            analise = analisar_frame(caminho)
            analises[nome_arquivo] = analise

    return analises

def salvar_analises(analises, caminho):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(analises, f, ensure_ascii=False, indent=2)

def main():
    print("🔍 Iniciando análise visual dos frames...")
    analises = analisar_frames_em_diretorio(FRAMES_DIR)
    salvar_analises(analises, OUTPUT_PATH)
    print(f"✅ Análise salva em {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
