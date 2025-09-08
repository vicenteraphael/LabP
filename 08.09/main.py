from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route('/area-restrita')
def area_restrita():
  '''
  Em uma aplicação real, aqui você verificaria
  se o usuário está logado.
  Como não temos sistema de login, vamos
  forçar o erro 401 com abort()
  '''
  print('Tentativa de acesso sem autorzação')
  abort(401)

@app.route('/painel-admin')
def painel_admin():
  print ("Tentativa de acesso ao painel de admin sem permissão.")
  abort(403)

@app.errorhandler(404)
def pagina_nao_encontrada(error):
  return render_template('404.html'), 404

@app.errorhandler(401)
def nao_autorizado(error):
  return render_template('401.html'), 401

@app.errorhandler(403)
def acesso_proibido(error):
  return render_template('403.html'), 403

if __name__ == '__main__':
  app.run(debug=True)