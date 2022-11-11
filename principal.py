#principal.py
from models import Produto
from config import db, app

with app.app_context():
    db.drop_all()
    db.create_all()

#cria entidade
tv = Produto(descricao='TV Samsung', preco=1889.90, quantidade='10')

#sem id
print(tv.id)
print(tv.descricao)

with app.app_context():
    # salva no banco
    db.session.add(tv) #adiciona objeto no banco
    db.session.commit() #confirma que é para salvar
    #agora tem id gerado pelo banco
    print('ID:', tv.id)
    #alterando os dados salvos
    tv.descricao = 'TV LG 50"'
    db.session.add(tv)
    db.session.commit()

    #cria outra entidade
    fogao = Produto(descricao='Fogão Eletrolux', preco=957.50, quantidade='5')

    #salva
    db.session.add(fogao)
    db.session.commit()

    #consulta os dados
    produtos = Produto.query.all()
    print(produtos)

    #busca um único registro
    porId = Produto.query.filter_by(id=1).first()
    print(porId)

    porDescricao = Produto.query.filter_by(descricao='Fogão Eletrolux').all()
    print(porDescricao)

    #apaga
    produto = Produto.query.filter_by(id=1).first()
    if produto:
        db.session.delete(produto)
        db.session.commit()
        print('Apagou produto')
    else:
        print('Não apagou ou produto')