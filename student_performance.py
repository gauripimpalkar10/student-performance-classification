import pandas as pd

df = pd.read_csv("Student_Performance_Dataset.csv")

print(df.head())
print(df.info())
print(df.describe())

print(df.isnull().sum())
print(df.columns)

print(df.columns.tolist())

X = df[
    [
        "Study_Hours_Per_Day",
        "Attendance_Percentage",
        "Previous_Year_Score",
        "Math_Score",
        "Science_Score",
        "English_Score"
    ]
]

y = df["Pass_Fail"]

print(X.head())
print(y.head())


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)


from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

print("Model training completed!")


y_pred = model.predict(X_test)

print("Predictions:")
print(y_pred[:20])


from sklearn.metrics import accuracy_score, classification_report

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(cm)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=model.classes_
)

disp.plot(cmap="Blues")
plt.title("Student Performance - Confusion Matrix")
plt.show()


from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=model.classes_,
    filled=True,
    rounded=True,
    max_depth=3
)

plt.title("Decision Tree for Student Performance")
plt.show()


import pickle

with open("student_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")