# 🚀 Predictive Maintenance AI
### Intelligent Machine Failure Prediction Using Machine Learning

An end-to-end Machine Learning project that analyzes industrial machine sensor data to predict potential equipment failures and support proactive maintenance decisions.

## 📌 Project Overview

Unexpected equipment failures can lead to production downtime, increased maintenance costs, and operational inefficiencies in industrial environments.

**Predictive Maintenance AI** aims to address this challenge by leveraging machine learning algorithms to analyze machine operating conditions and predict potential failures.

This project combines data analysis, machine learning model development, model evaluation, and an interactive Streamlit application to demonstrate how AI can support smarter industrial maintenance decisions.

## 🌐 Live Application

**Try the Predictive Maintenance AI application here:**

https://predictive-maintenance-ai-gxxcuycp9nbvfr2xndyjxv.streamlit.app/

Explore the application by entering machine operating parameters and generating machine failure predictions.

## 🎯 Business Problem

Traditional maintenance approaches often depend on fixed maintenance schedules or respond only after equipment failures occur.

This can result in:
- Unplanned production downtime
- Increased maintenance expenses
- Equipment performance issues
- Reduced operational efficiency

**Our Approach:** Use historical machine sensor data to identify failure patterns and predict potential machine failures before they occur.

## 🎯 Project Objectives

- Explore and understand industrial machine sensor data.
- Perform data cleaning and preprocessing.
- Identify patterns and relationships between machine parameters and failures.
- Develop and compare Machine Learning classification models.
- Evaluate model performance using appropriate metrics.
- Build an interactive application for machine failure prediction.

The dataset is used to understand machine operating conditions and identify patterns associated with equipment failure.

## 🤖 Machine Learning Approach

Two classification algorithms were developed and compared:

**1. Decision Tree Classifier**
- Learns decision rules from machine operating parameters.
- Provides an interpretable classification approach.

**2. Random Forest Classifier**
- Uses multiple decision trees to generate predictions.
- Helps capture complex relationships within the dataset.
- Selected as the prediction model used in the Streamlit application.

Model evaluation includes classification metrics such as accuracy, precision, recall, F1-score, and confusion matrix.

## ⚙️ Project Workflow

1. **Data Understanding** – Explore dataset structure, features, and target variable.
2. **Exploratory Data Analysis** – Analyze distributions, patterns, and relationships.
3. **Data Preprocessing** – Prepare the dataset for machine learning.
4. **Model Development** – Train Decision Tree and Random Forest classifiers.
5. **Model Comparison** – Evaluate and compare classification performance.
6. **Model Saving** – Save the trained model using Joblib.
7. **Application Development** – Build an interactive Streamlit interface.
8. **Prediction** – Accept machine parameters and generate failure predictions.

## 🖥️ Interactive Web Application

The project includes a Streamlit-based application that allows users to enter machine operating parameters and generate predictions using the trained Random Forest model.

**Application Features**
- Interactive machine parameter inputs.
- Trained model integration.
- Real-time prediction based on submitted inputs.
- Clear machine failure prediction output.
- Cached model loading for improved application efficiency.

**Prediction Results:**
- Machine Failure Predicted
- No Machine Failure Predicted

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Directory

```bash
cd Predictive-Maintenance-AI
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Launch the Streamlit Application

```bash
streamlit run app_work/app.py
```

Open the local URL displayed in the terminal to access the application.

## 📈 Project Outcome

Successfully developed an end-to-end machine learning workflow for industrial machine failure prediction.

The project demonstrates practical implementation of:
- Data analysis and preprocessing
- Supervised machine learning
- Classification model comparison
- Model persistence and integration
- Interactive AI application development

It provides a practical demonstration of how machine learning can be applied to industrial predictive maintenance use cases.

## 🔮 Future Enhancements

- Cloud deployment for public application access.
- Advanced model optimization and evaluation.
- Prediction history and monitoring dashboard.
- Integration with real-time IoT sensor data.
- Improved failure risk analysis.

## 👨‍💻 Author

**Jeevagan K.**

Computer Science and Engineering Graduate | Aspiring AI Engineer

Interested in Artificial Intelligence, Machine Learning, Data Analytics, and solving real-world problems through technology.

---
