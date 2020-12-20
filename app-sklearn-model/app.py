from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

import pickle
import sklearn

app = Flask(__name__)
CORS(app)

model = pickle.load(open("simple-model.pkl", "rb"))

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/predict')
def predict():
  try:
    args = request.args

    sepal_length = float(args.get("sepalLength"))
    sepal_width  = float(args.get("sepalWidth"))
    petal_length = float(args.get("petalLength"))
    petal_width  = float(args.get("petalWidth"))

    pred = model.predict([[
      sepal_length,
      sepal_width,
      petal_length,
      petal_width
      ]])

    return jsonify({"message": str(pred[0])})

  except Exception as e:
    return jsonify({"message": str(e)})

if __name__ == "__main__":
  app.run()