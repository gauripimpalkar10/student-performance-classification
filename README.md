# Student Performance Classification

## 📌 Project Overview

This mini project uses Machine Learning to classify students as **Pass or Fail** based on their academic and attendance-related factors.

## 🎯 Problem Statement

The objective is to build a classification model that predicts whether a student will pass or fail using factors such as study hours, attendance, previous performance, and subject scores.

## 📊 Dataset

The dataset contains student information including:

- Study Hours Per Day
- Attendance Percentage
- Previous Year Score
- Math Score
- Science Score
- English Score
- Pass/Fail status

## 🤖 Machine Learning Model

The project uses a **Decision Tree Classifier** for predicting student performance.

### Features Used

- `Study_Hours_Per_Day`
- `Attendance_Percentage`
- `Previous_Year_Score`
- `Math_Score`
- `Science_Score`
- `English_Score`

### Target Variable

- `Pass_Fail`

## ⚙️ Project Workflow

1. Load the dataset
2. Inspect the data
3. Check for missing values
4. Select relevant features
5. Split data into training and testing sets
6. Train the Decision Tree Classifier
7. Predict student results
8. Evaluate the model
9. Analyze the confusion matrix

## 📈 Model Evaluation

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook / VS Code

## 📁 Project Structure

```text
ML.mini/
│
├── Student_Performance_Dataset.csv
├── student_performance.py
└── README.md