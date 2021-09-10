import sqlite3

conexao = sqlite3.connect('dotis.db')
c = conexao.cursor()

c.execute("""
CREATE TABLE usuario (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    fone TEXT NOT NULL,
    estado TEXT NOT NULL,
    cidade TEXT
);
""")
c.execute("""
CREATE TABLE pet (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    sexo TEXT NOT NULL,
    vacina TEXT NOT NULL,
    castracao TEXT NOT NULL,
    descricao TEXT
);
""")
c.execute("""
CREATE TABLE publicacao (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    data DATE NOT NULL,
    id_user INTEGER,
    id_pet INTEGER,
    FOREIGN KEY(id_user) REFERENCES usuario(id)
    FOREIGN KEY(id_pet) REFERENCES pet(id)
);
""")
c.execute("""
CREATE TABLE adocao (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    data DATE NOT NULL,
    id_user INTEGER,
    id_pet INTEGER,
    FOREIGN KEY(id_user) REFERENCES usuario(id)
    FOREIGN KEY(id_pet) REFERENCES pet(id)
);
""")

c.execute("""
INSERT INTO pet (nome, idade, sexo, vacina, castracao, descricao)
VALUES ("Felix", 2, "M", "Sim", "Não", "Arisco")
""")

conexao.commit()

c.execute("""
SELECT * FROM pet;
""")

for i in c.fetchall():
    print(i)

conexao.commit()
conexao.close()


