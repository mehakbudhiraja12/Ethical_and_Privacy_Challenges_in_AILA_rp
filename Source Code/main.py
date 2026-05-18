# Ethical and Privacy Challenges in AI-Based Learning Analytics
# Smart Student Monitoring and Privacy Protection System

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Sample student learning analytics dataset
data = {
    'Student_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Study_Hours': [5, 2, 6, 1, 4, 3, 7, 2],
    'Attendance': [90, 60, 95, 50, 80, 70, 98, 55],
    'Assignments_Submitted': [10, 4, 9, 3, 8, 6, 10, 2],
    'Quiz_Score': [85, 40, 92, 35, 76, 60, 95, 30],
    'Final_Result': [1, 0, 1, 0, 1, 0, 1, 0]
}

# Creating DataFrame
df = pd.DataFrame(data)

# ---------------- PRIVACY PROTECTION ----------------

# Anonymizing personal student identity
df['Student_ID'] = 'Anonymous'

print("Privacy-Protected Dataset:\n")
print(df)

# ---------------- AI-BASED ANALYTICS ----------------

# Selecting input features
X = df[['Study_Hours', 'Attendance',
        'Assignments_Submitted', 'Quiz_Score']]

# Target variable
y = df['Final_Result']

# Splitting dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Training Machine Learning model
model = RandomForestClassifier()

model.fit(X_train, y_train)

# Making predictions
predictions = model.predict(X_test)

# Checking model accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nPredicted Results:")
print(predictions)

print("\nModel Accuracy:")
print(accuracy)

# ---------------- ETHICAL MONITORING ----------------

# Detecting students needing academic support
at_risk_students = df[
    (df['Attendance'] < 65) |
    (df['Quiz_Score'] < 40)
]

print("\nStudents Requiring Academic Support:\n")
print(at_risk_students)

# ---------------- DATA SECURITY ----------------

# Saving protected data
df.to_csv("protected_student_data.csv", index=False)

print("\nProtected student data saved securely.")