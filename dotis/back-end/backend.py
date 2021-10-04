from config import *
from modelo import Usuario
from modelo import Pet
from flask import render_template

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
    r.headers.add("Access-Control-Allow-Origin", "*") 
    return r

@app.route("/inserir_pets", methods=['POST'])
def inserir_pets():
    r = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    try:
        novo = Pet(**dados)
        db.session.add(novo)
        db.session.commit()
    except Exception as e:
        r = jsonify({"resultado": "erro", "detalhes": str(e)})
    r.headers.add("Access-Control-Allow-Origin", "*")
    return r

@app.route('/uploadajax', methods = ['POST'])
def upldfile():
    r = jsonify({"mensagem":"tentando..."})
    if request.method == 'POST':
        file_val = request.files['file']
        print("vou salvar em: "+file_val.filename)
        arquivoimg = os.path.join(path, 'img_pet/'+file_val.filename)
        file_val.save(arquivoimg)
        r = jsonify({"mensagem":"ok"})
    r.headers.add("Access-Control-Allow-Origin", "*")
    return r

# @app.route("/index")
# def index():
#     return render_template('index.html', titulo='Dotis')

app.run(debug = True)
