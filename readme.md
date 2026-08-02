# 🎓 Student Performance Predictor

A Machine Learning web application that predicts a student's final academic score based on study habits and academic factors.

The project uses **Linear Regression** for prediction and **Flask** to provide a simple web interface.

## 🚀 Features

- Predicts a student's final score
- Classifies performance as:
  - Excellent
  - Good
  - Average
  - Needs Improvement
- Validates user input
- Displays prediction through a web interface
- Uses a trained Machine Learning model
- Evaluates the model using MAE and R² Score

## 🧠 Machine Learning Model

The project uses **Linear Regression** from Scikit-learn.

The model considers the following features:

| Feature | Description |
|---|---|
| Hours | Study hours per day |
| Attendance | Attendance percentage |
| Score | Previous exam score |
| Sleep | Sleep hours per day |
| Questions | Number of practice questions completed |

The model predicts:

**Final Score**

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn
- Joblib
- HTML
- CSS
- Machine Learning

## 📁 Project Structure

```text
student-performance-predictor/
│
├── data/
│   └── students.csv
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── model.pkl
├── train.py
├── predict.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/student-performance-predictor.git
```

Move into the project directory:

```bash
cd student-performance-predictor
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🧪 Train the Model

Run the training script:

```bash
python train.py
```

The script:

1. Loads the student dataset
2. Separates features and target
3. Splits the data into training and testing sets
4. Trains a Linear Regression model
5. Evaluates the model using MAE and R²
6. Saves the trained model as `model.pkl`

## 💻 Test from the Terminal

You can test the trained model without starting Flask:

```bash
python predict.py
```

Enter values such as:

```text
Study hours per day: 8
Attendance percentage: 90
Previous exam score: 85
Sleep hours per day: 8
Practice questions completed: 80
```

The program will display the predicted final score and performance category.

## 🌐 Run the Flask Application

Start the development server:

```bash
python app.py
```

Then open the local address displayed in your terminal, usually:

```text
http://127.0.0.1:5000
```

Enter the student's details and click the prediction button to get the predicted final score.

## 📊 Performance Categories

| Predicted Score | Performance |
|---:|---|
| 90–100 | Excellent |
| 75–89.99 | Good |
| 60–74.99 | Average |
| Below 60 | Needs Improvement |

## 🔄 Application Workflow

```text
Student Dataset
      ↓
Data Preprocessing
      ↓
Train/Test Split
      ↓
Linear Regression
      ↓
Model Evaluation
      ↓
model.pkl
      ↓
Flask Application
      ↓
Student Input
      ↓
Predicted Final Score
```

## 📌 Future Improvements

- Add more training data
- Experiment with Random Forest and other regression models
- Compare multiple ML algorithms
- Add prediction visualizations
- Store prediction history in a database
- Deploy the application online
- Improve model accuracy with feature engineering

## 👨‍💻 Author

**Satya**

B.Tech Student | Python | Machine Learning | Web Development

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐.