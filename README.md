<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=35&duration=3000&pause=1000&color=6C63FF&center=true&vCenter=true&width=600&lines=%F0%9F%A4%96+AI%2FML+Engineering+Internship;%F0%9F%94%A5+6+Tasks+%7C+100%25+Complete;%F0%9F%8F%86+DevelopersHub+Corporation" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Internship-June%202026-blueviolet?style=for-the-badge&logo=googlecalendar" />
  <img src="https://img.shields.io/badge/Status-100%25%20Complete-success?style=for-the-badge&logo=checkmarx" />
  <img src="https://img.shields.io/badge/Python-3.8%2B-yellow?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Due-26th%20June-ff6b6b?style=for-the-badge&logo=clock" />
</p>

<br />

<p align="center">
  <i>Where raw data meets intelligence. Six real-world problems, one journey from intern to ML engineer.</i>
</p>

<br />

---

## 📊 The Mission

| # | Task | Difficulty | Type | Status |
|:--:|------|:----------:|------|:------:|
| 🌸 | **Iris Dataset Exploration** | `Easy` | Data Viz & EDA | ✅ |
| 📈 | **Stock Price Prediction** | `Medium` | Time Series Regression | ✅ |
| 💓 | **Heart Disease Prediction** | `Medium` | Binary Classification | ✅ |
| 🩺 | **General Health Chatbot** | `Hard` | Prompt Engineering + LLM | ✅ |
| 🧠 | **Mental Health Support Chatbot** | `Hard` | Fine-Tuning LLM | ✅ |
| 🏠 | **House Price Prediction** | `Medium` | Regression | ✅ |

<p align="center">
  <b>🏆 All 6 tasks crushed. 0 excuses.</b>
</p>

---

## 🧬 Tech DNA

<p align="center">
  <img src="https://img.shields.io/badge/pandas-black?style=flat-square&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/numpy-013243?style=flat-square&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Seaborn-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" />
  <img src="https://img.shields.io/badge/Transformers-FFD21E?style=flat-square&logo=huggingface&logoColor=black" />
  <img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white" />
  <img src="https://img.shields.io/badge/yfinance-00A86B?style=flat-square&logo=yahoo&logoColor=white" />
</p>

```
┌─────────────────────────────────────────────────────────────┐
│  📊 DATA         │  🤖 MODELS              │  📐 EVALUATION │
│─────────────────────────────────────────────────────────────│
│  pandas          │  Linear Regression       │  MAE          │
│  numpy           │  Random Forest           │  RMSE         │
│  matplotlib      │  Logistic Regression     │  R² Score     │
│  seaborn         │  Decision Tree           │  Accuracy     │
│  yfinance        │  Ridge Regression        │  ROC-AUC      │
│  HuggingFace DSL │  Gradient Boosting       │  F1-Score     │
│                  │  DistilGPT2 (Fine-tuned)  │  Precision    │
│                  │  Mistral-7B-Instruct     │  Recall       │
│                  │  GPT-3.5 (OpenAI)        │               │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

```bash
# Clone and dive in
git clone <this-repo>
cd developershub-ai-ml-internship

# Pick a task, any task!
cd task1-iris-exploration
pip install -r requirements.txt
jupyter notebook notebooks/iris_exploration.ipynb
```

---

## 🔮 Task Deep Dive

<details>
<summary><b>🌸 Task 1 — Iris Dataset Exploration</b></summary>
<br />

> *"Every data story begins with a scatter plot."*

- **Dataset:** Iris (Fisher, 1936) — the Hello World of ML
- **Vibe:** Exploratory Data Analysis — distributions, correlations, outlier hunting
- **Visuals:** Pair plots, box plots, histograms, KDE distributions
- **Verdict:** The iris still teaches us more than any textbook ever could.

| 📦 pandas | 🎨 matplotlib | 🖼️ seaborn |
</details>

<details>
<summary><b>📈 Task 2 — Stock Price Prediction</b></summary>
<br />

> *"Past prices, future predictions. Time is the only dimension that matters."*

- **Dataset:** AAPL (Apple Inc.) — live from Yahoo Finance via `yfinance`
- **Approach:** Engineered lag features, rolling windows, technical indicators
- **Models:** Linear Regression (baseline) → Random Forest Regressor
- **Metrics:** MAE, RMSE, side-by-side Actual vs. Predicted showdown

| 📈 yfinance | 🌲 Random Forest | ⏱️ Time Series |
</details>

<details>
<summary><b>💓 Task 3 — Heart Disease Prediction</b></summary>
<br />

> *"14 features. One binary outcome. A life on the line."*

- **Dataset:** UCI Heart Disease (Cleveland) — 303 patients, 76 attributes
- **Target:** Presence or absence of heart disease
- **Models:** Logistic Regression vs. Decision Tree — who wins?
- **Report Card:** Accuracy, Precision, Recall, F1, ROC-AUC, confusion matrix

| ⚕️ Medical ML | 📊 Classification | 🎯 ROC-AUC |
</details>

<details>
<summary><b>🩺 Task 4 — General Health Chatbot</b></summary>
<br />

> *"Your AI doctor is in. Prompt carefully."*

- **Engine:** Mistral-7B-Instruct via Hugging Face Inference API (+ GPT-3.5 fallback)
- **Craft:** Precision prompt engineering — role-setting, safety layers, emergency keyword detection
- **Guardrails:** Medical disclaimers, medication refusal, crisis routing
- **Deliverable:** A conversational health assistant that knows its limits

| 🤗 Hugging Face | 🧪 Prompt Engineering | 🛡️ Safety-First |
</details>

<details>
<summary><b>🧠 Task 5 — Mental Health Support Chatbot</b></summary>
<br />

> *"Fine-tuning empathy. The model that listens."*

- **Base Model:** DistilGPT2 (82M params)
- **Dataset:** EmpatheticDialogues — 25k conversations across 32 emotion labels
- **Training:** Hugging Face Trainer API, causal language modeling objective
- **Interface:** CLI chatbot with real-time crisis detection & resource signposting

| 🎯 Fine-Tuning | 💬 Conversational AI | 🧘 Emotional Intelligence |
</details>

<details>
<summary><b>🏠 Task 6 — House Price Prediction</b></summary>
<br />

> *"Location, location, regression."*

- **Objective:** Predict sale prices from 80+ property features
- **Pipeline:** Handle missing data, encode categoricals, scale numerics, engineer interaction terms
- **Models:** Ridge Regression (L2 regularization) vs. Gradient Boosting Regressor
- **Diagnostics:** MAE, RMSE, R², residual plots, feature importance ranking

| 🏗️ Feature Engineering | 📉 Gradient Boosting | 🎯 R² Score |
</details>

---

## 📂 Repository Anatomy

```
developershub-ai-ml-internship/
│
├── 📓 task1-iris-exploration/          EDA on the classic Iris dataset
├── 📓 task2-stock-prediction/          AAPL price forecasting
├── 📓 task3-heart-disease/             Binary classification for heart health
├── 📓 task4-health-chatbot/            Prompt-engineered medical chatbot
├── 📓 task5-mental-health-chatbot/     Fine-tuned empathetic AI companion
├── 📓 task6-house-price-prediction/    Regression on property valuation
│
├── 📄 requirements.txt                 Global deps (pandas, torch, transformers...)
└── 📄 README.md                        You are here. 👋
```

---

## 🎓 What I Learned

```diff
+ Data doesn't speak — you ask the right questions
+ A baseline model beats no model. Always ship the simple version first.
+ Prompt engineering is programming. Every word in the system prompt matters.
+ Fine-tuning an LLM is equal parts art, science, and patience.
+ Safety guardrails in health chatbots aren't optional — they're the product.
+ Feature engineering > model selection. Garbage features → garbage predictions.
- Overthinking. Just run the notebook.
```

---

## 🤝 Connect

<p align="center">
  <a href="mailto:nomanshaker2@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-nomanshaker2%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
  <a href="https://github.com/CodeWithZavi">
    <img src="https://img.shields.io/badge/GitHub-CodeWithZavi-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</p>

<p align="center">
  <b>📬 nomanshaker2@gmail.com</b> &nbsp;&nbsp;|&nbsp;&nbsp; <b>🐙 CodeWithZavi</b>
</p>

<br />

---

<p align="center">
  <b>⚡ Built with caffeine, code, and conviction.</b><br />
  <i>DevelopersHub Corporation · AI/ML Engineering Internship · June 2026</i>
</p>

<p align="center">
  <sub>🎓 Internship complete. The real learning starts now.</sub>
</p>
