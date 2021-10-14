from config import *

class Usuario(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(254))
	email = db.Column(db.String(254))
	estado = db.Column(db.String(254))
	cidade = db.Column(db.String(254))
	fone = db.Column(db.String(254))
	cpf = db.Column(db.Integer)

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
	foto = db.Column(db.String(254))
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
	id_user = db.Column(db.Integer, db.ForeignKey(Usuario.id))
	id_pet = db.Column(db.Integer, db.ForeignKey(Pet.id))
	usuario = db.relationship("Usuario")
	pet = db.relationship("Pet")

	def json(self):
		return {
			"id" : self.id,
			"data" : self.data,
			"id_user" : self.id_user,
			"id_pet" : self.id_pet
		}

class Adocao(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	data = db.Column(db.Date)
	id_user = db.Column(db.Integer, db.ForeignKey(Usuario.id))
	id_pet = db.Column(db.Integer, db.ForeignKey(Pet.id))
	usuario = db.relationship("Usuario")
	pet = db.relationship("Pet")

	def json(self):
		return {
			"id" : self.id,
			"data" : self.data,
			"id_user" : self.id_user,
			"id_pet" : self.id_pet
		}

if __name__ == "__main__":
	# apagar o arquivo, se houver
	if os.path.exists(arquivobd):
		os.remove(arquivobd)

	# criar tabelas
	db.create_all()

	# teste da classe Pessoa
	p1 = Pet(nome = "Max", foto = "gato.png", idade = 2, sexo = "M", castracao = "N", vacinas = "S", desc = "cachorro de porte médio")
	p2 = Pet(nome = "Felice", foto = "gato1.jpg", idade = 4, sexo = "F", castracao = "S", vacinas = "S", desc = "gato pequeno") 
	p3 = Pet(nome = "Bob", foto = "gato2.jpg", idade = 2, sexo = "M", castracao = "N", vacinas = "S", desc = "cachorro de porte médio")
	p4 = Pet(nome = "Pip", foto = "gato3.jpg", idade = 4, sexo = "F", castracao = "S", vacinas = "S", desc = "gato pequeno")
	p5 = Pet(nome = "Neve", foto = "gato4.jpg", idade = 2, sexo = "M", castracao = "N", vacinas = "S", desc = "cachorro de porte médio")
	p6 = Pet(nome = "Dog", foto = "gato5.jpeg", idade = 4, sexo = "F", castracao = "S", vacinas = "S", desc = "gato pequeno")   

	# persistir
	db.session.add(p1)
	db.session.add(p2)
	db.session.add(p3)
	db.session.add(p4)
	db.session.add(p5)
	db.session.add(p6)
	db.session.commit()

	# exibir a pessoa no format json
	print(p5.json())
	# curl -X POST -H "Content-Type:application/json" -d '{"nome": "Jack", "idade": "1", "sexo": "F", "castracao": "S", "vacinas": "S", "desc": "gato bonito"}' localhost:5000/inserir_pets

