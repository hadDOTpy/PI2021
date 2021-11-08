from config import *
from modelo import Usuario
from modelo import Pet
from flask import render_template, send_file

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

@app.route("/inserir_user", methods=['POST'])
def inserir_user():
    r = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    try:
        novo = Usuario(**dados)
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

@app.route('/get_image/<int:pet_id>')
def get_image(pet_id):
    pet = db.session.query(Pet).get(pet_id)
    # if request.args.get('type') == '1':
    #    filename = 'ok.gif'
    # else:
    #    filename = 'error.gif'
    arquivoimg = os.path.join(path, 'img_pet/'+ pet.foto)
    # arquivoimg = os.path.join('/home/ingguk/mysite/img_pet', pet.foto)
    # /home/ingguk/mysite/img_pet
    return send_file(arquivoimg, mimetype='image/gif')

# @app.route("/index")
# def index():
#     return render_template('index.html', titulo='Dotis')

@app.route('/get_pet/<int:pet_id>')
def get_pet(pet_id):
    pet = db.session.query(Pet).get(pet_id)
    return jsonify(pet.json())

app.run(debug = True)
