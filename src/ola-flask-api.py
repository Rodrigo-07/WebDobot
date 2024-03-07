from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/ping')
def ping():
    return "poing"

# O metodo POST é usado para enviar dados para o servidor para criar/alterar um recurso 
# O metodo GET é usado para solicitar dados de um recurso especifico

@app.route('/echo', methods=['POST'])
def echo():
    # Aqui enviamos dados para o servidor e ele nos devolve (printa) os mesmos dados
    return jsonify(request.json)

# Nos dois endpoits, estamos passando os parametros direto na URL sem query String 
@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return jsonify({"resultado": a + b})

@app.route("/subtracao/<int:a>/<int:b>")
def subtracao(a, b):
    return jsonify({"resultado": a - b})

# Aqui estamos passando os parametros via query string
@app.route("/multiplicacao")
def multiplicacao():
    # Dessa forma, estamos pegando os parametros via query string
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return jsonify({"resultado": a * b})

# Aqui estamos passando os parametros via body por isso usamos o método POST
@app.route("/divisao", methods=["POST"])
def divisao():
    dados = request.json
    a = int(dados.get("a"))
    b = int(dados.get("b"))
    return jsonify({"resultado": a / b})