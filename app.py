from flask import Flask, render_template, request,jsonify
import pandas as pd
import numpy as np
import requests
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers.core import Dense, Dropout
from keras.models import load_model
import os

# Create flask instance
app = Flask(__name__,static_folder = 'static')




@app.route('/', methods=['GET', 'POST'])
def home():
    
    return render_template("home.html")

@app.route('/predict', methods = ['POST'])
def predict(final_features):

     
     
   
     class_prediction= model.predict(final_features)
     
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

     return product

@app.route('/result', methods = ['POST'])
def result():
     if request.method == 'POST':
              float_features = [float(x) for x in request.form.values()]
              final_features = [np.array(float_features)]
              result = predict(final_features)

     return render_template('home.html', prediction_text='The Activity of Human {}'.format(result))


if __name__ == "__main__":
    global model
    model = load_model('model.h5')
    app.run(debug=True)