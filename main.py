from extract_frames import extract_frames
from extract_audio import extract_audio

video_path = "assets/video.mp4"
frames_output_dir = "outputs/frames"
audio_output_path = "outputs/audio.mp3"

print("🎬 Iniciando extração de vídeo...")
extract_frames(video_path, frames_output_dir)

print("🎧 Iniciando extração de áudio...")
extract_audio(video_path, audio_output_path)

print("✅ Fase 1 finalizada com sucesso.")
