1from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():


    if request.method == "POST":
        error = None
        Hours = float(request.form["Hours"])
        Attendance = float(request.form["Attendance"])
        Score = float(request.form["Score"])
        Sleep = float(request.form["Sleep"])
        Questions = int(request.form["Questions"])



        if Hours < 0 or Hours > 24:
            error = "Study hours must be between 0 and 24."

        elif Attendance < 0 or Attendance > 100:
            error = "Attendance must be between 0 and 100."

        elif Score < 0 or Score > 100:
            error = "Previous score must be between 0 and 100."

        elif Sleep < 0 or Sleep > 24:
            error = "Sleep hours must be between 0 and 24."

        elif Questions < 0:
            error = "Practice questions cannot be negative."

        if error:
            return render_template(
                "index.html",
                error=error
            )


        student = pd.DataFrame({
            "Hours": [Hours],
            "Attendance": [Attendance],
            "Score": [Score],
            "Sleep": [Sleep],
            "Questions": [Questions]
        })


        prediction = model.predict(student)

        predicted_score = prediction[0]

        predicted_score = max(0, min(100, predicted_score))
        predicted_score = round(predicted_score, 2)

        if predicted_score >= 90:
            performance = "Excellent"

        elif predicted_score >= 75:
            performance = "Good"

        elif predicted_score >= 60:
            performance = "Average"

        else:
            performance = "Needs Improvement"
        return render_template(
            "index.html",
            Predict=predicted_score,
            performance=performance
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
