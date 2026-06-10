# Task 3: Heart Disease Prediction

## Objective
Build a classification model to predict whether a person is at risk of heart disease based on their health attributes.

## Dataset
- **Name:** Heart Disease UCI Dataset
- **Source:** Kaggle (UCI Machine Learning Repository)
- **Records:** 303 patients
- **Features:** 14 attributes (age, sex, chest pain type, blood pressure, cholesterol, etc.)
- **Target:** 0 = No heart disease, 1 = Heart disease present

## Models Used
- **Logistic Regression** — Interpretable baseline classifier
- **Decision Tree Classifier** — Rule-based model with feature importance

## Evaluation Metrics
- **Accuracy**, Precision, Recall, F1-Score
- **ROC-AUC Score**
- **Confusion Matrix**
- **Feature Importance Analysis**

## Key Results
- Identified top risk factors for heart disease
- Both models achieve strong classification performance
- Confusion matrix provides clear view of model errors

## Requirements
```
pandas numpy matplotlib seaborn scikit-learn imbalanced-learn jupyter
```

## Run
```bash
pip install -r requirements.txt
jupyter notebook notebooks/heart_disease_prediction.ipynb
```