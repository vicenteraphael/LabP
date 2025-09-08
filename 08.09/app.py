from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = 'uma-chave-secreta-muito-segura'

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
  if request.method == "POST":
    #Em uma aplicação real, aqui ocorreria a validação no back-end
    nome = request.form.get('nome')
    email = request.form.get('email')
    print(f"Dados recebidos do formulário: Nome: {nome}, Email: {email}")
    #Simula uma mesnagem de sucesso:
    flash(f"Obrigado por se cadastrar, {nome}!", "sucess")
    return redirect(url_for('formulario'))
  return render_template('formulario.html')

if __name__ == "__main__":
  app.run(debug=True)