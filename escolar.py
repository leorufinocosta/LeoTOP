# Importando bibliotecas
from flask import Flask, request, render_template
from flaskext.mysql import MySQL
from bd import *
from bdsimulado import *


# Instanciando a app Flask
app = Flask(__name__)
# Instanciar o objeto MySQL
mysql = MySQL()
# Ligar o MYSQL ao Flask
mysql.init_app(app)

# Configurando o acesso ao MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'escolar'

# Rota para /
@app.route('/')
def principal():
    return render_template('index.html')

# Rota para /login
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')

        # Obtendo o cursor para acessar o BD
        cursor = mysql.get_db().cursor()

        # Obtendo o idlogin
        idlogin = get_idlogin(cursor, login, senha)

        # Verificar a senha
        if idlogin is None:
            return render_template('index.html', erro='Login/senha incorretos!')
        else:
            # Obtendo o cursor para acessar o BD
            cursor = mysql.get_db().cursor()

            return render_template('oi.html', nome=login, disciplinas=get_notas(cursor, idlogin))

    else:
        return render_template('index.html', erro='Método incorreto. Use POST!')

# Rota para detalhar dsciplina
@app.route('/detalhar/<disciplina>')
def detalhar(disciplina):
    return render_template('disciplina.html', disciplina = disciplina, detalhe=get_detalhes(disciplina))

# Rodando a app
if __name__ == '__main__':
    app.run(debug=True)