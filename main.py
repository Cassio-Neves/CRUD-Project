# Importação da biblioteca que integra com o MySQL
import mysql.connector




# Criando uma classe para a conexão
class CRUD:
    def __init__(self):
        # Globalizando os escopos da conexão e cursor para utlizarmos nos métodos principais do CRUD
        global conexao, cursor

        # Configurando para conectar com o banco de dados
        conexao = mysql.connector.connect(
            host= 'host',
            user= 'username',
            password= 'senha da conexão',
            database= 'nome do banco de dados'
        )
        # Esse é o cursor que vai alterar nosso banco de acordo com nossas necessidades
        cursor = conexao.cursor()

    

    
                

    #CRUD:
    #Create
    def create(self, nome_produto, price):
        comando = f'INSERT INTO sales (product_name, price) VALUES ("{nome_produto}", {price})'
        cursor.execute(comando)
        conexao.commit()

        

    
    #Read
    def read(self):
        comando = f'SELECT * FROM sales'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for linha in resultado:
            print(linha)
        if len(resultado) == 0:
            print('Empty List')
            
        

        

    #Update
    def update(self, nome_produto, price):
        comando = f'UPDATE sales SET price = {price} WHERE product_name = "{nome_produto}"'
        cursor.execute(comando)
        conexao.commit()
        
        

    #Delete
    def delete(self, id):
        comando = f'DELETE FROM sales WHERE id_sale = {id}'
        cursor.execute(comando)
        conexao.commit()
        
# Teste do programa
if __name__ == '__main__':
    teste = CRUD()
    teste.create('something expensive', 1000)
    teste.read()
    teste.update('something cheap', 10)
    teste.delete(1)