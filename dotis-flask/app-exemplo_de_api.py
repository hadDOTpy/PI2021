#| Exemplo para a API
#|
#| PARA QUE ?
#| Seria utilizado pelas empresas que tivessem convenio com nosso site
#| As empresas ganhariam uma imagem positiva por estarem ajudando essa causa, mais vizualização e mais público
#| Os usuários ganhariam pontos se quisessem ajudar mensalmente as instituições que ajudam os animais
#| esses pontos seriam utilizados para trocar por produtos / pontos / descontos / cupons (Ainda estamos decidindo isso...)
#| O ponto é:
#| 
#| PRA QUE PRECISAMOS DE UMA API ?
#| Imagine que teremos mais de uma empresa conveniada, e alguem foi na loja física deles e disse "Quero pagare com DotiCoins"
#| O que o funcionario faria? Acessar o banco de dados e editar isso manualmente? Entrar no site e trocar isso em algum lugar?
#| E se o funcionário não tiver conhecimento para isso? ele não precisa se preucupar com como ele faria isso a função dele é apenas vender.
#| 
#| ONDE A API AJUDARIA ?
#| Assim que tivermos uma API serão inumeros os jeitos que poderemos adicionar, remover e checar esses pontos
#| Pode ser desde um aplicativo, um site, um comando de linha, pode até ser implementado no própio site da empresa
#| 
#| EX em um pseudo-código:
#| 
#| if payment == DotisCoins:
#|     auth = 'Mjk2MDU4MDAzNDUzMzc4NTYy.YFzLWw.nMQf-U0b_e2y9BnCEqRezltkuIc' #| Pode ser um input de senha que cada empresa teria, só criptografar em sha256 ou md5
#|     points = checkDPoints('0018749848963', auth)
#|     
#|     if points >= cartValue:
#|         updateDPoints((cartValue * -1), '0018749848963', auth)
#| 


#| 1º flask com <f> minusculo 2º com <f> maiusculo
from flask import Flask, redirect, url_for
import random

#| Define a instancia do flask como uma variavel, P.O.O
app = Flask(__name__)


#| Roda root
@app.route('/')
def main():
    return f'Criar meu web site, fazer minha home-page... \nCom quantos gigabytes se faz uma jangada? Um barco que veleje nesse info-mar ?'



#| Métodos HTTP:
#|
#| GET     >   Manda uma request para ter alguma informação, o server retorna (ou não) as informações, de preferencia em JSON;
#| POST    >   Utilizado para formularios;
#| HEAD    >   A mesma coisa que o get, mas com menos informação;
#| PUT / PATCH     >   Troca a informação que tem pela que você especificou;
#| DELETE  >   Deleta as informações do target que você especificou;
#| 
#| https://pythonbasics.org/flask-http-methods/




@app.route('/hello')
def hello():                                                  #|  ⎫ 
                                                              #|  | 
                                                              #|  | Pega um emoji aleatório da lista de emojos
                                                              #|  | trata a str e analisa 
                                                              #|  | return A + emooj
                                                              #|    se resetado:
                                                              #|  ⎬ return B
                                                              #|  |
                                                              #|  | Nenhum desses  
                                                              #|  | so da uma resposta default
                                                              #|  |
                                                              #|  ⎭ retorna XYZ dependendo dos if                                                              
    pass


#| se for chamado no terminal executa outra coisa, se exportar como modulo não, o de sempre
if __name__ == "__main__":
    app.run(debug=True, port=6969)
#| Porta n pode começar com 0
