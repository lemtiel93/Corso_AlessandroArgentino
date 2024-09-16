import mysql.connector

def create_admin_table():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="studenti",
        port = 8889 
    )

    mycursor = mydb.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        admin BOOLEAN NOT NULL
    );
    """

    mycursor.execute(sql)
    
     
    