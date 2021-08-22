from flask import Flask

app = Flask(__name__)   #, static_folder='static')
#| bla bla bla  ----    static folder é aonde_
#|                      >ficarão arquivos como
#|                      >css(scss,sass); Imagens
#|                      >os própios html's, etc...
#|
#| Vc ñ precisa dar <static_folder='static'> 
#| por padrão ja é static
#| só pra mostrar q vc pode mudar (._. )

@app.route('/')
def index():
    return


if __name__ == "__main__":
    app.run(debug=True)