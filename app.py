import mysql.connector
import pprint
from pprint import pprint 


conn = mysql.connector.connect(
        host="localhost",
        user="henrique",
        password="1234",
        database="erp_agro"
    )

def cadastrar_usuario():

        # cadastro de um usuario
        cursor = conn.cursor()

        usuario = input('Digite aqui seu nome de usuario!  ')
        senha = input('Crie uma senha aqui:  ')
        senha_confirm = input('Crie uma senha aqui:  ')
        email = input('Coloque seu melhor email aqui!  ')

        # criar tabela para cada usuario.

        sql = 'INSERT INTO usuarios (usuario, senha, senha_confirm, email) VALUES (%s, %s, %s, %s)'
        valores = (usuario, senha, senha_confirm, email)
        cursor.execute(sql, valores)

        pprint('Cadastro realizado com sucesso!')

        conn.commit()
        cursor.close()


def dashboard(nome_usuario):
    while True:
        print('\n[1] Cadastrar animais:')
        print('[2] Insumos')
        print('[3] Sair')
          
        escolha_dash = input('Escolha sua opção:  ')

        if escolha_dash == '1':
            cadastro_de_animais()
        elif escolha_dash == '2':
            insumos()
        elif escolha_dash == '3':
            print('Até uma proxima!')
            break
        else:
             print('Opção invalida!')
          


def insumos():
     while True:
        print('\n[1] Ver insumos')
        print('[2] Atualizar insumos')
        print('[3] Gerar relatorio de insumos')
        print('[4] Sair')

        escolha_insumos = input('Escolha uma opção:  ')

        if escolha_insumos == '1':
            print('')
        elif escolha_insumos == '2':
            print('')
        elif escolha_insumos == '3':
            print('')
        elif escolha_insumos == '4':
            print('até uma proxima!')
            break
        else:
             print('Opção invalida! tente novamente')


def cadastro_de_animais():

        # Cadastrando um animal
        cursor_animais_cad = conn.cursor()

        especie = input('Insira aqui a especie do animal:  ')
        peso = input('Insira aqui o peso do animal:  ')
        genero = input('Insira aqui o genero do animal:  ')
        porte_do_animal = input('Insira aqui o porte do animal:  ')
        doencas = input('Insira se o animal tiver doenças, se não ouver insira (nd):  ')
        alimentacao = input('Insira o que o animal come:  ')
        idade = input('Insira quantos anos e meses o animal tem (insira como (1.6 anos)):  ')
        vacinacao = input('Insira quais vacinas o animal já tomou:  ')
        produtividada = input('O que o animal produz:  ')

        sql_animais = 'INSERT INTO animais (especie, peso, genero, porte_do_animal, doencas, alimentacao, idade, vacinacao, produtividada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        valores_dos_animais = (especie, peso, genero, porte_do_animal, doencas, alimentacao, idade, vacinacao, produtividada)
        cursor_animais_cad.execute(sql_animais, valores_dos_animais)

        pprint('Cadastro do Animal feito com sucesso!')

        conn.commit()
        cursor_animais_cad.close()

def login_usuario():
        
        #login
        cursor_login = conn.cursor()

        email = input('Insira seu email de login aqui: ')
        senha = input('Insira aqui sua senha:')

        sql_login = 'SELECT usuario FROM usuarios WHERE email = %s AND senha = %s'
        cursor_login.execute(sql_login, (email, senha))

        usuario = cursor_login.fetchone()
        cursor_login.close

        if usuario:
            nome_usuario = usuario[0]
            print(f'✅ Bem-vindo, {usuario[0]}!')
            dashboard(nome_usuario)
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

conn.commit()

conn.close()