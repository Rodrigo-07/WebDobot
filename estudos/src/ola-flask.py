from flask import Flask

# Instanciar uma instancia do Flask
app = Flask(__name__)

# O app é um singleton, ou seja, só pode existir uma instancia do app por vez. É compartilhado por toda a aplicação

# Definir uma rota

# A função que vir debaixo disso é a função que vai ser executada quando a rota for chamada
@app.route('/') # Isso é um decorador
def hello_world():
    return "<p> Olá, mundo!!!</p>"

@app.route('/teste') # Isso é um decorador
def hello_world2():
    return "<p> Olá, mundsdsdsdasdasdasdasdasdasdsadsado!!!</p>"