# main.py

from models.product_dao import ProductDAO

def main():
    # Troque os valores por suas credenciais
    host = 'localhost'       # ou o IP do seu servidor MySQL
    user = 'admin'
    password = 'Oa023568910@'
    database = 'hortifruti_bd'

    # Criar uma instância do ProductDAO
    product_dao = ProductDAO(host, user, password, database)

    # Adicionar um produto (exemplo)
    product_dao.add_product("Produto Exemplo", 99.99, 1)  # Coloque o ID de tipos_produto apropriado
    print("Produto adicionado.")

    # Obter todos os produtos
    products = product_dao.get_all_products()
    print("Produtos no banco de dados:")
    for product in products:
        print(product)

    # Fechar a conexão
    product_dao.close_connection()

if __name__ == "__main__":
    main()
