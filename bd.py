# Função validar login
def get_idlogin(cursor, login, senha):
    # Executar o sql
    cursor.execute(f'select idlogin from login where login = "{login}" and senha = "{senha}"')

    # Recuperando o retorno do BD
    idlogin = cursor.fetchone()

    # Fechar o cursor
    cursor.close()

    # Retornar o idlogin
    return idlogin[0]

# Funcao para retornar as disciplinas
def get_notas(cursor, idlogin):
    # Executar o SQL
    cursor.execute(f'select disciplinas, nota1, nota2, nota3 from notas where idlogin = {idlogin}')

    # Recuperando o retorno do BD
    disciplinas = cursor.fetchall()

    print(disciplinas)

    # Fechar o cursor
    cursor.close()

    # Retornar os dados
    return disciplinas

def get_disciplinas(cursor, iddisciplinas):
    cursor.execute(f'select nome, descrição from disciplinas where iddisciplinas = {iddisciplinas}')

    nome = cursor.fetchall()

    print(nome)

    cursor.close()

    return nome
