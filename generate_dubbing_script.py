import os
import json
import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

INPUT_PATH = "outputs/insights.json"
OUTPUT_PATH = "outputs/dubbing_script.txt"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def carregar_insights():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["insights"]

def gerar_script(insights):
    prompt = (
        "Com base nos seguintes insights de um vídeo, gere um roteiro de narração adaptado, "
        "em tom natural e envolvente, com começo, meio e fim. Este texto será utilizado para dublagem.\n\n"
        f"{insights}"
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()

def main():
    insights = carregar_insights()
    script = gerar_script(insights)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(script)
    print(f"Script de dublagem salvo em {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
