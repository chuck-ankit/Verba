from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the fine-tuned model and tokenizer
MODEL_NAME = "Telugu-LLM-Labs/Indic-gemma-7b-finetuned-sft-Navarasa-2.0"
device = "cuda" if torch.cuda.is_available() else "cpu"

model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).to(device)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def generate_response(instruction: str, input_text: str):
    input_prompt = f"### Instruction: {instruction}\n### Input: {input_text}\n### Response:"
    inputs = tokenizer([input_prompt], return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_new_tokens=300, use_cache=True)
    response = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    return response
