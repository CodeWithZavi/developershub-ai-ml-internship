# Task 6: House Price Prediction

## Objective
Predict house prices using property features such as size, number of bedrooms, and location using regression models.

## Dataset
- **Name:** House Prices - Advanced Regression Techniques
- **Source:** Kaggle
- **Features:** 79 explanatory variables (square footage, bedrooms, year built, location, etc.)
- **Target:** SalePrice (continuous)

## Models Used
- **Linear Regression** — Baseline model with regularization (Ridge/Lasso)
- **Gradient Boosting Regressor** — Advanced ensemble method

## Feature Engineering
- Handling missing values
- Feature scaling and transformation
- Encoding categorical variables
- Feature selection based on correlation

## Evaluation Metrics
- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**
- **R² Score**

## Requirements
```
pandas numpy matplotlib seaborn scikit-learn xgboost jupyter
```

## Run
```bash
pip install -r requirements.txt
jupyter notebook notebooks/house_price_prediction.ipynb
```