import mysql.connector
from pprint import pprint 
import pandas as pd
from IPython.display import display

conn = mysql.connector.connect(
        host="localhost",
        user="henrique",
        password="1234",
        database="erp_agro"
    )

def dashboard(nome_usuario):
    while True:
        print('DASHBOARD')
        print('____________________________________________')
        print('\n[1] Atualizar consumos de hoje')
        print('[2] Animais')
        print('[3] Insumos')
        print('[4] Maquinário')
        print('[5] Sair')
          
        escolha_dash = input('Escolha sua opção:  ')

        if escolha_dash == '1':
            atualizar_consumo()
            print('Estamos construindo esta parte ainda! em breve esta opção estara disponivel!')
        if escolha_dash == '2':
            animais()
        elif escolha_dash == '3':
            insumos()
        elif escolha_dash == '4':
            print('Estamos construindo esta parte ainda! em breve esta opção estara disponivel!')
        elif escolha_dash == '5':
            print('Até uma proxima!')
            break
        else:
            print('Opção invalida!')

        print('____________________________________________')

def atualizar_consumo():
        print('Estamos construindo esta parte ainda! em breve esta opção estara disponivel!')
     

def cadastrar_usuario():

        # cadakstro de um usuario
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

def animais():
     while True:
        print('SEÇÃO ANIMAL')
        print('____________________________________________')
        print('\n[1] Cadastrar Animais')
        print('[2] Ver Animais cadastrados')
        print('[3] Sair')

        escolha_animais = input('Escolha sua opção:  ')

        if escolha_animais == '1':
            cadastro_de_animais()
        elif escolha_animais == '2':
            info_animais()
        elif escolha_animais == '3':
            break
        else: 
            print('Opção Invalida!')

def info_animais():
        print('INFORMAÇÕES DOS ANIMAIS')
        print('____________________________________________')
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM relat_animais')
        inf_animal_cs = cursor.fetchall()

        if inf_animal_cs:
            print('Animais Cadastrados')

            lista_animais = []
            for animais in inf_animal_cs:
                lista_animais.append({'Especie do animal': animais['especie'], 'Peso do Animal': animais['peso'], 'Genero': animais['genero'], 'Porte do animal': animais['porte_do_animal'], 'Idade': animais['idade'], 'Produtividade': animais['produtividade'] })

        df = pd.DataFrame(lista_animais)
        print(df)

        cursor.close()


def insumos():
     while True:

        print('SEÇÃO DE INSUMOS')
        print('____________________________________________')

        print('[1] Atualizar insumos')
        print('[2] Gerar relatorio de insumos')
        print('[3] Cadastrar insumos')
        print('[4] Sair')

        escolha_insumos = input('Escolha uma opção:  ')

        if escolha_insumos == '1':
            print('Estamos montando esta area ainda')
        elif escolha_insumos == '2':
            relat_insumos()
        elif escolha_insumos == '3':
            cadastrar_insumos()
        elif escolha_insumos == '4':
            print('até uma proxima!')
            break
        else:
            print('Opção invalida! tente novamente')

def cadastrar_insumos():
        
        print('CADASTRAR INSUMOS')
        print('____________________________________________')
        
        cursor_cad_insumos = conn.cursor()

        nome_insumo = input('Qual insumo deseja cadastrar?  ')
        categoria_insumo = input('Qual categoria?  ')
        qntd_add_insumo = input('Quanto deseja adicionar? (adicione com unidade de medida)  ')
        validade_insumo = input('Data de validade?  ')
        fornecedor_insumo = input('Qual fornecedor?  ')
        pa_insumo = input('Qual o preço de aquisição?  ')
        qntd_usd_insumo = input('Quanto já foi utiliazdo?  ')

        sql_insumo = 'INSERT INTO insumos (nome_insumo, categoria_insumo, qntd_add_insumo, validade_insumo, fornecedor_insumo, pa_insumo, qntd_usd_insumo) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        valores_insumos = (nome_insumo, categoria_insumo, qntd_add_insumo, validade_insumo, fornecedor_insumo, pa_insumo, qntd_usd_insumo)
        cursor_cad_insumos.execute(sql_insumo, valores_insumos)

        pprint('Cadastrado com sucesso"')

        conn.commit()
        cursor_cad_insumos.close()


def relat_insumos():
        print('RELATORIO DE INSUMOS')
        print('____________________________________________')

        cursor_relat_insumos = conn.cursor()

        sql_relat_insumos = 'SELECT * FROM erp_agro.insumos_view_relat_testando;'
        cursor_relat_insumos.execute(sql_relat_insumos)
        insumos = cursor_relat_insumos.fetchall()
        cursor_relat_insumos.close()

        if insumos:
            print('Insumos disponíveis:')

            insumos_lista = []
            for insumo in insumos:
                insumos_lista.append({'nome': insumo[0], 'categoria': insumo[1], 'Validade': insumo[2], 'Qtd Adicionada': insumo[3], 'Qtd Usada': insumo[4] })

            df = pd.DataFrame(insumos_lista)
            print('Aqui é o print')
            print(df)
        else:
            print('Nenhum insumo encontrado.')


def cadastro_de_animais():
        
        print('CADASTRO DE ANIMAIS')
        print('____________________________________________')

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
        
        print('LOGIN')
        print('____________________________________________')

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
        print("\033[32m'Olá! seja bem vindo ao AgroControl'\033[0m")
        print('____________________________________________')

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
            print('____________________________________________')
            break
        else:
            print('Erro, tente novamente!')

menu()
conn.close()