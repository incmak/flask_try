from flask import Flask, appcontext_popped, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/hello')
def index():
    flash('Hello World!')
    return render_template('index.html')

@app.route('/greet', methods=['POST', 'GET'])
def greet():
    flash("Hi " + str(request.form['name_input']) + " great to meet you!")
    request.form['name_input']
    return render_template('index.html')