import mysql.connector
import pprint
from pprint import pprint 


conn = mysql.connector.connect(
        host="localhost",
        user="henrique",
        password="1234",
        database="meu_banco"
    )

try:
    if conn.is_connected():
        print("ótimo, você se conectou! insira as seguintes informações:")


        # Criar um cursor
        cursor = conn.cursor()

        nome = input('Digite aqui seu nome!')
        idade = input('Insira aqui sua idade:')
        email = input('Coloque seu melhor email aqui!')

        sql = 'INSERT INTO usuarios (nome, idade, email) VALUES (%s, %s, %s)'
        valores = (nome, idade, email)
        cursor.execute(sql, valores)

        pprint('Cadastro realizado com sucesso!')

        conn.commit()
        cursor.close()

except mysql.connector.Error as err:
    print(f"Erro ao conectar: {err}")




finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Conexão fechada.")

conn.close()
