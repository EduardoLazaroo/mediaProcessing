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
        st.markdown("**Descrição Visual:**")
        st.write(frames_analysis.get(selected_frame, "Sem análise disponível."))
    else:
        st.warning("Imagem do frame não encontrada.")
else:
    st.warning("Arquivo de análise visual não encontrado.")
