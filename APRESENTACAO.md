# Apresentação Profissional: MediaProcessing

## 1. Identidade e Proposta de Valor

O **MediaProcessing** é uma plataforma e arquitetura para **análise multimodal de vídeo** potencializada por inteligência artificial generativa. O projeto enfrenta o desafio de extrair sentido profundo de mídias audiovisuais não estruturadas, integrando de ponta a ponta a separação de sinais, visão computacional, reconhecimento automático de fala e fusão cognitiva em modelos multimodais de fronteira.

Em vez de tratar vídeo apenas como uma sequência passiva de quadros ou um arquivo de áudio isolado, o sistema executa uma **decomposição sincronizada**: quadros-chave são processados com **OpenCV** e analisados pelo **GPT-4o Vision**, enquanto a trilha acústica é isolada via **FFmpeg**, transcrita pelo **Whisper** e sintetizada em reflexões temáticas e roteiros de dublagem profissional reproduzidos por **TTS**.

---

## 2. Destaques Técnicos e Decisões de Arquitetura

1. **Pipeline Assíncrono com Amostragem Eficiente**: Implementa amostragem temporal uniforme a cada 30 quadros (1,25s), capturando 86 quadros representativos de uma mídia de 107 segundos, reduzindo custos de inferência visual sem perda de continuidade narrativa.
2. **Fusão Cognitiva Texto-Visão**: Supera a limitação de transcrições imperfeitas ao cruzar o áudio transcrito com a semântica visual dos frames, permitindo que a LLM identifique metáforas implícitas, arcos de personagens e ambientações cênicas.
3. **Geração Automatizada de Artefatos Downstream**: A compreensão multimodal alimenta a criação automática de roteiros de dublagem estruturados em três atos (Início, Meio e Fim) e sua subsequente síntese em áudio de alta qualidade (3,56 MB).
4. **Interface Unificada e Transparente**: Toda a cadeia é inspecionável por meio de uma interface Streamlit reativa, permitindo que operadores humanos naveguem pelos quadros, inspecionem hipóteses da IA e reexecutem etapas sob demanda.

---

## 3. Texto Executivo para Divulgação / Portfólio

> "O processamento inteligente de vídeos requer a harmonização entre visão computacional, acústica e compreensão de linguagem natural. No projeto **MediaProcessing**, desenvolvi uma solução completa em Python e **Streamlit** que orquestra **OpenCV**, **FFmpeg**, **OpenAI Whisper** e **GPT-4o Vision**.
>
> O pipeline decompõe fluxos de vídeo em canais paralelos de imagem e áudio, executa transcrição fonética e inspeção visual por quadro-chave e realiza a fusão cognitiva das modalidades. A partir dessa compreensão, o sistema produz automaticamente análises de sentimento, reflexões socioeducacionais e roteiros adaptados para dublagem em três atos, convertidos em áudio sintetizado por TTS.
>
> Validado sobre conteúdo audiovisual real, o pipeline demonstrou alta consistência narrativa, robustez no processamento de mídia e uma interface interativa centrada na experiência do usuário."

---

## 4. Evidências Empíricas e Visuais Disponíveis

- [`evidencias/arquitetura_pipeline_multimodal.png`](evidencias/arquitetura_pipeline_multimodal.png): Fluxograma completo do pipeline desde a ingestão do MP4 até a entrega dos artefatos e dashboard Streamlit.
- [`evidencias/decomposicao_multimodal_frames_audio.png`](evidencias/decomposicao_multimodal_frames_audio.png): Gráfico de evolução da luminância e canais RGB dos 86 frames correlacionados à divisão de atos narrativos.
- [`evidencias/log_execucao_real.txt`](evidencias/log_execucao_real.txt): Relatório de inspeção com métricas exatas de resolução (640x360), contagem de frames (2568), duração (107,1s) e tamanhos de áudio.
