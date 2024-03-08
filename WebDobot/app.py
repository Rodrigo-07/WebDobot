from flask import Flask, render_template, request, redirect, url_for, session, flash
from tinydb import TinyDB, Query
from serial.tools import list_ports
from dobot import Dobot

app = Flask(__name__)
dobot = Dobot()

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

# Endpoints de controle do braço robótico

@app.route('/conexaoRobot')
def conexaoRobot():
    portas_disponiveis = list_ports.comports()

    portas = [x.device for x in portas_disponiveis]

    return render_template('conectarDobot.html', portas=portas)

@app.route('/conectarDobot', methods=['POST'])
def conectarDobot():
    porta = request.form.get('porta')

    if dobot.conectar_dobot(porta):
        return "Conectado ao dobot com sucesso."
    else:
        return "Falha ao conectar ao dobot."

@app.route('/listPortas')
def listarPortas():
    portas_disponiveis = list_ports.comports()

    portas = [x.device for x in portas_disponiveis]

    return render_template('conectarDobot.html', portas=portas)

@app.route('/desconectarDobot')
def desconectarDobot():
    dobot.desconectar_robot()

    return "Desconectado do dobot com sucesso."

@app.route('/moverPara')
def moverPara():
    return render_template('moverPara.html')

@app.route('/posicaoEspefica', methods=['POST'])
def posicaoEspecifica():
    x = float(request.form.get('x'))
    y = float(request.form.get('y'))
    z = float(request.form.get('z'))
    r = float(request.form.get('r'))

    dobot.mover_para(x, y, z, r)

    return "Movido para a posição especificada."

@app.route('/movimentacaoLivre')
def movimentacaoLivre():
    return render_template('movimentacaoLivre.html')

@app.route('/moverLivre', methods=['POST'])
def moverLivre():
    taxa = float(request.form.get('taxa'))
    movimento = request.form.get('direcao')

    print(taxa, movimento)

    dobot.movimentacao_livre(movimento, taxa)

    
    return render_template('movimentacaoLivre.html', taxa=taxa, mensagem="Movimento executado: " + movimento + " com taxa: " + str(taxa))


# Tendo o run não precisamos passar os parametrso do servidor pelo terminal basta rodar o arquivo
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)



