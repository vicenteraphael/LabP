#projetado em 16/06
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Olá, Mundo!"

if __name__ == "__main__":
    app.run(debug=True)