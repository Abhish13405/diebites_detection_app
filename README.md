# Diabetes Prediction System

This is a Flask-based Machine Learning project that predicts whether a person is diabetic or not based on medical details.

I created this project while learning Machine Learning and Flask. The model takes health-related information from the user and gives a prediction result on a web page.

## Technologies Used

- Python
- Flask
- NumPy
- Scikit-learn
- HTML
- CSS

## Project Files

```text
app.py                 -> Flask application
diabetes_model.sav     -> Trained ML model
scaler.sav             -> StandardScaler object
templates/index.html   -> Frontend page
static/style.css       -> Styling file
```

## Inputs Used

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

## How to Run

1. Clone the repository

```bash
git clone https://github.com/Abhish13405/diebites_detection_app.git
```

2. Open project folder

```bash
cd diebites_detection_app
```

3. Install required libraries

```bash
pip install flask numpy scikit-learn
```

4. Run the application

```bash
python app.py
```

5. Open browser and visit:

```text
http://127.0.0.1:5000
```

## Output

The application shows one of the following results:

- The Person is Diabetic
- The Person is Not Diabetic

## About This Project

This project was built for practice and learning purposes to understand:

- Machine Learning workflow
- Data preprocessing
- Model deployment using Flask
- Frontend and backend integration

## Author

Abhishek Kushwaha
