from flask import Flask, render_template, request, redirect, url_for, session
import re

app = Flask(__name__, template_folder='templates')
@app.route('/')
def home():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
   app.run(debug=True)
