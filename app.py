from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(_name_)
model = pickle.load(open('model.pkl', 'rb'))

education_map = {'High School': 0, 'Bachelor': 1, 'Master': 2}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [
        float(data['experience']),
        education_map[data['education']],
        float(data['evaluation'])
    ]
    prediction = model.predict([features])[0]
    return jsonify({'performance': prediction})

if _name_ == '_main_':
    app.run(port=5000)
