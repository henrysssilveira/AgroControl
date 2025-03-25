import mysql.connector
import pprint
from pprint import pprint 


conn = mysql.connector.connect(
        host="localhost",
        user="henrique",
        password="1234",
        database="meu_banco"
    )

def cadastrar_usuario():

        # cadastro de um usuario
        cursor = conn.cursor()

        nome = input('Digite aqui seu nome! ')
        idade = input('Insira aqui sua idade: ')
        email = input('Coloque seu melhor email aqui! ')

        sql = 'INSERT INTO usuarios (nome, idade, email) VALUES (%s, %s, %s)'
        valores = (nome, idade, email)
        cursor.execute(sql, valores)

        pprint('Cadastro realizado com sucesso!')

        conn.commit()
        cursor.close()


def dashboard():
    while True:
        print('\n[1] Cadastrar animais:')
        print('[2] Sair')
          
        escolha_dash = input('Escolha sua opção')

        if escolha_dash == '1':
            cadastro_de_animais()
        elif escolha_dash == '2':
            print('Até uma proxima!')
            break
        else:
             print('Opção invalida!')
          
dashboard()

def cadastro_de_animais():

        # Cadastrando um animal
        cursor_animais_cad = conn.cursor()

        nome_do_animal = input('Insira o nome do animal? (ex: Dolores) ')
        tipo_de_animal = input('Qual é o tipo do seu animal? (ex: grande porte) ')
        idade_do_animal = input('Quantos anos seu animal tem? (ex: 6 anos) ')

        sql_animais = 'INSERT INTO animais (nome_do_animal, idade_do_animal, tipo_de_animal) VALUES (%s, %s, %s)'
        valores_dos_animais = (nome_do_animal, idade_do_animal, tipo_de_animal)
        cursor_animais_cad.execute(sql_animais, valores_dos_animais)

        pprint('Cadastro do Animal feito com sucesso!')

        conn.commit()
        cursor_animais_cad.close()

def login_usuario():
        
        #login
        cursor_login = conn.cursor()

        email = input('Insira seu email de login aqui: ')

        sql_login = 'SELECT nome FROM usuarios WHERE email = %s'
        cursor_login.execute(sql_login, (email,))

        usuario = cursor_login.fetchone()
        cursor_login.close

        if usuario:
            nome_usuario = usuario[0]
            print(f'✅ Bem-vindo, {usuario[0]}!')
            dashboard()
        else:
            print('❌ E-mail não encontrado. Tente novamente.')

def menu():
      
      # Menu para escolha entre login e cadastro
    while True:
        print("\n[1] Cadastrar-se")
        print("[2] Fazer Login")
        print("[3] Sair")

        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            cadastrar_usuario()
        elif escolha == '2':
            login_usuario()
        elif escolha == '3':
            print('Até uma proxima!')
            break
        else:
            print('Erro, tente novamente!')

menu()

conn.close()