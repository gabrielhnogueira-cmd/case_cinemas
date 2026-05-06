from src.database.connection import ConnectionFactory


def create_tables():
    connection = ConnectionFactory.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            genero TEXT NOT NULL,
            duracao INTEGER NOT NULL,
            classificacao TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

    print("Tabelas criadas com sucesso!")