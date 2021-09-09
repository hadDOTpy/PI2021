from config import *
from modelo import Planta

@app.route("/")
def padrao():
    return "backend operante"

@app.route("/listar_usuarios")
def listar_usuarios():
    usuarios = db.session.query(Usuario).all()
    retorno = []
    for i in usuarios:
        retorno.append(i.json())
    r = jsonify(retorno)
    return r

@app.route("/listar_pets")
def listar_pets():
    pets = db.session.query(Pet).all()
    retorno = []
    for i in pets:
        retorno.append(i.json())
    r = jsonify(retorno)
    return r

app.run(debug = True)