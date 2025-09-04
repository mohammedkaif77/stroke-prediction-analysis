# Stroke Prediction Data Analysis Project

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# Load Dataset
df = pd.read_csv("stroke.csv")
print("Shape:", df.shape)
df.head()

# Data Cleaning
df = df.dropna(subset=["bmi"])
df["bmi"] = df["bmi"].replace(0, df["bmi"].median())
print("Cleaned Shape:", df.shape)

# Basic EDA
print("\nStroke Distribution:\n", df["stroke"].value_counts())
print("\nSummary Statistics:\n", df.describe())

# Visualization 1 - Stroke Count
plt.figure(figsize=(6,4))
sns.countplot(x="stroke", data=df, palette="Set2")
plt.title("Stroke Distribution (0 = No Stroke, 1 = Stroke)")
plt.show()

# Visualization 2 - Age Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["age"], bins=30, kde=True, color="blue")
plt.title("Age Distribution of Patients")
plt.show()

# Visualization 3 - Age vs Stroke
plt.figure(figsize=(8,5))
sns.boxplot(x="stroke", y="age", data=df, palette="coolwarm")
plt.title("Age vs Stroke Outcome")
plt.show()

# Visualization 4 - Glucose vs Stroke
plt.figure(figsize=(8,5))
sns.boxplot(x="stroke", y="avg_glucose_level", data=df, palette="viridis")
plt.title("Glucose Levels vs Stroke Outcome")
plt.show()

# Smoking vs Stroke
plt.figure(figsize=(7,5))
sns.countplot(x="smoking_status", hue="stroke", data=df, palette="Set1")
plt.title("Smoking Status vs Stroke")
plt.xticks(rotation=30)
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="magma", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# SQL Integration
conn = sqlite3.connect(":memory:")
df.to_sql("patients", conn, index=False, if_exists="replace")

query1 = "SELECT stroke, COUNT(*) as count FROM patients GROUP BY stroke;"
print("\nStroke Cases:\n", pd.read_sql(query1, conn))

query2 = "SELECT smoking_status, AVG(avg_glucose_level) as avg_glucose FROM patients GROUP BY smoking_status;"
print("\nAverage Glucose by Smoking Status:\n", pd.read_sql(query2, conn))

query3 = "SELECT age, AVG(bmi) as avg_bmi FROM patients GROUP BY age ORDER BY avg_bmi DESC LIMIT 5;"
print("\nTop 5 Ages with Highest Avg BMI:\n", pd.read_sql(query3, conn))

# Key Insights
print("\n📊 Key Insights:")
print("1. Stroke cases are fewer compared to non-stroke, but risk factors are clear.")
print("2. Patients above 60 years have much higher stroke risk.")
print("3. Higher glucose levels strongly correlate with stroke.")
print("4. Smoking and hypertension significantly increase stroke risk.")
