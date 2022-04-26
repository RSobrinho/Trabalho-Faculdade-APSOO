import sqlite3


class Model:

    
    def __init__(self):

        self._connection = sqlite3.connect('Clientes.db')

    
    def disconnect(self):

        print('Desconectando...')
        self._connection.close()
        print('Banco desconectado.')

    
    def create_table(self, table_name):

        cursor = self._connection.cursor()
        sql = "CREATE TABLE IF NOT EXISTS Clientes (nome TEXT NOT NULL, cpf INTEGER(11) PRIMARY KEY NOT NULL, data_nascimento TEXT, endereco TEXT, cidade TEXT, uf VARCHAR(2) NOT NULL, telefone TEXT, email TEXT NOT NULL)"
        cursor.execute(sql)

        print('Tabela {} criada com sucesso.'.format(table_name))

    
    def create_item(self, nome, cpf, data_nascimento, endereco, cidade, uf, telefone, email):

        cursor = self._connection.cursor()
        sql = "INSERT INTO Clientes (nome, cpf, data_nascimento, endereco, cidade, uf, telefone, email) VALUES " + "( " + nome + ", " + str(cpf) + ", " + data_nascimento + ", " + endereco + ", " + cidade + ", " + uf + ", " + telefone + ", " + email + ")"
        cursor.execute(sql)
        self._connection.commit()

        print('Dados inseridos com sucesso.')


    def read_items(self):

        cursor = self._connection.cursor()
        sql = "SELECT * FROM Clientes"
        cursor.execute(sql)

        return cursor.fetchall()

    
    def update_item(self, nome, cpf, data_nascimento, endereco, cidade, uf, telefone, email):

        cursor = self._connection.cursor()
        sql = "UPDATE Clientes SET nome  = " + nome + ", data_nascimento = " + data_nascimento+ ", endereco = " + endereco + ", cidade = " + cidade + ", uf = " + uf + ", telefone = " + telefone + ", email = " + email +" WHERE Clientes.cpf = "+str(cpf)
        cursor.execute(sql)

        self._connection.commit()
        print('Dados atualizados com sucesso.')

    
    def delete_item(self, cpf):

        cursor = self._connection.cursor()
        sql = "DELETE FROM Clientes WHERE cpf = "+ str(cpf)
        cursor.execute(sql)

        self._connection.commit()

        print('Registro excluído com sucesso.')