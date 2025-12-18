# 🪙 Gold Price Prediction App

This project aims to build a predictive model that accurately forecasts the Gold Price (GLD) using various financial indicators. The goal is to help investors and analysts make informed decisions by understanding the key drivers influencing gold price fluctuations.

## 🔍 Project Objective
Gold is one of the most valuable and volatile commodities in the financial market. This app utilizes historical data and a regression model to predict the price of gold based on macroeconomic features.

## 🚀 Live Demo
https://huggingface.co/spaces/saiteja2001/Gold_Price_Prediction

## 📊 Features Used for Prediction
The model predicts the **Gold Price (GLD)** based on the following indicators:
- **SPX**: S&P 500 Stock Market Index
- **USO**: Crude Oil Prices
- **SLV**: Silver Prices
- **EUR/USD**: Euro to US Dollar Exchange Rate

## 🛠️ Tech Stack
- **Framework**: Streamlit (Web Interface)
- **Machine Learning**: Scikit-learn (KNN Regressor / Pipeline)
- **Data Manipulation**: Pandas, Numpy
- **Visualization**: Plotly, Matplotlib, Seaborn

## 📁 Project Structure
- gold.py: The main Streamlit application script.
- knn_gold1.pkl: The trained KNN regression model saved as a pickle file.
- Regression-Gold.ipynb: Jupyter Notebook containing data cleaning, EDA, and model training logic.
- requirements.txt: List of necessary Python libraries for deployment.

## 📈 Model Information
The model was trained on historical data, undergoing rigorous data cleaning (handling missing values, outliers, and duplicates) and univariate analysis. The final deployment uses a K-Nearest Neighbors (KNN) approach stored within a Scikit-learn pipeline for consistent preprocessing.




