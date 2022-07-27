from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('rf_reg_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        year = int(request.form['Year'])
        year_used=2022-year
        fuel_type = int(request.form["fuel_type"])
        Kms_Driven=int(request.form['Kms_Driven'])
        Kms_Driven = Kms_Driven/1000
        transmission = int(request.form["transmission"])
        owner=int(request.form["owner"])
        seller_type = int(request.form['seller_type'])
        mileage = float(request.form['mileage'])
        engine = int(request.form['engine'])
        power = float(request.form['max power'])
        seats = int(request.form['seats'])

        prediction=model.predict([[Kms_Driven, fuel_type, transmission, owner,seller_type,mileage, engine,power,seats,year_used]])
        print(prediction)
        output=round(prediction[0],2)
        if output<0:
            return render_template('index2.html',prediction_texts="Sorry the car belongs to scrap")
        else:
            return render_template('index2.html',prediction_text="You Can Sell The Car around {} lac".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)