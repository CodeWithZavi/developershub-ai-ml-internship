# DevelopersHub Corporation - AI/ML Engineering Internship

**Internship Period:** June 2026  
**Due Date:** 26th June, 2026  
**Requirement:** Complete at least 3 out of 6 tasks

## Repository Structure

```
developershub-ai-ml-internship/
├── README.md                          # This file
├── task1-iris-exploration/            # Task 1: Exploring and Visualizing Iris Dataset
│   ├── notebooks/
│   │   └── iris_exploration.ipynb
│   ├── README.md
│   └── requirements.txt
├── task2-stock-prediction/            # Task 2: Stock Price Prediction
│   ├── notebooks/
│   │   └── stock_price_prediction.ipynb
│   ├── README.md
│   └── requirements.txt
├── task3-heart-disease/               # Task 3: Heart Disease Prediction
│   ├── notebooks/
│   │   └── heart_disease_prediction.ipynb
│   ├── README.md
│   └── requirements.txt
├── task4-health-chatbot/              # Task 4: General Health Query Chatbot
│   ├── notebooks/
│   │   └── health_chatbot.ipynb
│   ├── README.md
│   └── requirements.txt
├── task5-mental-health-chatbot/       # Task 5: Mental Health Support Chatbot
│   ├── notebooks/
│   │   └── mental_health_chatbot.ipynb
│   ├── README.md
│   └── requirements.txt
└── task6-house-price-prediction/      # Task 6: House Price Prediction
    ├── notebooks/
    │   └── house_price_prediction.ipynb
    ├── README.md
    └── requirements.txt
```

## Tasks Overview

| Task | Title | Type | Status |
|------|-------|------|--------|
| 1 | Exploring and Visualizing a Simple Dataset (Iris) | Data Exploration & Visualization | ✅ Complete |
| 2 | Predict Future Stock Prices (Short-Term) | Time Series Regression | ✅ Complete |
| 3 | Heart Disease Prediction | Binary Classification | ✅ Complete |
| 4 | General Health Query Chatbot | Prompt Engineering / LLM API | ✅ Complete |
| 5 | Mental Health Support Chatbot | Fine-tuning LLM | ✅ Complete |
| 6 | House Price Prediction | Regression | ✅ Complete |

## Completed Tasks (6/6 All Tasks Done)

### Task 1: Iris Dataset Exploration
- **Objective:** Load, inspect, and visualize the Iris dataset
- **Dataset:** Iris Dataset (via seaborn)
- **Skills:** pandas, matplotlib, seaborn, data visualization
- **Key Visualizations:** Scatter plots, histograms, box plots, pair plots

### Task 2: Stock Price Prediction
- **Objective:** Predict next day's closing price using historical data
- **Dataset:** Yahoo Finance (via yfinance) - Apple (AAPL)
- **Models:** Linear Regression, Random Forest Regressor
- **Skills:** Time series handling, regression modeling, API data fetching
- **Evaluation:** MAE, RMSE, Actual vs Predicted plots

### Task 3: Heart Disease Prediction
- **Objective:** Predict heart disease risk from health data
- **Dataset:** UCI Heart Disease Dataset (Kaggle)
- **Models:** Logistic Regression, Decision Tree Classifier
- **Skills:** Binary classification, EDA, ROC-AUC, confusion matrix, feature importance
- **Evaluation:** Accuracy, Precision, Recall, F1-Score, ROC Curve

### Task 4: General Health Query Chatbot
- **Objective:** Prompt-engineered chatbot answering health questions via LLM
- **Models:** Mistral-7B-Instruct (Hugging Face) / GPT-3.5 (OpenAI)
- **Skills:** Prompt engineering, LLM APIs, safety filtering, conversational AI
- **Safety:** Emergency keyword detection, disclaimers, medication guardrails

### Task 5: Mental Health Support Chatbot
- **Objective:** Fine-tuned empathetic chatbot for emotional wellness support
- **Base Model:** DistilGPT2 (82M params), fine-tuned on EmpatheticDialogues
- **Skills:** Fine-tuning with HF Trainer, causal LM, emotional dialogue modeling
- **Interface:** CLI chatbot with crisis detection safeguards

### Task 6: House Price Prediction
- **Objective:** Predict house prices from property features
- **Models:** Ridge Regression, Gradient Boosting Regressor
- **Skills:** Feature engineering, regression, MAE/RMSE evaluation
- **Evaluation:** MAE, RMSE, R² Score, Residual Analysis

## Quick Start

### Prerequisites
```bash
python >= 3.8
pip install -r requirements.txt  # In each task directory
```

### Running Notebooks
```bash
# Navigate to any task directory
cd task1-iris-exploration

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook notebooks/iris_exploration.ipynb
```

## Submission Checklist (Per Task)

- [x] Jupyter Notebook with complete analysis
- [x] Clear problem statement and goal
- [x] Dataset loading and preprocessing
- [x] Data visualization and exploration
- [x] Model training and evaluation
- [x] Explanation of results and final insights
- [x] Clean, modular, commented code
- [x] README.md with task summary
- [x] GitHub repository with all files

## Technologies Used

- **Python 3.8+**
- **Data Science:** pandas, numpy, scikit-learn
- **Visualization:** matplotlib, seaborn, plotly
- **Time Series:** yfinance
- **ML Models:** Linear Regression, Random Forest, Logistic Regression, Decision Tree, Ridge, Gradient Boosting
- **Deep Learning:** DistilGPT2, Hugging Face Transformers, Trainer API
- **LLM / Prompt Engineering:** Mistral-7B-Instruct, GPT-3.5, Hugging Face Inference API
- **Evaluation:** MAE, RMSE, R², Accuracy, ROC-AUC, Confusion Matrix, Precision, Recall, F1-Score

## Author

DevelopersHub Corporation AI/ML Engineering Intern

## License

This project is for educational purposes as part of the DevelopersHub Corporation Internship Program.