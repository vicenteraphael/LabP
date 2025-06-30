#projetado em 23/06
#atualizado dia 30/06
from flask import Flask, request, render_template, redirect, make_response, url_for

app = Flask(__name__)

users = {"raphael" : "0297",
         "rodrigo": "1546",
         "rogério": "1540"}

@app.route('/')
def view_form():
    return render_template('loginForm.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    mensagem = "Faça login para aproveitar nossos serviços"
    if request.method == 'POST':
        nome = request.form['nome'].lower()
        senha = request.form['senha'].lower()
        if nome in users and users[nome] == senha:
            resposta = make_response(redirect(url_for('home')))
            resposta.set_cookie('username', nome, max_age=60*60*24)
            return resposta
        else:
            mensagem = "Usuário ou senha inválidos. Tente novamente."

    return render_template('loginForm.html', mensagem=mensagem)

@app.route('/home_page')
def home():
    produtos = ['Maçã', 'Banana', 'Laranja']
    username = request.cookies.get('username')
    if username:
        return render_template('home.html', produtos=produtos, usuario=username)
    return render_template('loginForm.html')

@app.route('/logout', methods=['POST'])   
def logout():
    resposta = make_response(redirect(url_for('view_form')))
    if request.method == 'POST':
        resposta = make_response(redirect(url_for('login')))
        resposta.set_cookie('username', '', expires=0)
    return resposta

if __name__ == '__main__':
    app.run(debug=True)