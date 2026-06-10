# Task 4: General Health Query Chatbot (Prompt Engineering)

## Objective
Build a chatbot that answers general health-related questions using an LLM via prompt engineering, with safety filters to avoid harmful medical advice.

## Approach
- Uses Hugging Face's free inference API (Mistral-7B-Instruct) or OpenAI API
- Prompt engineering: System prompt sets the AI as a helpful medical assistant
- Safety filters: Disclaimers and guardrails for potentially harmful queries

## Example Queries
- "What causes a sore throat?"
- "Is paracetamol safe for children?"
- "How can I reduce stress?"

## Safety Features
- Clear disclaimer that this is not medical advice
- Queries about emergencies redirect to seek professional help
- Medication dosage questions recommend consulting a doctor

## Requirements
```
transformers torch requests python-dotenv jupyter
```
Optional: `openai` for GPT-3.5/4

## Run
```bash
pip install -r requirements.txt
jupyter notebook notebooks/health_chatbot.ipynb
```