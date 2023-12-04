#  Creating an API which will predict the risk of heart attack using our Decision Tree Model
#  Endpoint - http://127.0.0.1:5000/heart-attack-risk Method - POST
#  Payload Sample: {"age": 49.0,  "bmi": 22.515,  "children": 0.0,  "sex_male": 1,  "smoker_yes": 0,  "region_northwest": 0,  "region_southeast": 0,  "region_southwest": 0}
#  Response Sample: 0

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route("/heart-attack-risk", methods=["POST"])
def results():
    print(request)
    data = request.get_json(force=True)
    print(data)
    prediction = model.predict([np.array(list(data.values()))])
    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
