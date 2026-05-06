import sqlite3


class ConnectionFactory:

    @staticmethod
    def get_connection():
        connection = sqlite3.connect("case_cinemas.db")
        return connection