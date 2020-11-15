from flask import Flask, jsonify
import pickle
import sklearn

app = Flask(__name__)

@app.route('/')
def hello_world():
  try:
    model = pickle.load(open("simple-model.pkl", "rb"))
    pred = model.predict([[5,4,3,1]])
    print(pred)
    return jsonify({"prediction": "hello world"})
  except Exception as e:
    return jsonify({"exception": str(e)})

if __name__ == "__main__":
  app.run()