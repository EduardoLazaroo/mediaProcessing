import os
import ffmpeg

def extract_audio(video_path, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    try:
        ffmpeg.input(video_path).output(output_path, ac=1, ar='16000').run(overwrite_output=True)
        print(f"[Áudio] Audio extraído para '{output_path}'")
    except ffmpeg.Error as e:
        print("[Erro FFmpeg]", e)
