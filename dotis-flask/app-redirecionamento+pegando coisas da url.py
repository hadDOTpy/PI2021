#| Importa o Flask  ¯\_(ツ)_/¯
#| 1º flask com <f> minusculo 2º com <f> maiusculo
from flask import Flask, redirect, url_for
import random

emojos   = ['✨', '🎉', '🦄', '💗', '👀']
coolNames= ['FERNANDA','HENRIQUE','INGRID','JOÃO']

#| Define a instancia do flask como uma variavel, P.O.O
app = Flask(__name__)



#| Roda root
@app.route('/')
def main():
    return f'<h3>/hello/seu-nome<h3>'


@app.route('/hello')          #      ⎫ > Todas essas rotas_
@app.route('/hello/')         #      ⎬ > Redirecionam pra msm coisa
@app.route('/hello/<nome>')   #      ⎭ > so q tem funciona como um "if" (na verdade ele só faz oque um decorador faz mesmo...)
                                                                #|  if rota === '/hello' or '/hello/' or '/hello/<nome>: \/'



def hello(nome=''):                                           #|  ⎫ 
                                                              #|  | 
    emooj = random.choice(emojos)                             #|  | Pega um emoji aleatório da lista de emojos
    if (nome.upper()).strip() in coolNames:                   #|  | trata a str e analisa 
        nomeK = f'<h1>Olá {nome}, seu nome é d+ {emooj}<h1>'  #|  | return A + emooj
    elif nome == '':                                          #|    se resetado:
        nomeK = f'Digite seu nome na url, /hello/seu-nome'    #|  ⎬ return B
                                                              #|  |
    else:                                                     #|  | Nenhum desses  
        nomeK = f'Olá {nome}'                                 #|  | so da uma resposta default
                                                              #|  |
    return f'{nomeK}'                                         #|  ⎭ retorna XYZ dependendo dos if



#| Exemplo para redirecionar para uma URL onde o que vem depois de /post/ tem que ser um int
#|                                                                           também pode ser: string, float, path (string mas aceita < / >) e uuid
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'


#| Rota admin
@app.route('/admin')
def admin():
#| Retorna admin
    return '<h3>Adê eme</h3>'

#| Rota guest com variavel na url (<nome>)
@app.route('/guest/<nome>')
def guest(nome):
    return f'<h3> Guest: {nome}</h3>'
#| Rota user
@app.route('/user/<nome>')
def user(nome):
    #| Se for ADMIN vai usar a função e redirecionar pra outro 
    if nome.upper() == "ADMIN":
        return redirect(url_for('admin'))
        #|                       /admin  <|> N precisa do '/'
    else:
        return redirect(url_for('guest', nome=nome))
        #| Se ñ so redireciona pra página guest msm

#| se for chamado no terminal executa outra coisa, se exportar como modulo não, o de sempre
if __name__ == "__main__":
    app.run(debug=True, port=6969)
#| Porta n pode começar com 0
