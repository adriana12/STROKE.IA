
import psycopg2
con = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="Nome_do_Banco",
    user="user",
    password="password")

cursor = con.cursor()
