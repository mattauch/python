from flask import Flask, render_template, request, redirect, url_for, flash, session

from produto import Produto
from dao import ProdutoDao

produtoDao = ProdutoDao('bancodados.db')

app = Flask(__name__)
app.secret_key = 'amanda'

@app.route('/')
def index():
    lista = produtoDao.listar()
    return render_template('relatorio.html', titulo='Relatório de Estoque', produtos=lista)

@app.route('/cadastrar')
def cadastrar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    return render_template('cadastrar.html', titulo='Cadastra Novo Produto')

@app.route('/editar/<string:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    produto = produtoDao.buscar_por_id(id)
    return render_template('editar.html', titulo='Alteração de Produto', produto=produto)

@app.route('/deletar/<string:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    produtoDao.deletar(id)
    flash('Produto removido com sucesso!')
    return redirect(url_for('index'))

@app.route('/salvar', methods=['POST'])
def salvar():
    id = request.form['id']
    descricao = request.form['descricao']
    preco = request.form['preco']
    quantidade = request.form['quantidade']
    produto = Produto(descricao, preco, quantidade, id)
    produtoDao.salvar(produto)
    flash('Produto editado com sucesso!')
    return redirect(url_for('index'))


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['senha'] == '123':
        session['usuario_logado'] = request.form['usuario']
        flash( 'Seja bem vindo(a) ' + request.form['usuario'] +'!' )
        return redirect(url_for('index'))
    else:
        flash('Senha inválida! Você tem mais 3 tentativas.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))


if __name__ == '__main__':
   # app.run(debug=True)
    app.run(debug=True, host='127.0.0.1', port=80)
