# Verba: Multilingual Voice Assistant using Ollama Models (Multimodal)

**Verba** is a powerful Multilingual Voice Assistant Application built using **Ollama models** (multimodal) and fine-tuned locally in a **WSL environment**. Verba understands and responds to user inputs in multiple languages by leveraging cutting-edge natural language processing (NLP) and automatic speech recognition (ASR) models. The project integrates **Whisper** for accurate voice-to-text transcription and Ollama’s language models for intelligent response generation.

## Key Features

- **Multilingual Voice Interaction**: Supports voice inputs and text responses in multiple languages.
- **Local Model Fine-tuning**: Fine-tunes Ollama models locally for custom language capabilities and improved performance.
- **Speech-to-Text and Text-to-Speech Integration**: Utilizes Whisper for transcribing voice inputs and `gTTS` for speech synthesis to create an interactive experience.
- **Performance Monitoring**: Includes tools to track model accuracy, latency, and overall performance during both training and inference.
- **WSL Environment**: Fully operational on Windows Subsystem for Linux (WSL), providing a seamless local development and deployment workflow.
- **Multimodal Support**: Potential for future enhancements to handle image-based queries and responses using multimodal data.

## Project Components

- **Ollama Model Fine-tuning**: Fine-tune the language models using multilingual datasets for improved contextual understanding.
- **Voice Recognition**: Employ `speech_recognition` and Whisper to capture and transcribe voice inputs, which are then processed by the text model.
- **Response Generation**: Handles user queries and generates intelligent responses from fine-tuned models.
- **Text-to-Speech Output**: Converts generated responses into speech using `gTTS`, providing a complete voice assistant experience.
- **Model Performance Monitoring**: Tracks essential metrics, including accuracy, latency, and model loss, ensuring high efficiency.

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/chuck-ankit/Verba.git
   cd verba
