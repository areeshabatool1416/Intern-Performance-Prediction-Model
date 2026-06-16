# Intern Performance Prediction Model
## Project Overview

This project predicts intern performance using Machine Learning based on:

• Completion Time

• Feedback Rating

• Attendance

The goal is to identify whether an intern is likely to excel, perform average, or struggle.

## Dataset

The dataset contains the following features:

| Feature | Description |
|---------|-------------|
| Completion_Time | Time taken to complete tasks |
| Feedback_Rating | Supervisor feedback |
| Attendance | Attendance percentage |
| Performance_Score | Target Variable |

##  Exploratory Data Analysis

The following analyses were performed:

- Missing Value Analysis
- Histograms
- Boxplots
- Outlier Detection
- Correlation Analysis

## Models Used

### Random Forest Regressor

An ensemble learning algorithm that builds multiple independent trees and averages their predictions.

### XGBoost Regressor

A boosting algorithm where each new tree learns from previous errors.

## Results

### Random Forest

- MAE: 7.85
- RMSE: 9.81
- R² Score: 0.57


### XGBoost

- MAE: 7.35
- RMSE: 9.16
- R² Score: 0.62


XGBoost performed better than Random Forest.

## Live Demo

Try the application here:

https://intern-performance-prediction-model-c2xmyp3zcstwvtxutgmneq.streamlit.app/

##  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost
- Streamlit
- Joblib

## Author

Areesha Batool

Computer Science Student

Machine Learning Enthusiast






