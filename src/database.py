import mysql.connector
import json


class Database:
    def __init__(self):
        self.connect("src/database_credentials.json")

    def connect(self, filepath):
        with open(filepath, "r") as file:
            credentials = json.load(file)

            self.connection = mysql.connector.connect(
                host=credentials["host"],
                user=credentials["user"],
                password=credentials["password"],
                database=credentials["database"]
            )
            self.cursor = self.connection.cursor()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            self.connection.rollback()
            return False

    def fetch_data(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def test_connection(self):
        query = "SELECT VERSION()"
        return self.fetch_data(query)


# data = Database()
# query = "select * from users;"
# query2 = "select * from books;"
# print(data.fetch_data(query2))
