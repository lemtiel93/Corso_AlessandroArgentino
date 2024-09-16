import mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "root",
port = 8889,
database = "studenti"
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