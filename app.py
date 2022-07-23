from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
    {
        "inputs": 5,
        "category": "Sports",
        "word": "Chess"
    },
    {
        "inputs": 6,
        "category": "European Country Name",
        "word": "France"
    },
    {
        "inputs": 12,
        "category": "process converts sugar to acids, alcohol, or gases",
        "word": "Fermentation"
    },
    {
        "inputs": 5,
        "category": "The name for the offspring of a lion and a tigress",
        "word": "Liger"
    },
    {
        "inputs": 7,
        "category": "A Country Known As 'Land Of Thousand Lakes'",
        "word": "Finland"
    },

]

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get-template")
def get_template():
  return jsonify({
        "status": "success",
        "word": random.choice(templates)
  })

if __name__ == '__main__':
  app.run()