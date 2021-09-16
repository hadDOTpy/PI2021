from config import *

class Usuario(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(254))
	email = db.Column(db.String(254))
	estado = db.Column(db.String(254))
 	cidade = db.Column(db.String(254))
	fone = db.Column(db.String(254))
	cpf = db.Column(db.Integer(11))

	def json(self):
		return {
			"id" : self.id,
			"nome" : self.nome,
			"email" : self.email,
			"estado" : self.estado,
			"cidade" : self.cidade,
			"fone" : self.fone,
			"cpf" : self.cpf
		}        

class Pet(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	foto = db.Column(db.LargeBinary)
	nome = db.Column(db.String(254))
	idade = db.Column(db.Integer)
	sexo = db.Column(db.String(254))
	castracao = db.Column(db.String(254))
	vacinas = db.Column(db.String(254))
	desc = db.Column(db.String(254))

	def json(self):
		return {
			"id" : self.id,
			"foto" : self.foto,
			"nome" : self.nome,
			"idade" : self.idade,
			"sexo" : self.sexo,
			"castracao" : self.castracao,
			"vacinas" : self.vacinas,
			"descricao" : self.desc
		}

class Publicacao(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	data = db.Column(db.Date)
	id_user = db.Column(db.Integer, foreign_key('usuario.id'))
	id_pet = db.Column(db.Integer, foreign_key('pet.id'))

class Adocao(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	data = db.Column(db.Date)
	id_user = db.Column(db.Integer, foreign_key('usuario.id'))
	id_pet = db.Column(db.Integer, foreign_key('pet.id'))       

if __name__ == "__main__":
	# apagar o arquivo, se houver
	if os.path.exists(arquivobd):
	os.remove(arquivobd)

	# criar tabelas
	db.create_all()

	# teste da classe Pessoa
	p1 = Pet(nome = "Max", idade = 2, sexo = "M", castracao = "N", vacinas = "S", desc = "cachorro de porte médio")
	p2 = Pet(nome = "Felice", idade = 4, sexo = "F", castracao = "S", vacinas = "S", desc = "gato pequeno")    

	# persistir
	db.session.add(p1)
	db.session.add(p2)
	db.session.commit()

	# exibir a pessoa no format json
	print(p2.json())
