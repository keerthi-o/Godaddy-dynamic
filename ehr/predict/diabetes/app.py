from flask import Flask, render_template, request
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('diabetes.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('diabetes.html')



@app.route("/predict", methods=['POST'])
def predict():
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
    if request.method == 'POST':
        Pregnancies = int(request.form['Pregnancies'])
        Glucose=int(request.form['glucose'])
        BloodPressure=int(request.form['BloodPressure'])
        SkinThickness=int(request.form['SkinThickness'])
        Insulin=int(request.form['Insulin'])
        BMI=int(request.form['BMI'])
        DiabetesPedigreeFunction=int(request.form['DiabetesPedigreeFunction'])
        Age=int(request.form['Age'])
        prediction=model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if prediction==0:
            return render_template('diabetes.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('diabetes.html',prediction_text="You Can Sell The Car at ")
    else:
        return render_template('diabetes.html')

if __name__=="__main__":
    app.run(debug=True)