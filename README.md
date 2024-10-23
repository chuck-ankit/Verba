# Verba - Multilingual AI Chatbot with Fine-tuned Gemma LLM

Verba is a multilingual chatbot application that leverages a fine-tuned version of the Gemma LLM model (based on `google/gemma-7b`). The model has been fine-tuned using LoRA on 15 Indian languages and English language instruction datasets. The chatbot is built using React for the frontend and Python with FastAPI for the backend.

## Features

- Supports multiple Indian languages (Hindi, Telugu, Marathi, Urdu, Assamese, Konkani, Nepali, Sindhi, Tamil, Kannada, Malayalam, Gujarati, Punjabi, Bengali, and Odia) as well as English.
- Interactive and user-friendly chatbot interface built with React.
- Fast and efficient inference using `unsloth` and HuggingFace libraries.
- Deployed using FastAPI as the backend framework.

## Demo

You can interact with the chatbot by entering instructions in different languages, and the model will respond accordingly.

## Tech Stack

- **Frontend**: React, HTML, CSS, JavaScript
- **Backend**: FastAPI, Python
- **Machine Learning**: Fine-tuned Gemma LLM model using `unsloth` for inference.
- **Deployment**: Docker, FastAPI

## Clone and Run the Project

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/chuck-ankit/Verba.git
cd Verba
