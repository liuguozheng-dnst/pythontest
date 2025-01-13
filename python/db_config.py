import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        self.config = {
            'host': '10.73.219.95',
            'user': 'root',
            'password': 'Dnss1234',
            'database': 'asset_management'
        }

    def connect(self):
        try:
            connection = mysql.connector.connect(**self.config)
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"数据库连接错误: {e}")
            return None 