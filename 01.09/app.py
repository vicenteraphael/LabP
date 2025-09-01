from flask import Flask, render_template, jsonify

app = Flask(__name__)

dados_biografia = {
    "santos_dumont": {
            "nome": "Santos Dumont",
            "texto": "Alberto Santos de Dumont foi um aronauta, esportista e inventor brasileiro..."
        },
    "maria_curie": {
        "nome" : "Maria Curiê",
        "texto" : "Maria Curiê foi uma física e química polonesa naturalizada francesa..."
    },
    "albert_einstein": {
        "nome" : "Alberto Einstênio",
        "texto" : "Alberto Einstênio foi um físico teórico alemão que desenvolveu a teoria da relatividade geral..."
    }
}

@app.route("/")
def index():
    personagens = dados_biografia.keys()
    return render_template('index.html', personagens=personagens, nomes=dados_biografia)

@app.route("/biografia/<id_personagem>")
def get_biografia(id_personagem):
    biografia_data = dados_biografia.get(id_personagem, {
        "nome" : "Desconhecido.",
        "texto" : "Personagem não encontrado."
    })
    return jsonify(biografia_data)

if __name__ == "__main__":
    app.run(debug=True)