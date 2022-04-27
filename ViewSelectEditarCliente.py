# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectEditarCliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_selectEditarCliente(object):
    def setupUi(self, selectEditarCliente):
        selectEditarCliente.setObjectName("selectEditarCliente")
        selectEditarCliente.resize(1280, 720)
        selectEditarCliente.setMinimumSize(QtCore.QSize(1280, 720))
        selectEditarCliente.setMaximumSize(QtCore.QSize(1280, 720))
        selectEditarCliente.setStyleSheet("background: white;")
        self.centralwidget = QtWidgets.QWidget(selectEditarCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_Box = QtWidgets.QFrame(self.centralwidget)
        self.frame_Box.setMaximumSize(QtCore.QSize(300, 200))
        self.frame_Box.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 245, 207);")
        self.frame_Box.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Box.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Box.setObjectName("frame_Box")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_Box)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame_Box)
        self.label.setMaximumSize(QtCore.QSize(250, 40))
        self.label.setStyleSheet("font-size: 17px;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame_BotaoLineEdit = QtWidgets.QFrame(self.frame_Box)
        self.frame_BotaoLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_BotaoLineEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_BotaoLineEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_BotaoLineEdit.setObjectName("frame_BotaoLineEdit")
        self.pushButton_botaoConfirmar = QtWidgets.QPushButton(self.frame_BotaoLineEdit)
        self.pushButton_botaoConfirmar.setGeometry(QtCore.QRect(65, 80, 150, 40))
        self.pushButton_botaoConfirmar.setMaximumSize(QtCore.QSize(150, 40))
        self.pushButton_botaoConfirmar.setStyleSheet("background: white;\n"
"border: 1px solid #FFD580;\n"
"font-size: 20px;")
        self.pushButton_botaoConfirmar.setObjectName("pushButton_botaoConfirmar")
        self.lineCPF = QtWidgets.QLineEdit(self.frame_BotaoLineEdit)
        self.lineCPF.setGeometry(QtCore.QRect(40, 20, 200, 35))
        self.lineCPF.setMaximumSize(QtCore.QSize(200, 35))
        self.lineCPF.setStyleSheet("background-color: #FFD580;\n"
"font-size: 18px;")
        self.lineCPF.setText("")
        self.lineCPF.setObjectName("lineCPF")
        self.verticalLayout.addWidget(self.frame_BotaoLineEdit)
        self.horizontalLayout.addWidget(self.frame_Box)
        selectEditarCliente.setCentralWidget(self.centralwidget)

        self.retranslateUi(selectEditarCliente)
        QtCore.QMetaObject.connectSlotsByName(selectEditarCliente)

    def retranslateUi(self, selectEditarCliente):
        _translate = QtCore.QCoreApplication.translate
        selectEditarCliente.setWindowTitle(_translate("selectEditarCliente", "MainWindow"))
        self.label.setText(_translate("selectEditarCliente", "SELECIONAR CLIENTE POR CPF:"))
        self.pushButton_botaoConfirmar.setText(_translate("selectEditarCliente", "Confirmar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selectEditarCliente = QtWidgets.QMainWindow()
    ui = Ui_selectEditarCliente()
    ui.setupUi(selectEditarCliente)
    selectEditarCliente.show()
    sys.exit(app.exec_())