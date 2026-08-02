import joblib
import pandas as pd


model = joblib.load("model.pkl")


Hours = float(input("Study hours per day: "))
Attendance = float(input("Attendance percentage: "))
Score = float(input("Previous exam score: "))
Sleep = float(input("Sleep hours per day: "))
Questions = int(input("Practice questions completed: "))




if Hours < 0 or Hours > 24:
    print("Invalid study hours.")
    exit()

if Attendance < 0 or Attendance > 100:
    print("Attendance must be between 0 and 100.")
    exit()

if Score < 0 or Score > 100:
    print("Previous score must be between 0 and 100.")
    exit()

if Sleep < 0 or Sleep > 24:
    print("Invalid sleep hours.")
    exit()

if Questions < 0:
    print("Practice questions cannot be negative.")
    exit()


student = pd.DataFrame({
    "Hours": [Hours  ],
    "Attendance": [Attendance],
    "Score": [Score],
    "Sleep": [Sleep],
    "Questions": [Questions]
})


prediction = model.predict(student)

predicted_score = prediction[0]

predicted_score = max(0, min(100, predicted_score))


if predicted_score >= 90:
    performance = "Excellent"

elif predicted_score >= 75:
    performance = "Good"

elif predicted_score >= 60:
    performance = "Average"

else:
    performance = "Needs Improvement"

print("\nPredicted Final Score:", (predicted_score))
print("Performance:", performance)