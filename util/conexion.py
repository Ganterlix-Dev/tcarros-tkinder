import mysql.connector

try:
    def connect_to_db():
        conexion = mysql.connector.connect(
            user="root",
            passwd="",
            host="localhost",
            db="tcarros_db"
        )
        print("connected to db")
        return conexion
except Exception as err:
    print(err)