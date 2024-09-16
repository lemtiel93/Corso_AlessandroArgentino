import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    port = 8889,
    database = "esercitazionepython"
)

mycursor = mydb.cursor()

def inserici_dati():
    sql = "insert into utenti (nome, cognome) values(%s , %s)"
    val = ("Mirko" , "Antonioni")

    mycursor.execute(sql , val)

    mydb.commit()

    print(mycursor.lastrowid)

def delete(id):
    sql = "delete from utenti where id = %s"

    mycursor.execute(sql , (id,))
    
    mydb.commit()
    print(mycursor.rowcount,"righe eliminate")
    
def selezione():
    sql = "select * from utenti where id > 3"
    mycursor.execute(sql)

    dati = mycursor.fetchall()

    for dato in dati:
        print(dato)


        
delete(3)