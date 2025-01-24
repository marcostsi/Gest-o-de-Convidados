from flask import *

app = Flask(__name__)

convidados = ['Alex', 'Robert', 'Hugo', 'Erik', 'Vinicius']

@app.route("/")
def principal():
    return render_template("index.html")

@app.route("/verificarUsuario", methods=['POST'])
def verificar():
    nome = request.form.get("nomeUsuario")
    if(nome in convidados):
        mensagem = "Você esta convidado"
        return render_template("resultado.html", mensagem=mensagem)
    else:
        mensagem = "Você NÃO esta convidado"
        return render_template("resultado.html", mensagem=mensagem)
    

app.run(debug=True)
