#projetado em 16/06
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home(logado):
    produtos = ['Maçã', 'Banana', 'Laranja']
    return render_template('home.html', produtos=produtos, logado=logado)

if __name__ == '__main__':
    app.run(debug=True)