from flask import Flask

app = Flask(__name__)

@app.route('/user/<nome>') 
def login(nome):
    return nome*10

if __name__ == "__main__":
    app.run()