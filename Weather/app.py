from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve user inputs from the form
    selected_city = request.form['City']
    sc=str(selected_city)+'.joblib'
    sc1=str(selected_city)+'1.joblib'
    model = joblib.load(sc)
    model1 = joblib.load(sc1)
# Load your trained model using joblib
    MinTemp = float(request.form['MinTemp'])
    MaxTemp = float(request.form['MaxTemp'])
    WindSpeed9am = int(request.form['WindSpeed9am'])
    Humidity9am = int(request.form['Humidity9am'])
    Pressure9am = float(request.form['Pressure9am'])

    # Create a numpy array with the user inputs
    input_data = np.array([[MinTemp, MaxTemp, WindSpeed9am, Humidity9am, Pressure9am]])

    # Make predictions using the loaded model
    predictions = model.predict(input_data)[0]
    predictions1 = model.predict(input_data)[0]
    if predictions==0:
        predictions='No'
    else:
        predictions='Yes'
    if predictions1==0:
        predictions1='No'
    else:
        predictions1='Yes'

    # You can customize this part based on how you want to display the prediction result
    return render_template('result.html', RainToday=predictions, RainTomorrow=predictions1, City=selected_city)

if __name__ == '__main__':
    app.run()
