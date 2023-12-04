#  Creating an API which will predict the risk of heart attack using our Naive Bayes Model
#  Endpoint - http://127.0.0.1:5000/heart-attack-risk Method - POST
#  Payload Sample: {  "age": 43.0,"education": 1.0, "currentSmoker": 1.0, "cigsPerDay": 25.0, "BPMeds": 0.0, "prevalentStroke": 0.0, "prevalentHyp": 0.0, "diabetes": 0.0, "totCholesterol": 201.0, "sysBP": 121.0, "diaBP": 82.0, "BMI": 23.84, "heartRate": 70.0, "glucose": 91.0, "Gender_Male": 1.0 }
#  Response Sample: 0

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
with open('naive_bayes_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route("/heart-attack-risk", methods=["POST"])
def results():
    print(request)
    data = request.get_json(force=True)
    print(data)
    prediction = model.predict([np.array(list(data.values()))])
    output = prediction[0]
    if not output:
        return jsonify({"message": "You don't have heart attack risk "})  
    return jsonify({"message": "Sorry! you have heart attack risk "})  


if __name__ == "__main__":
    app.run(debug=True)
