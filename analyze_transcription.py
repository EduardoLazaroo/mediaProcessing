import os
import openai
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

TRANSCRIPTION_PATH = "outputs/transcription.txt"
ANALYSIS_OUTPUT_PATH = "outputs/analysis.json"

# Inicializa o cliente com a nova sintaxe
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def carregar_transcricao(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()

def analisar_transcricao(texto):
    prompt = f"""
Você é um assistente de IA que analisa transcrições de vídeos em português.

Transcrição:
{texto}

Com base nisso, retorne um JSON com os seguintes campos:
- resumo: parágrafo resumindo o conteúdo.
- topicos: lista dos principais assuntos discutidos.
- sentimentos: análise geral do tom da conversa.
- personagens: nomes de pessoas mencionadas (se houver).

Responda apenas com JSON válido.
"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message.content.strip()

def salvar_analise(analise_json):
    with open(ANALYSIS_OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(analise_json)

def main():
    print("📖 Lendo transcrição...")
    texto = carregar_transcricao(TRANSCRIPTION_PATH)

    print("🧠 Analisando com GPT-4o...")
    analise = analisar_transcricao(texto)

    print("💾 Salvando análise em outputs/analysis.json")
    salvar_analise(analise)

    print("✅ Fase 3 finalizada com sucesso.")

if __name__ == "__main__":
    main()
