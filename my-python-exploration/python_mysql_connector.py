import mysql.connector
connection = mysql.connector.connect(host="localhost",user="root",password="1234")
if connection.is_connected():
    print("Connection eestablished")
