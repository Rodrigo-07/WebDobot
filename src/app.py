# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

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
        nome = request.form.get("nome") # Vai pegar o valor do input com o nome "nome"
    return render_template("sobre.html", nome=nome)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)