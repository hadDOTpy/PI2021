from config import *

class Usuario(db.Model):
	id_usuario = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(254))
	email = db.Column(db.String(254))
	endereco = db.Column(db.String(254))
	fone = db.Column(db.String(254))
	pontos_acumulados = db.Column(db.Integer)

	def json(self):
        return {
          "id" : self.id_usuario,
          "nome" : self.nome,
          "email" : self.email,
          "endereco" : self.endereco,
          "fone" : self.fone,
          "pontos" : sefl.pontos_acumulados
        }        

class Pet(db.Model):
	id_pet = db.Column(db.Integer, primary_key = True)
	foto = db.Column(db.LargeBinary)
	nome = db.Column(db.String(254))
	idade = db.Column(db.Integer)
	sexo = db.Column(db.String(254))
	castracao = db.Column(db.String(254))
	vacinas = db.Column(db.String(254))
	descricao = db.Column(db.String(254))

	def json(self):
        return {
          "id" : self.id_pet,
          "foto" : self.foto,
          "nome" : self.nome,
          "idade" : self.idade,
          "sexo" : self.sexo,
          "castracao" : self.castracao,
          "vacinas" : self.vacinas,
          "descricao" : self.descricao	
        }        
