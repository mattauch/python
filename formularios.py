#formularios.py

# pip install wtforms
# pip install flask_wtf
# pip install wtforms[email]
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import validators, ValidationError, StringField, IntegerField, SubmitField, PasswordField, EmailField
from wtforms.validators import Length, DataRequired, number_range, Email, EqualTo, Optional

#Usando google reCAPTCHA v2 para registrar um formulário em Flask, para certificar que não é um robô.
#para poder integrar o google reCAPTCHA em um app Flask, nós precisamos registrar um site e obter um par de chaves API

#Google fornece 4 tipos de reCAPTCHA:
#v3 = valida solicitações com pontuação
#v2 = valida solicitações com "Eu não sou um robô"
#invisible = não precisa que clique em uma caixa de seleção
#é chamado quando o usuário clica em um botão do site
#android

#passos:
#1 fazer o login no google
#Documentação: developers.google.com/recaptcha/docs/display
#registro: google.com/recaptcha/admin/create

#2 Etiqueta: primeirorecaptcha
#Tipo: reCAPTCHA v2 - não sou um robô
#Domínios: 127.0.0.1 ou localhost (não são suportados por default)
#verificar e-mail
#marcar Aceitas e Enviar

#3 google vai enviar 2 chaves: chave do site e chave secreta
#salar as chaves em app.config

class FormCadastro(FlaskForm):
    nome = StringField('Nome', validators=[validators.data_required('Faltou digitar o nome'), validators.Length(min=6,max=60)])
    idade = IntegerField('Idade', validators=[DataRequired('Faltou colocar a idade'), number_range(min=18, max=65)])
    email = EmailField('E-mail', validators=[Length(min=6, max=60), Email(message='Entre com um e-mail válido'), DataRequired()])
    senha = PasswordField('Senha', validators=[
        DataRequired(),
        Length(min=6, message='Selecione uma senha forte'),
        EqualTo('confirmacao', message='Senhas devem bater')
    ])
    confirmacao = PasswordField('Confirma sua senha', validators=[DataRequired()])

    recaptcha = RecaptchaField()

    submit = SubmitField('Enviar')

