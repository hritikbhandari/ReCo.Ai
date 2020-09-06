from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers.core import Dense, Dropout
from keras.models import load_model
import os

# Create flask instance
app = Flask(__name__)

def init():
    global model
    model = load_model('model.h5')
    #graph = tf.get_default_graph()


@app.route('/', methods=['GET', 'POST'])
def home():
    
    return render_template("home.html")

@app.route('/predict', methods = ['POST'])
def predict():


     float_features = [float(x) for x in request.form.values()]
     final_features = [np.array(float_features)]
   
     class_prediction = model.predict(final_features)
     
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

     return render_template('home.html', prediction_text='The Activity of Human {}'.format(product))


if __name__ == "__main__":
    app.run(debug=True)