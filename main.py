from extract_frames import extract_frames
from extract_audio import extract_audio
from transcribe_audio import transcribe
from analyze_frames import main as analisar_frames

video_path = "assets/video.mp4"
frames_output_dir = "outputs/frames"
audio_output_path = "outputs/audio.mp3"
transcription_output_path = "outputs/transcription.txt"

print("🎬 Iniciando extração de vídeo...")
extract_frames(video_path, frames_output_dir)

print("🎧 Iniciando extração de áudio...")
extract_audio(video_path, audio_output_path)

print("🗣️ Iniciando transcrição com Whisper...")
transcribe(audio_output_path, transcription_output_path)

print("🧠 Iniciando análise visual dos frames...")
analisar_frames()