import sqlite3


class Model:

    
    def __init__(self):

        self._connection = sqlite3.connect('Clientes.db')

    
    def disconnect(self):

        self._connection.close()

    
    def create_table(self):

        print('\nCriando tabela Clientes')
        cursor = self._connection.cursor()
        sql = "CREATE TABLE IF NOT EXISTS Clientes (nome TEXT NOT NULL, cpf INTEGER(11) PRIMARY KEY NOT NULL, data_nascimento TEXT, endereco TEXT, cidade TEXT, uf VARCHAR(2) NOT NULL, telefone TEXT, email TEXT NOT NULL)"
        cursor.execute(sql)
        self._connection.commit()

        print('\nTabela Clientes criada com sucesso.')

    
    def create_item(self, nome, cpf, data_nascimento, endereco, cidade, uf, telefone, email):

        cursor = self._connection.cursor()
        sql = "INSERT INTO Clientes (nome, cpf, data_nascimento, endereco, cidade, uf, telefone, email) VALUES " + "( '" + nome + "', '" + str(cpf) + "', '" + data_nascimento + "', '" + endereco + "', '" + cidade + "', '" + uf + "', '" + telefone + "', '" + email + "')"
        cursor.execute(sql)
        self._connection.commit()

        print('\nDados do cliente de cpf ' + str(cpf) + ' inseridos com sucesso.')

    def read_items(self):
        """
        Lê os valores: nome | email | telefone

        retorna list de clientes
        """

        print('\nConsultando no banco...')
        cursor = self._connection.cursor()
        sql = "SELECT nome, email, telefone FROM Clientes"
        cursor.execute(sql)

        return cursor.fetchall()

    def read_all_for_item(self, cpf) -> list:
        """
        Lê todos os valores dos clientes
        """

        print('\nConsultando no banco...')
        cursor = self._connection.cursor()
        sql = "SELECT nome, data_nascimento, endereco, cidade, uf, telefone, email FROM Clientes WHERE cpf = '" + str(cpf) + "'"
        cursor.execute(sql)

        data = cursor.fetchone()

        return data[0], data[1], data[2], data[3], data[4], data[5], data[6]

    
    def update_item(self, nome, cpf, data_nascimento, endereco, cidade, uf, telefone, email):

        cursor = self._connection.cursor()
        sql = "UPDATE Clientes SET nome  = '" + nome + "', data_nascimento = '" + data_nascimento+ "', endereco = '" + endereco + "', cidade = '" + cidade + "', uf = '" + uf + "', telefone = '" + telefone + "', email = '" + email +"' WHERE Clientes.cpf = "+str(cpf)
        cursor.execute(sql)

        self._connection.commit()
        print('\nDados do clinte de cpf ' + str(cpf) + ' atualizados com sucesso.')

    
    def delete_item(self, cpf):

        cursor = self._connection.cursor()
        sql = "DELETE FROM Clientes WHERE cpf = '"+ str(cpf) + "'"
        cursor.execute(sql)

        self._connection.commit()

        print('\nRegistro excluído: ' + cpf)