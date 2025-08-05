# MediaProcessing

**mediaProcessing** é uma plataforma modular de análise multimodal de vídeos com Inteligência Artificial. O projeto automatiza o processamento de vídeos, explorando tanto o conteúdo visual quanto o textual para gerar análises profundas, insights inteligentes e artefatos como roteiros de dublagem e áudio sintetizado.

---

## 🚀 Visão Geral

O objetivo do projeto é proporcionar um pipeline completo de análise de vídeos, combinando transcrição automática, análise textual, análise visual de frames, compreensão multimodal, geração de insights e roteirização para dublagem — tudo integrado a uma interface interativa com Streamlit.

---

## 🛠️ Tecnologias Utilizadas

- **Python** — linguagem principal
- **Streamlit** — interface web interativa
- **OpenAI API (GPT-4o, Whisper)** — análise textual, visual, geração de insights, roteiros e transcrição de áudio
- **dotenv** — gerenciamento de variáveis de ambiente (API keys)
- **Pillow (PIL)** — manipulação de imagens dos frames
- **Subprocess, JSON, Base64** — suporte ao processamento, execução de scripts e manipulação de dados
- **Outras dependências** podem ser listadas no `requirements.txt`

---

## 🧩 Pipeline de Processamento

1. **Extração de Frames e Áudio**
   - O vídeo original é processado para extrair imagens de frames e o áudio em MP3.

2. **Transcrição do Áudio**
   - O áudio é transcrito automaticamente utilizando Whisper.

3. **Análise Textual**
   - A transcrição é analisada pelo GPT-4o, retornando resumo, tópicos, sentimentos e personagens mencionados.

4. **Análise Visual dos Frames**
   - Cada frame é analisado pelo GPT-4o, gerando descrições detalhadas do conteúdo visual.

5. **Compreensão Multimodal**
   - As análises textual e visual são combinadas para obter uma visão integrada do vídeo.

6. **Geração de Insights**
   - Insights de alto nível são gerados com base na compreensão multimodal.

7. **Roteiro de Dublagem**
   - Um roteiro adaptado é criado automaticamente a partir dos insights.

8. **Geração de Áudio Sintetizado**
   - O roteiro pode ser convertido em áudio por TTS.

9. **Interface Interativa**
   - Todo o pipeline é integrado e facilmente controlado via Streamlit.

---

## 📂 Estrutura de Diretórios

```
assets/
  video.mp4                # Vídeo original
outputs/
  frames/                  # Frames extraídos
  audio.mp3                # Áudio extraído
  transcription.txt        # Transcrição do áudio
  analysis.json            # Análise textual
  frames_analysis.json     # Análise visual dos frames
  multimodal_understanding.json # Análise multimodal combinada
  insights.json            # Insights extraídos
  dubbing_script.txt       # Roteiro de dublagem
  dubbing_audio.mp3        # Áudio de dublagem gerado
```

---

## ⚙️ Como Executar

1. **Pré-requisitos:**
   - Python 3.8+
   - Chave de API OpenAI
   - Dependências do projeto (`pip install -r requirements.txt`)

2. **Configuração do ambiente:**
   - Crie um arquivo `.env` com sua chave de API OpenAI:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

3. **Execução:**
   - Inicie o Streamlit:
     ```
     streamlit run app.py
     ```
   - Siga as etapas pela interface para processar seu vídeo.

---

## 📝 Etapas Detalhadas

- Scripts principais:
  - `main.py`: orquestra extração de frames, áudio e transcrição
  - `analyze_transcription.py`: análise textual da transcrição
  - `analyze_frames.py`: análise visual dos frames
  - `multimodal_understanding.py`: compreensão combinada texto+imagem
  - `generate_insights.py`: geração de insights inteligentes
  - `generate_dubbing_script.py`: roteiro para dublagem
  - `generate_dubbing_audio.py`: gera áudio do roteiro (opcional, requer TTS)

---

## 🤖 Exemplos de Uso

- **Análise multimodal de vídeos educacionais**
- **Geração automática de roteiros a partir de vídeos**
- **Extração de insights para contextos sociais, culturais ou didáticos**

---

## 👤 Autor

[Eduardo Lazaro](https://github.com/EduardoLazaroo)

---
