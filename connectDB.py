import mysql.connector
from mysql.connector import Error

# connect to MySQL database
def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "root", "")

host_name='localhost'
database ='test'
user_name = 'root'
user_password='abcd1234'
# main code
create_connection(host_name, user_name, user_password)
