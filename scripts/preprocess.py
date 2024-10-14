from transformers import AutoTokenizer

def preprocess(data):
    tokenizer = AutoTokenizer.from_pretrained("ollama/model-name")
    return tokenizer(data['text'], truncation=True, padding=True)

