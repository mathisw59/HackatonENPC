from flask import Flask
from flask import request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.post("/prompt")
def return_answer():
    return(jsonify({"answer" : request.form['prompt']}))

@app.get('/prompt')
def maFonction():
    return("<p> Hellow world ! </p>")