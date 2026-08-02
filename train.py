import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score



data = pd.read_csv("data/students.csv")



X = data[
    [
        "Hours",
        "Attendance",
        "Score",
        "Sleep",
        "Questions"
    ]
]


y = data["Final"]


trainx, testx, trainy, testy = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



model = LinearRegression()



model.fit(trainx, trainy)

print("\nModel training completed!")

print("Training students:", len(trainx))
print("Testing students:", len(testx))



predictions = model.predict(testx   )


# Evaluate model
mae = mean_absolute_error(testy, predictions)
r2 = r2_score(testy, predictions)

print("\nModel Evaluation")
print("----------------")
print("MAE:", round(mae, 2))
print("R² Score:", round(r2, 3))



print("\nModel Coefficients")
print("------------------")

for feature, coefficient in zip(X.columns, model.coef_):
    print(feature, ":", round(coefficient, 3))

print("Intercept:", round(model.intercept_, 3))


joblib.dump(model, "model.pkl")

print("\nModel saved successfully!")