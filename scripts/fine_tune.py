from transformers import AutoModelForSeq2SeqLM, Trainer, TrainingArguments
import datasets

model_name = "ollama/model-name"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load your dataset
dataset = datasets.load_dataset('your_dataset_name')

# Tokenize your data
tokenized_data = dataset.map(lambda x: tokenizer(x['text'], truncation=True, padding=True), batched=True)

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    per_device_train_batch_size=16,
    num_train_epochs=3,
    save_steps=10_000,
    save_total_limit=2,
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_data["train"],
    eval_dataset=tokenized_data["test"],
)

# Fine-tune the model
trainer.train()
