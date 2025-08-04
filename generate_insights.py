import os
import json
import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

INPUT_PATH = "outputs/multimodal_understanding.json"
OUTPUT_PATH = "outputs/insights.json"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def carregar_analise():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["compreensao_multimodal"]

def gerar_insights(analise):
    prompt = (
        "A seguir está uma análise multimodal de um vídeo. Gere insights úteis, como aprendizados, reflexões, valores transmitidos, ou aplicações em contextos educacionais, sociais ou culturais.\n\n"
        f"{analise}"
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
    )

    return response.choices[0].message.content.strip()

def main():
    analise = carregar_analise()
    insights = gerar_insights(analise)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump({"insights": insights}, f, ensure_ascii=False, indent=2)
    print(f"Insights gerados em {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
