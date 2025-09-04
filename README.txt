# Stroke Prediction Data Analysis

## Problem Statement
Analyze patient health data to identify factors that increase the risk of stroke.

## Dataset
- Source: Kaggle Stroke Prediction Dataset (~5000 patients)
- Features: Age, Gender, Hypertension, Heart Disease, Glucose Level, BMI, Smoking Status
- Target: Stroke (1 = Stroke, 0 = No Stroke)

## Steps
1. Data Cleaning (handled missing values, replaced invalid BMI)
2. EDA (distribution plots, correlations, stroke vs risk factors)
3. Visualization (Age, Glucose, Smoking status, Heatmap)
4. SQL Analysis (patients by outcome, avg glucose by smoking status)
5. Insights:
   - Stroke risk increases after 60 years.
   - Higher glucose and BMI are linked to stroke.
   - Smoking and hypertension are significant risk factors.

## Tools Used
- Python (Pandas, Matplotlib, Seaborn)
- SQL (SQLite)
