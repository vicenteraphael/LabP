#projetado em 23/06
from flask import Flask, request, render_template
import app3

app = Flask(__name__)

users = {"raphael" : "0297",
         "rodrigo": "1546",
         "rogério": "1540"}

@app.route('/')
def view_form():
    return render_template('loginForm.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        if nome in users and users[nome] == senha:
            return app3.home(True)
        else:
            return app3.home(False)
    else:
        return render_template('loginForm.html')

if __name__ == '__main__':
    app.run(debug=True)