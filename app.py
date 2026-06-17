#
from flask import Flask,render_template,request
import pickle
import numpy as np

#

app = Flask(__name__)


model = pickle.load(open("diabetes_model.sav", "rb"))
scaler = pickle.load(open("scaler.sav", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    preg = float(request.form["preg"])
    glucose = float(request.form["glucose"])
    bp = float(request.form["bp"])
    skin = float(request.form["skin"])
    insulin = float(request.form["insulin"])
    bmi = float(request.form["bmi"])
    dpf = float(request.form["dpf"])
    age = float(request.form["age"])
    # Convert into NumPy Array
    input_data = np.asarray([preg, glucose, bp, skin, insulin, bmi, dpf, age]).reshape(
        1, -1
    )

    # Scale the data
    std_data = scaler.transform(input_data)

    # Predict
    prediction = model.predict(std_data)

    # Result
    if prediction[0] == 1:
        result = "The Person is Diabetic"
    else:
        result = "The Person is Not Diabetic"

    return render_template("index.html", prediction_text=result)


if __name__ == "__main__":
    print("Starting Flask...")
    app.run(debug=True)
