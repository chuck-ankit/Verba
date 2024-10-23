# Install necessary libraries
!pip install -U xformers --index-url https://download.pytorch.org/whl/cu121
!pip install "unsloth[kaggle-new] @git+https://github.com/unslothai/unsloth.git@nightly"

# Import required libraries
from unsloth import FastLanguageModel
from unsloth.trainers import SFTTrainer, LoRAConfig
import torch

# Define paths and configurations
model_name = "google/gemma-7b"  # Base model
tokenizer_name = model_name

# Load the model and tokenizer
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=model_name,
    max_seq_length=2048,
    dtype=None,  # Auto detection, you can set 'torch.float16' or 'torch.bfloat16' for specific GPUs
    load_in_4bit=False,
    device_map="auto"
)

# Enable LoRA fine-tuning
lora_config = LoRAConfig(
    r=8,  # Rank of low-rank adaptation
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],  # Target specific attention layers for LoRA
    lora_dropout=0.05,
    bias="none"
)

# Define fine-tuning datasets (you already have datasets per language)
datasets = [
    "ravithejads/samvaad-hi-filtered",  # Hindi
    "HydraIndicLM/hindi_alpaca_dolly_67k",  # Hindi
    "Telugu-LLM-Labs/telugu_alpaca_yahma_cleaned_filtered_romanized",  # Telugu
    "Telugu-LLM-Labs/telugu_teknium_GPTeacher_general_instruct_filtered_romanized",  # Telugu
    "Telugu-LLM-Labs/marathi_alpaca_cleaned_filtered",  # Marathi
    "Telugu-LLM-Labs/urdu_alpaca_yahma_cleaned_filtered",  # Urdu
    "Telugu-LLM-Labs/assamese_alpaca_yahma_cleaned_filtered",  # Assamese
    "Telugu-LLM-Labs/konkani_alpaca_yahma_cleaned_filtered",  # Konkani
    "Telugu-LLM-Labs/nepali_alpaca_yahma_cleaned_filtered",  # Nepali
    "Telugu-LLM-Labs/sindhi_alpaca_yahma_cleaned_filtered",  # Sindhi
    "abhinand/tamil-alpaca",  # Tamil
    "Tensoic/airoboros-3.2_kn",  # Kannada
    "VishnuPJ/Alpaca_Instruct_Malayalam",  # Malayalam
    "Tensoic/Alpaca-Gujarati",  # Gujarati
    "HydraIndicLM/punjabi_alpaca_52K",  # Punjabi
    "HydraIndicLM/bengali_alpaca_dolly_67k",  # Bengali
    "OdiaGenAI/Odia_Alpaca_instructions_52k",  # Odia
    "yahma/alpaca-cleaned"  # English
]

# Trainer configuration
trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    dataset_names=datasets,
    data_loading_workers=8,  # Number of CPU threads for data loading
    batch_size=2,  # Adjust batch size based on available GPU memory
    gradient_accumulation_steps=8,  # Helps to simulate larger batch sizes
    learning_rate=2e-5,
    num_train_epochs=3,
    weight_decay=0.01,
    lora_config=lora_config,  # Pass LoRA config for fine-tuning
    output_dir="output/gemma-lora-finetuned",  # Output directory for fine-tuned model
)

# Start fine-tuning
trainer.train()

# Save the fine-tuned model
trainer.save_model()

print("Fine-tuning complete! Model saved in 'output/gemma-lora-finetuned'")
