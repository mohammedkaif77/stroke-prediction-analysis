
# 🩺 Stroke Prediction Data Analysis

## 📌 Problem Statement
Analyze patient health data to identify the major factors that increase the risk of stroke.

---

## 🧠 Dataset Overview
- **Source:** [Kaggle Stroke Prediction Dataset](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset) (~5,000 patient records)  
- **Features:**  
  `age`, `gender`, `hypertension`, `heart_disease`, `avg_glucose_level`, `bmi`, `smoking_status`  
- **Target Variable:**  
  `stroke` → (1 = Stroke, 0 = No Stroke)

---

## 🧹 Data Cleaning
- Removed duplicate rows and handled missing values.  
- Replaced missing or invalid **BMI** values with median values.  
- Standardized categorical variables (`gender`, `smoking_status`).  
- Added derived columns such as **age_group** for better visualization.  
- Saved cleaned data as `cleaned_stroke.csv`.

---

## 📊 Exploratory Data Analysis (EDA)
Performed detailed analysis using **Pandas**, **Matplotlib**, and **Seaborn**.

### Key EDA Steps:
- Distribution plots for **Age**, **Glucose**, and **BMI**.  
- Countplots for categorical variables like **Smoking Status**, **Hypertension**, and **Heart Disease**.  
- Correlation heatmap for numerical features.  
- Stroke rate analysis by **Age Group**, **Smoking Status**, and **Hypertension**.

---

## 🖼️ Visualizations
- **Age vs Stroke Rate:** Stroke risk increases sharply after 60 years.  
- **Glucose & BMI Comparison:** Higher glucose and BMI are linked to stroke.  
- **Smoking Status:** Smokers show greater stroke incidence.  
- **Heatmap:** Revealed positive correlation between stroke, glucose level, and hypertension.

All generated plots are saved under:  
`/outputs/figures/`

---

## 🧮 SQL Analysis
Performed aggregation queries using **SQLite3** to summarize patterns in the dataset.

### Sample Queries:
```sql
-- 1. Count of patients by outcome
SELECT stroke, COUNT(*) AS num_patients
FROM stroke
GROUP BY stroke;

-- 2. Average glucose level by smoking status
SELECT smoking_status, ROUND(AVG(avg_glucose_level),2) AS avg_glucose
FROM stroke
GROUP BY smoking_status
ORDER BY avg_glucose DESC;

-- 3. Stroke rate by age group
SELECT age_group,
       COUNT(*) AS total,
       SUM(CASE WHEN stroke=1 THEN 1 ELSE 0 END) AS strokes,
       ROUND(100.0 * SUM(CASE WHEN stroke=1 THEN 1 ELSE 0 END) / COUNT(*),2) AS stroke_rate_pct
FROM stroke
GROUP BY age_group
ORDER BY stroke_rate_pct DESC;
````

---

## 💡 Key Insights

* Stroke risk **rises significantly after age 60**.
* **Higher glucose** and **higher BMI** correlate strongly with stroke incidence.
* **Hypertension** and **smoking** are major risk factors.
* **Heart disease** also increases stroke likelihood, though it may co-occur with hypertension and age.

---

## 🧰 Tools & Libraries Used

| Category      | Tools / Libraries          |
| ------------- | -------------------------- |
| Language      | Python                     |
| Data Handling | Pandas, NumPy              |
| Visualization | Matplotlib, Seaborn        |
| SQL           | SQLite3                    |
| Environment   | Jupyter Notebook / VS Code |

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/stroke-prediction-analysis.git
cd stroke-prediction-analysis
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Place Dataset

Download the Kaggle dataset and place it in the `/data/` folder as `stroke-data.csv`.

### 4️⃣ Run Analysis

```bash
jupyter notebook notebooks/01-data-cleaning.ipynb
jupyter notebook notebooks/02-eda-visualization.ipynb
python src/sql_analysis.py
```

---

## 📈 Results Summary

* Stroke is more frequent among elderly individuals with hypertension or high glucose.
* Lifestyle factors such as smoking contribute notably to risk.
* Visualization and SQL aggregation confirm strong multi-factor relationships.

---

## 🚀 Future Enhancements

* Add **machine learning models** (Logistic Regression, Random Forest) for stroke prediction.
* Apply **SMOTE** or **class weights** to handle class imbalance.
* Use **SHAP** or **LIME** for model explainability.
* Build an **interactive dashboard** (Streamlit / Power BI) for better visualization.

---

## 📎 Requirements

```
pandas
numpy
matplotlib
seaborn
scikit-learn
jupyter
sqlite3   # built-in with Python
```

---

## 📂 Recommended Folder Structure

```
stroke-prediction-analysis/
├── data/
│   ├── stroke-data.csv
│   ├── cleaned_stroke.csv
├── notebooks/
│   ├── 01-data-cleaning.ipynb
│   ├── 02-eda-visualization.ipynb
├── src/
│   ├── data_cleaning.py
│   ├── eda_plots.py
│   ├── sql_analysis.py
├── sql/
│   ├── stroke_queries.sql
├── outputs/
│   ├── figures/
│   ├── reports/
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Author

**Mohammed Kaif**
📧 Email: [kaif09390@gmail.com](mailto:kaif09390@gmail.com)
💼 Role: Data Analyst & AI/ML Enthusiast
🌐 GitHub: [github.com/yourusername](https://github.com/yourusername)
