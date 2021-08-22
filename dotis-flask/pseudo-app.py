from flask import Flask, render_template

#| Define a instancia do flask como uma variavel, P.O.O
app = Flask(__name__)

#| Aqui você cria a 'url' com o decorador ( @ )
@app.route('/')
#| Qnd em site.com/
def index():
    return "<h1>Hey, you, you\'re finally awake !<h1>" #| Da pra colocar tags no retun


#| Outro jeito de criar rotas sem o decorador (@)____________________,
# ⠀                                                                 #|
def teste():                                                        #|
    return '<h1>você esta na rota 127.0.0.1:XXXX/teste-1 !</h1>'    #|
# ⠀                                                                 #|
def teste2():                                                       #|
    return '<h1>você esta na rota 127.0.0.1:XXXX/teste-2 !</h1>'    #|
# ⠀                                                                 #|
# ⠀                                                                 #|
app.add_url_rule('/teste-2','n_sei_q_isso_faz',teste2)              #|
app.add_url_rule('/teste-1','cobre', teste)                         #|
# ⠀                 \/    |   \/     |  \/                          #|
#                  rota   |          | a função                     #|
#                         | ¯\(ツ)/¯ | q ele chama                  #|
#                         |          | def teste()                  #|
# ⠀                                                                 #|
#|{{end_%block%}}___________________________________________________#|


#| Redireciona em caso de erro=| 
#|                 \/---------=/
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
#|                                        \
#| renderiza a página 404 e retorna o erro_|

#| Se for chamado no terminal executa outra coisa, se exportar como modulo não
if __name__ == '__main__':
    app.run(debug=True, port=6969)
#| renderizar( Deug = True, porta = 7777 )
#| Porta n pode começar com 0
