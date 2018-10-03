import sqlite3

# conectando...
conn = sqlite3.connect('bd_nutrif.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela de campus.
cursor.execute("""
CREATE TABLE tb_campus (
        id_campus INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome_campus TEXT NOT NULL,
        cidade TEXT NOT NULL,
        sigla VARCHAR(3) NOT NULL
);
""")

# criando a tabela de aluno.
cursor.execute("""
CREATE TABLE tb_aluno (
        id_aluno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        matricula_aluno VARCHAR(12) NOT NULL UNIQUE,
        nome TEXT NOT NULL,
        nascimento DATE NOT NULL,
        altura REAL NOT NULL,
        peso REAL NOT NULL


);
""")

# criando a tabela de nutricionista.
cursor.execute("""
CREATE TABLE tb_nutricionista (
        id_nutricionista INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        siape VARCHAR(10) NOT NULL UNIQUE,
        CRN TEXT NOT NULL,
        FOREIGN KEY(id_nutricionista) REFERENCES tb_campus(id_campus)

);
""")

# criando a tabela de refeição.
cursor.execute("""
CREATE TABLE tb_refeicao (
        id_refeicao INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        hr_inicial TIME NOT NULL,
        hr_final TIME NOT NULL,
        custo REAL NOT NULL,
        FOREIGN KEY(id_refeicao) REFERENCES tb_campus(id_campus)


);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()
