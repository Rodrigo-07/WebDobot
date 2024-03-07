# app.py
from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB

app = Flask(__name__)

# Configuração para recarregar os templates (Páginas HTML) automaticamente
app.config["TEMPLATES_AUTO_RELOAD"] = True

db = TinyDB("posts.json")

@app.route("/")
def index():
    return render_template("index.html")

# Aqui estamos passando um parametro para a rota e usando ele no template então quando rederizamos o template ele vai mostrar o nome que passamos na URL
# @app.route("/sobre/<nome>")
# def sobre(nome):
#     return render_template("sobre.html", nome=nome)

@app.route("/sobre", methods=["GET", "POST"])
def sobre(nome=None):
    if request.method == "POST":
        nome = request.form.get("nome")
        db.insert({"nome": nome})

    # Pegar todos os dados do banco de dados
    posts = db.all()
    return render_template("sobre.html", nome=nome, posts=posts)

# Tendo o run não precisamos passar os parametrso do servidor pelo terminal basta rodar o arquivo
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000) # host="0. 0. 0. 0" para rodar em qualquer IP da sua rede