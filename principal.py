#principal.py
from flask import render_template, redirect, request, session, flash

from formularios import FormCadastro
from models import Login
from config import db, app, lista



@app.route('/')
def home():
    if not session:
        session['login'] = None
    db.create_all()
    lista = Login.query.all()
    return render_template('inicial.html', lista=lista)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if session['login'] == None:
        flash('Nenhum usuário logado')
        return redirect('/')
    form = FormCadastro()
    return render_template('formulario.html', form=form)

@app.route('/salvar', methods=['GET', 'POST'])
def salvar():
    form = FormCadastro()
    if form.validate_on_submit():
        nome = form.nome.data
        idade = form.idade.data
        email = form.email.data
        senha = form.senha.data
        #verifica se o e-mail já existe
        if Login.query.filter_by(email=email).first():
            form.email.errors.clear()
            form.email.errors.append('Este e-mail já está cadastrado, use outro!')
            return render_template('formulario.html', form=form)
        else:
            #salva o login
            cadastro = Login(nome, idade, email, senha)
            db.session.add(cadastro)
            db.session.commit()
            return redirect('/')
    else:
        form.recaptch.errors.clean()
        form.recaptcha.errors.append('Você precisa validar o CAPTCHA')
        return render_template('formulario.html', form=form)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    email = request.form['email']
    senha = request.form['senha']
    login = Login.query.filter_by(email=email).first()
    if login and login.verificar_senha(senha):
        session['login'] = login.nome
        flash(login.nome + ' está logado')
        return redirect('/')
    else:
        flash('E-mail e/ou senha inválido')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['login'] = None
    flash('Nenhum usuário logado!')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)