import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="henrique",
        password="1234",
        database="meu_banco"
    )
    if conn.is_connected():
        print("Conectado ao MySQL com sucesso!")

except mysql.connector.Error as err:
    print(f"Erro ao conectar: {err}")

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Conexão fechada.")
