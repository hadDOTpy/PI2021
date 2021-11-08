from config import *

class Usuario(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(254))
	email = db.Column(db.String(254))
	estado = db.Column(db.String(254))
	cidade = db.Column(db.String(254))
	fone = db.Column(db.String(254))
	senha = db.Column(db.String(254))

	def json(self):
		return {
			"id" : self.id,
			"nome" : self.nome,
			"email" : self.email,
			"estado" : self.estado,
			"cidade" : self.cidade,
			"fone" : self.fone,
			"senha" : self.senha
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

# class Publicacao(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)
# 	data = db.Column(db.Date)
# 	id_user = db.Column(db.Integer, db.ForeignKey(Usuario.id))
# 	id_pet = db.Column(db.Integer, db.ForeignKey(Pet.id))
# 	usuario = db.relationship("Usuario")
# 	pet = db.relationship("Pet")

# 	def json(self):
# 		return {
# 			"id" : self.id,
# 			"data" : self.data,
# 			"id_user" : self.id_user,
# 			"id_pet" : self.id_pet
# 		}

# class Adocao(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)
# 	data = db.Column(db.Date)
# 	id_user = db.Column(db.Integer, db.ForeignKey(Usuario.id))
# 	id_pet = db.Column(db.Integer, db.ForeignKey(Pet.id))
# 	usuario = db.relationship("Usuario")
# 	pet = db.relationship("Pet")

# 	def json(self):
# 		return {
# 			"id" : self.id,
# 			"data" : self.data,
# 			"id_user" : self.id_user,
# 			"id_pet" : self.id_pet
# 		}

if __name__ == "__main__":
	# apagar o arquivo, se houver
	if os.path.exists(arquivobd):
		os.remove(arquivobd)

	# criar tabelas
	db.create_all()

	# teste da classe Pet
	p1 = Pet(nome = "Max", foto = "gato.png", idade = 1, sexo = "M", castracao = "N", vacinas = "S", desc = "gato pequeno, gosta de brincar e é muito carinhoso.")
	p2 = Pet(nome = "Felice", foto = "gato1.jpg", idade = 4, sexo = "F", castracao = "S", vacinas = "N", desc = "gato quieto e independente.") 
	p3 = Pet(nome = "Bob", foto = "gato2.jpg", idade = 8, sexo = "M", castracao = "N", vacinas = "S", desc = "gato grande, muito carente, porém medroso.")
	p4 = Pet(nome = "Pip", foto = "gato3.jpg", idade = 4, sexo = "F", castracao = "S", vacinas = "N", desc = "gato pequeno, gosta de brinquedos de arranhar.")
	p5 = Pet(nome = "Neve", foto = "gato4.jpg", idade = 10, sexo = "M", castracao = "N", vacinas = "S", desc = "gato grande, se dá muito bem com crianças e outros animais.")
	p6 = Pet(nome = "Dog", foto = "gato5.jpeg", idade = 1, sexo = "F", castracao = "S", vacinas = "S", desc = "gato pequeno, gosta de carinho nas orelhas e petiscos de frango.")

	u1 = Usuario(nome = "João", email = "joão@gmail.com", estado = "SC", cidade = "Blumenau", fone = "(47)99999-9999", senha = "senhasecreta")
	u2 = Usuario(nome = "Gabriela", email = "gabi@gmail.com", estado = "SP", cidade = "Tremembé", fone = "(47)99999-0000", senha = "senha")
	u3 = Usuario(nome = "Marta", email = "marta@gmail.com", estado = "SC", cidade = "Timbó", fone = "(47)90000-9999", senha = "supersenha")

	# persistir
	db.session.add(p1)
	db.session.add(p2)
	db.session.add(p3)
	db.session.add(p4)
	db.session.add(p5)
	db.session.add(p6)
	db.session.add(u1)
	db.session.add(u2)
	db.session.add(u3)
	db.session.commit()

	# exibir a pessoa no format json
	print(p5.json())
	print(u3.json())


