from flask import Flask, render_template, request, redirect, url_for, session, flash
from tinydb import TinyDB, Query

app = Flask(__name__)

dbUsario = TinyDB('usuarios.json', indent=4)

# Configuração para recarregar os templates (Páginas HTML) automaticamente
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastrar.html')

@app.route('/validarLogin', methods=['POST'])
def validarLogin():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    # Busca no banco de dados o usuário e senha
    procura = Query()

    # Verifica se o usuário e senha estão no banco de dados
    resultado = dbUsario.search((procura.usuario == usuario) & (procura.senha == senha))

    # Busca vazia, usuário ou senha inválidos
    if resultado == []:
        return render_template('login.html', erro="Usuário ou senha inválidos")
    else:
        return render_template('home.html', usuarioLogado=usuario)

@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrar():
    # Recebo o request que foi pego do meu formulário
    nome = request.form.get('usuario')
    email = request.form.get('email')
    senha = request.form.get('senha')

    dbUsario.insert({'usuario': nome, 'email': email, 'senha': senha})
    return render_template('cadastrar.html')

# Tendo o run não precisamos passar os parametrso do servidor pelo terminal basta rodar o arquivo
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)



