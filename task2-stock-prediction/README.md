# Task 2: Predict Future Stock Prices (Short-Term)

## Objective
Use historical stock data to predict the next day's closing price using regression models.

## Dataset
- **Source:** Yahoo Finance via `yfinance` library
- **Stock:** Apple Inc. (AAPL)
- **Period:** Last 3 years of historical data
- **Features:** Open, High, Low, Volume, Adjusted Close

## Models Used
- **Linear Regression** — Baseline model
- **Random Forest Regressor** — Ensemble method for improved accuracy

## Feature Engineering
- Lag features (previous day's prices)
- Moving averages (7-day, 21-day)
- Price change ratios
- Volume change ratios

## Evaluation Metrics
- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**
- **R² Score**

## Key Results
- Random Forest outperformed Linear Regression
- Predicted prices closely track actual price trends
- Model works best for short-term (next-day) predictions

## Requirements
```
pandas numpy matplotlib seaborn scikit-learn yfinance jupyter
```

## Run
```bash
pip install -r requirements.txt
jupyter notebook notebooks/stock_price_prediction.ipynb
```