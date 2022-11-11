#config.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Configurações do banco de dados
#para MySQL:
#mysql://username:password@host:port/database_name
#mysql://root:softgraf@localhost:3306/nome_banco

#para PostgreSQL
#postgresql://username:password@host:port/database_name

#aqui vamos usar o SQLite, então precisamos do diretório base do projeto
basedir = os.path.abspath(os.path.dirname(__file__))
#print(basedir)

#url do SQLite
uri = 'sqlite:///' + os.path.join(basedir, 'database.db')
#print(uri)

#Cria a aplicação
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#objeto que representa o banco de dados
db = SQLAlchemy(app)