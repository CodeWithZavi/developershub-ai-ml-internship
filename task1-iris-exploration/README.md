# Task 1: Exploring and Visualizing the Iris Dataset

## Objective
Load, inspect, and visualize the classic Iris dataset to understand data trends, feature distributions, and relationships between variables.

## Dataset
- **Name:** Iris Dataset (Fisher's Iris)
- **Source:** Built-in via seaborn (`seaborn.load_dataset('iris')`)
- **Records:** 150 samples, 4 features
- **Classes:** Setosa, Versicolor, Virginica (50 each)
- **Features:** Sepal Length, Sepal Width, Petal Length, Petal Width

## Visualizations
- Scatter plots (feature relationships)
- Histograms (value distributions)
- Box plots (outlier detection)
- Pair plots (multi-feature relationships)
- Correlation heatmap

## Key Findings
- Petal length and petal width are highly correlated
- Setosa is easily separable from the other two species
- Virginica has the largest petal dimensions
- Minimal outliers detected in the dataset

## Requirements
```
pandas
numpy
matplotlib
seaborn
scikit-learn
jupyter
```

## Run
```bash
pip install -r requirements.txt
jupyter notebook notebooks/iris_exploration.ipynb
```