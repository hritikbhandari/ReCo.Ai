from flask import Flask, render_template, request,jsonify
import requests
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers.core import Dense, Dropout
from keras.models import load_model
import os

# Create flask instance
app = Flask(__name__,static_folder='static')

def init():
    global model
    model = load_model('model.h5')
    


@app.route('/', methods=['GET', 'POST'])
def home():
    
    return render_template("home.html")


@app.route('/predict', methods = ['POST'])
def predict():
    

     #int_features = [int(x) for x in request.form.values()]
     #final_features = [np.array(int_features)]
   
     #class_prediction = model.predict(final_features)
     init()
     class_predicition = model.predict([np.array(list(data.values()))])

     if class_prediction == 0:
           product = "WALKING"
     elif class_prediction == 1:
           product = "WALKING_UPSTAIRS"
     elif class_prediction == 2:
           product = "WALKING_DOWNSTAIRS"
     elif class_prediction == 3:
           product = "SITTING"
     elif class_prediction == 4:
           product = "STANDING"
     elif class_prediction == 5:
           product = "LAYING"

     return render_template('result.html', prediction_text='The Activity of Human {}'.format(product))


'''@app.route('/predict_api',methods=['POST'])
def predict_api():
    
    data = request.get_json(force=True)
    prediction = predict()
    output = prediction[0]
    return jsonify(output)'''

if __name__ == "__main__":
    app.run(debug=True)