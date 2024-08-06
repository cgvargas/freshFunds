# models/produto_dao.py

import mysql.connector

class ProductDAO:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def get_all_products(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM produtos")
        products = cursor.fetchall()
        cursor.close()
        return products

    def add_product(self, descricao, valor_unitario, id_tipos_produto):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO produtos (descricao, valor_unitario, id_tipos_produto) VALUES (%s, %s, %s)",
            (descricao, valor_unitario, id_tipos_produto)
        )
        self.connection.commit()
        cursor.close()

    def close_connection(self):
        self.connection.close()
