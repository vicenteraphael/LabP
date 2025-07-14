from flask import Flask, render_template, request, flash, redirect, url_for, session, make_response

app = Flask(__name__)

app.secret_key = '5051'

user = {
    'rafael@gmail.com' : ['Rafael', '5051'],
    'valter@gmail.com' : ['Valter', '5052']
}

@app.route('/')
def index():
    return redirect(url_for('registrarUsuario'))

@app.route('/registrarUsuario', methods=['GET', 'POST'])
def registrarUsuario():
    session.pop('_flashes', None)
    if request.method == 'POST':
        username = request.form['username'].capitalize()
        email = request.form['email'].lower()
        password = request.form['password']
        if not username or not email or not password:
            flash('Todos os campos são obrigatórios!', 'danger')
        elif not email in user:
            flash('Usuário não encontrado', 'danger')
        elif user[email][0] != username or user[email][1] != password:
            flash('Usuário ou senha incorreto(s)', 'danger')
        else:
            flash(f'Usuário {username} cadastrado com sucesso!', 'success')
            response = make_response(redirect(url_for('home')))
            response.set_cookie('username', username, max_age=60*30)
            response.set_cookie('email', email, max_age=60*30)
            response.set_cookie('password', password, max_age=60*30)
            return response
    
    return render_template("formulario.html")

@app.route('/home')
def home():
    session.pop('_flashes', None)
    username = request.cookies.get('username')
    if username:
        return render_template("home.html", username=username)
    return redirect(url_for('registrarUsuario'))

if __name__ == '__main__':
    app.run(debug=True)