
from PyQt5 import QtCore, QtGui, QtWidgets
from colorama import Cursor
from model import Model
import sys, files_rc

class Controller():
    def __init__(self) -> None:
        
        self._app    = QtWidgets.QApplication(sys.argv)
        self._window = QtWidgets.QMainWindow()
        self._loop   = False
        con = Model()
        con.create_table()
        con.disconnect()

    ######### Controller #########

    def selecionar_usuario_para_edicao(self):
        from ViewSelectEditarCliente import Ui_selectEditarCliente

        ui = Ui_selectEditarCliente()
        ui.setupUi(self._window)

        ui.pushButton_botaoConfirmar.clicked.connect(lambda: self.editar(ui.lineCPF.text()))

        self._window.show()

    def editar(self, cpf):

        from ViewEditar import EditarCliente

        con = Model()
        nome, data_nascimento, endereco, cidade, estado, telefone, email = con.read_all_for_item(cpf)
        con.disconnect()

        ui = EditarCliente()
        ui.setupUi(self._window)

        ui.lineEdit_user.setText(nome)
        ui.lineEdit_user_2.setText(cpf)
        ui.lineEdit_user_3.setText(data_nascimento)
        ui.lineEdit_user_5.setText(endereco)
        ui.lineEdit_user_4.setText(cidade)
        ui.lineEdit_user_6.setText(estado)
        ui.lineEdit_user_8.setText(telefone)
        ui.lineEdit_user_7.setText(email)
        ui.pushButton_enter.clicked.connect(lambda: self.update_item(ui))


        self._window.show()

    def cadastrar(self):

        from ViewCadastrar import CadastrarCliente

        ui = CadastrarCliente()
        ui.setupUi(self._window)

        ui.pushButton_enter.clicked.connect(lambda: self.register_item(ui))


        self._window.show()

    def listar(self):

        from ViewListar import Ui_TelaListagemClientes

        con = Model()
        pessoas = con.read_items()
        con.disconnect()

        ui = Ui_TelaListagemClientes()
        ui.setupUi(self._window)

        ui.tableWidget_TabelaPessoas.setRowCount(len(pessoas))

        for row in range(len(pessoas)):
            ui.tableWidget_TabelaPessoas.setRowHeight(row, 50)
            for coluna in range(3):
                ui.tableWidget_TabelaPessoas.setItem(row, coluna, QtWidgets.QTableWidgetItem(pessoas[row][coluna]))

        ui.pushButton_Sair.clicked.connect(self._app.exit)
        ui.pushButton_Excluir.clicked.connect(self.deletar)
        ui.pushButton_Alterar.clicked.connect(self.selecionar_usuario_para_edicao)
        ui.pushButton_Cadastrar.clicked.connect(self.cadastrar)

        self._window.show()
        if not self._loop:
            self._loop = True
            sys.exit(self._app.exec_())

        
    def deletar(self):

        from ViewDeletar import Ui_DeletarCliente

        ui = Ui_DeletarCliente()
        ui.setupUi(self._window)

        ui.pushButton_botaoConfirmar.clicked.connect(lambda: self.delete_item(ui))

        self._window.show()

    ######### Service #########

    def delete_item(self, ui):
    
        cpf = ui.lineEdit.text()

        con = Model()
        con.delete_item(cpf)
        con.disconnect()

        self.listar()

    def update_item(self, ui):

        nome            = ui.lineEdit_user.text()
        cpf             = ui.lineEdit_user_2.text()
        data_nascimento = ui.lineEdit_user_3.text()
        endereco        = ui.lineEdit_user_5.text()
        cidade          = ui.lineEdit_user_4.text()
        estado          = ui.lineEdit_user_6.text()
        telefone        = ui.lineEdit_user_8.text()
        email           = ui.lineEdit_user_7.text()

        con = Model()
        con.update_item(nome, cpf, data_nascimento, endereco, cidade, estado, telefone, email)
        con.disconnect()

        self.listar()

    def register_item(self, ui):

        nome            = ui.lineEdit_user.text()
        cpf             = ui.lineEdit_user_2.text()
        data_nascimento = ui.lineEdit_user_3.text()
        endereco        = ui.lineEdit_user_5.text()
        cidade          = ui.lineEdit_user_4.text()
        estado          = ui.lineEdit_user_6.text()
        telefone        = ui.lineEdit_user_8.text()
        email           = ui.lineEdit_user_7.text()

        con = Model()
        con.create_item(nome, cpf, data_nascimento, endereco, cidade, estado, telefone, email)
        con.disconnect()

        self.listar()