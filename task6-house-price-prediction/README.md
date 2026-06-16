# Task 6: House Price Prediction

## Objective
Predict house prices using property features such as square footage, bedrooms, build quality, and location from the Kaggle House Prices dataset.

## Dataset
- **Name:** House Prices - Advanced Regression Techniques (Kaggle)
- **Source:** Kaggle (`train.csv` placed locally or in `data/`)
- **Features:** 79 explanatory variables (lot size, living area, build quality, garage, basement, etc.)
- **Target:** SalePrice (log-transformed for better model stability)

## Models Used
- **Ridge Regression** — L2-regularized linear baseline, handles multicollinearity
- **Gradient Boosting Regressor** — Tree-based ensemble capturing non-linear interactions

## Feature Engineering
- Missing value imputation (median for numeric, mode for categorical)
- Label encoding for categorical features
- Log transformation of target (reduces right-skew)
- Derived features: TotalSF, HouseAge, RemodAge
- RobustScaler for outlier-resilient scaling

## Evaluation Metrics
- **Mean Absolute Error (MAE)** in original dollars
- **Root Mean Squared Error (RMSE)** in original dollars
- **R² Score** on log-transformed target
- **Average % Error** relative to mean price
- **Residual Analysis** — scatter plots + distribution histograms

## Requirements
```
pandas numpy matplotlib seaborn scikit-learn jupyter
```

## Setup
1. Download `train.csv` from [Kaggle House Prices](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)
2. Place it in this directory or in `data/train.csv`
3. If no local file found, a fallback synthetic dataset is generated automatically

## Run
```bash
pip install -r requirements.txt
jupyter notebook notebooks/house_price_prediction.ipynb
```