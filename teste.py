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

        usuario = input('Digite aqui seu nome de usuario! ')
        senha = input('Crie uma senha aqui: ')
        senha_confirm = input('Crie uma senha aqui: ')
        email = input('Coloque seu melhor email aqui! ')

        # criar tabela para cada usuario.

        sql = 'INSERT INTO usuarios (usuario, senha, senha_confirm, email) VALUES (%s, %s, %s, %s)'
        valores = (usuario, senha, senha_confirm, email)
        cursor.execute(sql, valores)

        pprint('Cadastro realizado com sucesso!')

        conn.commit()
        cursor.close()

