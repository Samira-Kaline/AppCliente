from flask import Flask,request
from flask import jsonify
import sqlite3

app = Flask(__name__)

@app.route('/campi', methods=['POST']) #POST: cadastrar.
def cadastrarCampus():

    print("Cadastrar o campus")
    req_data = request.get_json()

    nome_campus = str(req_data['nome_campus'])
    cidade = str(req_data['cidade'])
    sigla = str(req_data['sigla'])

    print(nome_campus, cidade, sigla)

    # Persistência dos dados
    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # inserindo dados na tabela
    cursor.execute("""
      INSERT INTO tb_campus (nome_campus, cidade, sigla)
      VALUES (?,?,?)
    """, (nome_campus, cidade, sigla))

    conn.commit()

    print('Dados inseridos com sucesso.')

    conn.close()

    resp = jsonify()
    resp.status_code = 201

    return resp

@app.route('/campi', methods=['GET']) #GET: listar todos.
def listarCampi():

    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
      SELECT * FROM tb_campus;
    """)
    # Lista de Pessoas.
    campi = []

    for linha in cursor.fetchall():
        id = str(linha[0])
        nome_campus = str(linha[1])
        cidade = str(linha[2])
        sigla = str(linha[3])
        # Pessoa.
        campus = {'id': id, 'nome': nome_campus, 'cidade': cidade,'sigla': sigla}
        # Adicionar a pessoa a lista.
        campi.append(campus)

    conn.close()

    resp = jsonify(Listadecampi=campi)
    resp.status_code = 201

    return resp

@app.route('/campi/nome/<nome_campus>', methods=['GET'])
def consultarCampusPorNome(nome_campus):

    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # lendo os dados
    query = "SELECT * FROM tb_campus WHERE nome_campus LIKE '%{}%'".format(nome_campus)
    cursor.execute(query)

    # Lista de Campi.
    campi = []

    for linha in cursor.fetchall():
        id = str(linha[0])
        nome_campus = str(linha[1])
        cidade = str(linha[2])
        sigla = str(linha[3])
        # Campi.
        campus = {'id': id, 'nome': nome_campus, 'cidade': cidade,'sigla': sigla}
        # Adicionar a campus a lista.
        campi.append(campus)

    conn.close()

    resp = jsonify(Campus_Pesquisado=campi)
    resp.status_code = 201

    return resp

@app.route("/campi/<int:id>", methods=['GET'])#GET: retornar a entidade por id.
def consultarCampusPorId(id):
    campus = []

    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
          SELECT * FROM tb_campus WHERE id_campus = %d;
        """%(id))

    resultSet = cursor.fetchone()

    if resultSet is not None:
        id_campus = str(resultSet[0])
        nome_campus = str(resultSet[1])
        cidade = str(resultSet[2])
        sigla = str(resultSet[3])

        # Pessoa.
        campus = {'id': id_campus,'nome': nome_campus, 'cidade': cidade, 'sigla': sigla}

    conn.close()

    resp = jsonify(campi=campus)
    resp.status_code = 201

    return resp

@app.route("/campi/<int:id>", methods=['DELETE']) #DELETE: remover a entidade por id.
def removerCampusPorId(id):
    print("Apagando: " + str(id))

    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # excluindo um registro da tabela
    cursor.execute("""
    DELETE FROM tb_campus
    WHERE id_campus = ?
    """, (id,))

    conn.commit()

    print('Registro excluido com sucesso.')

    conn.close()

    resp = jsonify()
    resp.status_code = 201

    return resp

@app.route('/alunos', methods=['POST'])
def cadastrarAluno():

    print("Entrou na função")
    req_data = request.get_json()

    matricula_aluno= str(req_data['matricula_aluno'])
    nome = str(req_data['nome'])
    nascimento = str(req_data['nascimento'])
    altura = float(req_data['altura'])
    peso= float(req_data['peso'])


    # Persistência dos dados
    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # inserindo dados na tabela
    cursor.execute("""
      INSERT INTO tb_aluno (matricula_aluno, nome, nascimento, altura, peso)
      VALUES (?,?,?,?,?)
    """, (matricula_aluno, nome, nascimento, altura, peso))

    conn.commit()

    print('Dados inseridos com sucesso.')

    conn.close()

    resp = jsonify()
    resp.status_code = 201

    return resp


@app.route('/alunos', methods=['GET'])
def listarAlunos():
    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
      SELECT * FROM tb_aluno;
    """)
    # Lista de Alunos.
    Lista_Alunos = []

    for linha in cursor.fetchall():
        id_aluno = str(linha[0])
        matricula_aluno = str(linha[1])
        nome = str(linha[2])
        nascimento= str(linha[3])
        altura = str(linha[4])
        peso = str(linha[5])

        pessoa = {'id': id_aluno, 'matricula': matricula_aluno, 'nome': nome, 'nascimento': nascimento, 'altura': altura, 'peso': peso}
        # Adicionar a aluno a lista.
        Lista_Alunos.append(pessoa)

    conn.close()

    resp = jsonify(lista_Pessoas=Lista_Alunos)
    resp.status_code = 201

    return resp

@app.route('/aluno/nome/<nome>', methods=['GET'])
def consultarAlunoPorNome(nome):

    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # lendo os dados
    query = "SELECT * FROM tb_aluno WHERE nome LIKE '%{}%'".format(nome)
    cursor.execute(query)
    # Lista de Alunos.
    Lista_Alunos = []

    for linha in cursor.fetchall():
        id_aluno = str(linha[0])
        matricula_aluno = str(linha[1])
        nome = str(linha[2])
        nascimento= str(linha[3])
        altura = str(linha[4])
        peso = str(linha[5])

        aluno = {'id': id_aluno, 'matricula': matricula_aluno, 'nome': nome, 'nascimento': nascimento, 'altura': altura, 'peso': peso}
        # Adicionar a aluno a lista.
        Lista_Alunos.append(aluno)

    conn.close()

    resp = jsonify(Aluno_Pesquisado=aluno)
    resp.status_code = 201

    return resp

@app.route('/alunos/<int:id>', methods=['GET'])
def consultarAlunoPorId(id):
    pessoa = []

    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
          SELECT * FROM tb_aluno WHERE id_aluno = %d;
        """%(id))

    resultSet = cursor.fetchone()

    if resultSet is not None:
        id_aluno = str(resultSet[0])
        matricula_aluno = str(resultSet[1])
        nome = str(resultSet[2])
        nascimento= str(resultSet[3])
        altura = str(resultSet[4])
        peso = str(resultSet[5])
        # Pessoa.
        pessoa = {'id_aluno': id_aluno,'matricula_aluno': matricula_aluno, 'nome': nome, 'nascimento': nascimento,'altura': altura,'peso': peso}

    conn.close()

    resp = jsonify(pessoa)
    resp.status_code = 201

    return resp

@app.route("/alunos/<int:id>", methods=['DELETE']) #DELETE: remover a entidade por id.
def removerAlunoPorId(id):
    print("Apagando: " + str(id))

    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # excluindo um registro da tabela
    cursor.execute("""
    DELETE FROM tb_aluno
    WHERE id_aluno = ?
    """, (id,))

    conn.commit()

    print('Registro excluido com sucesso.')

    conn.close()

    resp = jsonify()
    resp.status_code = 201

    return resp

@app.route('/nutricionista', methods=['POST']) #POST: cadastrar.
def cadastrarNutricionista():

    print("Cadastrar o nutricionista")
    req_data = request.get_json()

    nome = str(req_data['nome'])
    siape = str(req_data['siape'])
    CRN = str(req_data['CRN'])

    print(nome, siape, CRN)

    # Persistência dos dados
    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # inserindo dados na tabela
    cursor.execute("""
      INSERT INTO tb_nutricionista (nome, siape, CRN)
      VALUES (?,?,?)
    """, (nome, siape, CRN))

    conn.commit()

    print('Dados inseridos com sucesso.')

    conn.close()

    resp = jsonify()
    resp.status_code = 201

    return resp

@app.route('/nutricionista', methods=['GET']) #GET: listar todos.
def listarNutricionista():

    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
      SELECT * FROM tb_nutricionista;
    """)
    # Lista de Pessoas.
    Nutricionistas = []

    for linha in cursor.fetchall():
        id = str(linha[0])
        nome = str(linha[1])
        siape = str(linha[2])
        CRN = str(linha[3])
        # Pessoa.
        nutric = {'id': id, 'nome': nome, 'siape': siape,'CRN': CRN}
        # Adicionar a pessoa a lista.
        Nutricionistas.append(nutric)

    conn.close()

    resp = jsonify(Lista_de_Nutricionistas=Nutricionistas)
    resp.status_code = 201

    return resp

@app.route('/nutricionista/nome/<nome>', methods=['GET'])
def consultarNutricionistaPorNome(nome):

    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # lendo os dados
    query = "SELECT * FROM tb_nutricionista WHERE nome LIKE '%{}%'".format(nome)
    cursor.execute(query)

    Nutricionistas = []

    for linha in cursor.fetchall():
        id = str(linha[0])
        nome = str(linha[1])
        siape = str(linha[2])
        CRN = str(linha[3])
        # Pessoa.
        nutric = {'id': id, 'nome': nome, 'siape': siape,'CRN': CRN}
        # Adicionar a nutricionista a lista.
        Nutricionistas.append(nutric)

    conn.close()

    resp = jsonify(Nutricionista_Pesquisado=nutric)
    resp.status_code = 201

    return resp

@app.route("/nutricionista/<int:id>", methods=['GET'])#GET: retornar a entidade por id.
def consultarNutricionistaPorID(id):

    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
          SELECT * FROM tb_nutricionista WHERE id_nutricionista = %d;
        """%(id))

    resultSet = cursor.fetchone()

    if resultSet is not None:
        id_nutricionista = str(resultSet[0])
        nome = str(resultSet[1])
        siape = str(resultSet[2])
        CRN = str(resultSet[3])

        # Pessoa.
        Nutricionista = {'id': id_nutricionista,'nome': nome, 'siape': siape, 'CRN': CRN}

    conn.close()

    resp = jsonify(Dados_do_Nutricionista=Nutricionista)
    resp.status_code = 201

    return resp

@app.route("/nutricionista/<int:id>", methods=['DELETE']) #DELETE: remover a entidade por id.
def removerNutricionistaPorID(id):
    print("Apagando: " + str(id))

    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # excluindo um registro da tabela
    cursor.execute("""
    DELETE FROM tb_nutricionista
    WHERE id_nutricionista = ?
    """, (id,))

    conn.commit()

    print('Registro excluido com sucesso.')

    conn.close()

    resp = jsonify()
    resp.status_code = 201

    return resp

@app.route('/refeicao', methods=['POST']) #POST: cadastrar.
def cadastrarRefeicao():

    print("Cadastrar a refeicao")
    req_data = request.get_json()

    nome = str(req_data['nome'])
    hr_inicial = str(req_data['hr_inicial'])
    hr_final = str(req_data['hr_final'])
    custo = float(req_data['custo'])

    # Persistência dos dados
    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # inserindo dados na tabela
    cursor.execute("""
      INSERT INTO tb_refeicao (nome, hr_inicial, hr_final, custo)
      VALUES (?,?,?,?)
    """, (nome, hr_inicial, hr_final, custo))

    conn.commit()

    print('Dados inseridos com sucesso.')

    conn.close()

    resp = jsonify()
    resp.status_code = 201

    return resp

@app.route('/refeicao', methods=['GET']) #GET: listar todos.
def listarRefeicao():

    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
      SELECT * FROM tb_refeicao;
    """)
    # Lista de Pessoas.
    refeicoes = []

    for linha in cursor.fetchall():
        id_refeicao = str(linha[0])
        nome = str(linha[1])
        hr_inicial = str(linha[2])
        hr_final = str(linha[3])
        custo = float(linha[4])
        # Pessoa.
        refeicao = {'id_refeicao': id_refeicao, 'nome': nome, 'hr_inicial': hr_inicial,'hr_final': hr_final, 'custo': custo}
        # Adicionar a pessoa a lista.
        refeicoes.append(refeicao)

    conn.close()

    resp = jsonify(Lista_de_refeicoes=refeicoes)
    resp.status_code = 201

    return resp

@app.route('/refeicao/nome/<nome>', methods=['GET'])
def consultarRefeicaoPorNome(nome):

    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # lendo os dados
    query = "SELECT * FROM tb_refeicao WHERE nome LIKE '%{}%'".format(nome)
    cursor.execute(query)

    refeicoes = []

    for linha in cursor.fetchall():
        id_refeicao = str(linha[0])
        nome = str(linha[1])
        hr_inicial = str(linha[2])
        hr_final = str(linha[3])
        custo = float(linha[4])
        # Pessoa.
        refeicao = {'id_refeicao': id_refeicao, 'nome': nome, 'hr_inicial': hr_inicial,'hr_final': hr_final, 'custo': custo}
        # Adicionar a refeição a lista.
        refeicoes.append(refeicao)

    conn.close()

    resp = jsonify(Refeicao_Pesquisada=refeicao)
    resp.status_code = 201

    return resp

@app.route("/refeicao/<int:id>", methods=['GET'])#GET: retornar a entidade por id.
def consultarRefeicaoPorID(id):

    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
          SELECT * FROM tb_refeicao WHERE id_refeicao = %d;
        """%(id))

    resultSet = cursor.fetchone()

    if resultSet is not None:
        id_refeicao = str(resultSet[0])
        nome = str(resultSet[1])
        hr_inicial = str(resultSet[2])
        hr_final = str(resultSet[3])
        custo = float(resultSet[4])

        # Pessoa.
        Refeicao = {'id': id_refeicao,'nome': nome, 'hr_inicial': hr_inicial, 'hr_final': hr_final, 'custo': custo}

    conn.close()

    resp = jsonify(Dados_da_Refeicao=Refeicao)
    resp.status_code = 201

    return resp

@app.route("/refeicao/<int:id>", methods=['DELETE']) #DELETE: remover a entidade por id.
def removerRefeicaoPorID(id):
    print("Apagando: " + str(id))

    conn = sqlite3.connect('bd_nutrif.db')
    cursor = conn.cursor()

    # excluindo um registro da tabela
    cursor.execute("""
    DELETE FROM tb_refeicao
    WHERE id_refeicao = ?
    """, (id,))

    conn.commit()

    print('Registro excluido com sucesso.')

    conn.close()

    resp = jsonify()
    resp.status_code = 201

    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
