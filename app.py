from flask import Flask, request, jsonify, render_template
from utils import car_price_prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    print('car price pred')
    data = request.form
    print(data)
    normalizedlosses = float(data['normalizedlosses'][1])
    print("normalizedlosses : ", normalizedlosses)
    wheelbase = float(data['wheelbase'][1])
    width = float(data['width'][1])
    curbweight = float(data['curbweight'][1])
    enginesize = float(data['enginesize'][1])
    horsepower = float(data['horsepower'][1])
    citympg = float(data['citympg'][1])
    highwaympg = float(data['highwaympg'][1])

    # Call your utility function to predict car price
    predicted_price = car_price_prediction(normalizedlosses, wheelbase, width, curbweight, enginesize, horsepower, citympg, highwaympg)
    print(predicted_price)
    return render_template('prediction.html', prediction=predicted_price)

if __name__ == '__main__':
    app.run(debug=False)
