import streamlit as st
import os
import json
from PIL import Image

st.set_page_config(page_title="Análise Multimodal de Vídeo", layout="wide")

VIDEO_PATH = "assets/video.mp4"
TRANSCRIPTION_PATH = "outputs/transcription.txt"
TEXT_ANALYSIS_PATH = "outputs/analysis.json"
FRAMES_PATH = "outputs/frames"
FRAMES_ANALYSIS_PATH = "outputs/frames_analysis.json"
MULTIMODAL_PATH = "outputs/multimodal_understanding.json"
INSIGHTS_PATH = "outputs/insights.json"
SCRIPT_PATH = "outputs/dubbing_script.txt"
AUDIO_PATH = "outputs/dubbing_audio.mp3"

st.title("📽️ Análise Multimodal de Vídeo com IA")

# --- Exibe o vídeo ---
st.subheader("🎬 Vídeo Original")
if os.path.exists(VIDEO_PATH):
    st.video(VIDEO_PATH)
else:
    st.warning("Vídeo não encontrado.")

# --- Transcrição e análise textual ---
st.subheader("📝 Transcrição e Análise Textual")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Transcrição")
    if os.path.exists(TRANSCRIPTION_PATH):
        with open(TRANSCRIPTION_PATH, "r", encoding="utf-8") as f:
            st.text(f.read())
    else:
        st.warning("Arquivo de transcrição não encontrado.")

with col2:
    st.markdown("### Análise Textual")
    if os.path.exists(TEXT_ANALYSIS_PATH):
        with open(TEXT_ANALYSIS_PATH, "r", encoding="utf-8") as f:
            analise = json.load(f)
            st.markdown(f"**Resumo:** {analise.get('resumo', '')}")
            st.markdown(f"**Tópicos:** {', '.join(analise.get('topicos', []))}")
            st.markdown(f"**Sentimentos:** {analise.get('sentimentos', '')}")
            st.markdown(f"**Personagens:** {', '.join(analise.get('personagens', []))}")
    else:
        st.warning("Análise textual não encontrada.")

# --- Análise Visual dos Frames ---
st.subheader("🖼️ Análise Visual dos Frames")

if os.path.exists(FRAMES_ANALYSIS_PATH):
    with open(FRAMES_ANALYSIS_PATH, "r", encoding="utf-8") as f:
        frames_analysis = json.load(f)

    frame_files = sorted([f for f in os.listdir(FRAMES_PATH) if f.lower().endswith(".jpg")])
    index = st.slider("Selecionar Frame", 0, len(frame_files) - 1, 0)
    selected_frame = frame_files[index]
    frame_path = os.path.join(FRAMES_PATH, selected_frame)

    if os.path.exists(frame_path):
        st.image(Image.open(frame_path), caption=selected_frame, use_container_width=True)
        with st.expander("Descrição Visual Completa"):
            st.write(frames_analysis.get(selected_frame, "Sem análise disponível."))
    else:
        st.warning("Imagem do frame não encontrada.")
else:
    st.warning("Arquivo de análise visual não encontrado.")

st.markdown("---")

# --- Etapa 6: Compreensão Multimodal ---
st.subheader("🧠 Compreensão Multimodal")

if os.path.exists(MULTIMODAL_PATH):
    with open(MULTIMODAL_PATH, "r", encoding="utf-8") as f:
        multimodal = json.load(f)

    resumo_geral = str(multimodal.get("resumo", "")).replace("\n", " ").strip()
    st.markdown(f"**Resumo Geral:** {resumo_geral}")
    
    st.markdown("**Correlação entre Texto e Imagem:**")
    for item in multimodal.get("correlacoes", []):
        st.markdown(f"- {str(item).strip()}")
else:
    st.warning("Compreensão multimodal não encontrada.")

st.markdown("---")

# --- Etapa 7: Geração de Insights ---
st.subheader("💡 Insights Inteligentes")

if os.path.exists(INSIGHTS_PATH):
    with open(INSIGHTS_PATH, "r", encoding="utf-8") as f:
        insights = json.load(f)

    insights_text = insights.get("insights", "")
    st.markdown(insights_text, unsafe_allow_html=True)
else:
    st.warning("Arquivo de insights não encontrado.")

st.markdown("---")

# --- Etapa 8: Script de Dublagem ---
st.subheader("🗣️ Script de Dublagem")

if os.path.exists(SCRIPT_PATH):
    with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
        script = f.read()
    st.markdown(f"```\n{script}\n```")
else:
    st.warning("Script de dublagem não encontrado.")

st.markdown("---")

# --- Etapa 9: Áudio Gerado com TTS ---
st.subheader("🔊 Áudio Gerado")

if os.path.exists(AUDIO_PATH):
    st.audio(AUDIO_PATH)
else:
    st.warning("Áudio de dublagem ainda não gerado.")
