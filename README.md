[README.md](https://github.com/user-attachments/files/22391207/README.md)
# n8n Extract Text + Hugging Face NER Demo

This repository demonstrates how to extract text from files in **n8n** and run **Named Entity Recognition (NER)** using Hugging Face.

## 📦 Contents
- `extract_text.py` → Python script for decoding text from binary input (base64).
- `requirements.txt` → Python dependencies.
- `sample_input.json` → Example input.
- `expected_output.json` → Example output with entities.
- `expected_output.csv` → Same output in CSV format.
- `n8n_workflow_ner.json` → Example n8n workflow export.

## 🚀 Setup
1. Clone this repo.
2. Install Python deps:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Hugging Face API key in n8n credentials (or environment):
   ```bash
   export HUGGINGFACE_API_KEY=hf_xxxxxxxx
   ```
4. Import `n8n_workflow_ner.json` into your n8n instance.

## ▶️ Usage
- Run workflow in n8n → extracts text → calls Hugging Face NER → returns JSON with entities.

