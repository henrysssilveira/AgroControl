import mysql.connector
import pprint
from pprint import pprint

conn = mysql.connector.connect(
        host="localhost",
        user="henrique",
        password="1234",
        database="erp_agro"
    )

cursor = conn.cursor(dictionary=True)
cursor.execute('SELECT * FROM usuarios')

usuarios = cursor.fetchall()

pprint(usuarios)

cursor.close()
conn.close()