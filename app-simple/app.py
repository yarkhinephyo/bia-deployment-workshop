from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello')
def hello():
  return "Hello world"

@app.route('/bia')
def bia():
  return "I <3 BIA"

@app.route('/page')
def page():
  return render_template("hello-world.html")

@app.route('/myname')
def myname():
  name = request.args.get("name")
  return jsonify({"My reply": f"My name is {name}"})

@app.route('/add')
def add():
  try:
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))

    return jsonify({"answer": f"{num1} + {num2} = {num1 + num2}"})
  except Exception as e:
    return jsonify({"exception": str(e)})

if __name__ == "__main__":
  app.run()
