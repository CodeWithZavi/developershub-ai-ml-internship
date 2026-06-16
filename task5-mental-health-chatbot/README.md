# Task 5: Mental Health Support Chatbot (Fine-Tuned)

## Objective
Fine-tune a small language model (DistilGPT2) on empathetic dialogues to create a supportive chatbot for stress, anxiety, and emotional wellness conversations.

## Dataset
- **Name:** EmpatheticDialogues (Facebook AI)
- **Source:** Hugging Face Datasets
- **Description:** 25k+ conversations grounded in emotional situations

## Model
- **Base:** DistilGPT-2 (82M parameters) — lightweight, fast to fine-tune
- **Alternative:** GPT-Neo 125M or Mistral 7B (if resources allow)
- **Fine-tuning:** Hugging Face Trainer API with causal language modeling

## Features
- Emotionally supportive and empathetic responses
- Gentle, non-judgmental tone
- Safety guardrails for crisis situations
- CLI and Streamlit-based interfaces

## Requirements
```
transformers datasets accelerate torch tensorboard streamlit jupyter
```

## Run

### Jupyter Notebook
```bash
pip install -r requirements.txt
jupyter notebook notebooks/mental_health_chatbot.ipynb
```

### Streamlit Web App
After training the model in the notebook, run:
```bash
streamlit run app.py
```