### MENU PARA PRUEBAS DE INTERFACES ###
### MENU PARA PRUEBAS DE INTERFACES ###
### MENU PARA PRUEBAS DE INTERFACES ###

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
import sys, csv
from VentanaIngresarCliente import VentanaIngresarCliente
from VentanaEditarCliente import VentanaEditarCliente
from VentanaComprarMedicamentos import VentanaComprarMedicamentos

class VentanaMain(object):
    def setupUi(self, VentanaMain):
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        ImagenFondo = QtGui.QPixmap('Imagenes/menu.png')
        
        VentanaMain.setWindowIcon(IconoTitulo)
        
        VentanaMain.resize(700, 395)
        VentanaMain.setMinimumSize(QtCore.QSize(700, 395))
        VentanaMain.setMaximumSize(QtCore.QSize(700, 395))
        
        # Etiqueta imagen superior
        self.imagen_fondoLabel = QtWidgets.QLabel(VentanaMain)
        self.imagen_fondoLabel.setGeometry(QtCore.QRect(0, 0, 700, 395))
        self.imagen_fondoLabel.setText("")
        self.imagen_fondoLabel.setPixmap(ImagenFondo)
        
        # Boton Ingresar Cliente
        self.BtnIngresarCliente = QtWidgets.QPushButton(VentanaMain)
        self.BtnIngresarCliente.setGeometry(QtCore.QRect(115, 151, 200, 50))
        self.BtnIngresarCliente.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnIngresarCliente.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Editar Cliente
        self.BtnEditarCliente = QtWidgets.QPushButton(VentanaMain)
        self.BtnEditarCliente.setGeometry(QtCore.QRect(358, 151, 200, 50))
        self.BtnEditarCliente.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnEditarCliente.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton AgregarMedicamentos
        self.BtnAgregarMedicamentos = QtWidgets.QPushButton(VentanaMain)
        self.BtnAgregarMedicamentos.setGeometry(QtCore.QRect(115, 228, 443, 50))
        self.BtnAgregarMedicamentos.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnAgregarMedicamentos.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Cerrar Menu
        self.BtnCerrarMenu = QtWidgets.QPushButton(VentanaMain)
        self.BtnCerrarMenu.setGeometry(QtCore.QRect(648, 10, 40, 40))
        self.BtnCerrarMenu.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnCerrarMenu.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Acción clickear botones
        self.BtnIngresarCliente.clicked.connect(self.onActionBtnIngresarCliente)
        self.BtnEditarCliente.clicked.connect(self.onActionBtnEditarCliente)
        self.BtnAgregarMedicamentos.clicked.connect(self.onActionBtnAgregarMedicamentos)
        self.BtnCerrarMenu.clicked.connect(VentanaMain.close)
        
        self.retranslateUi(VentanaMain)
        QtCore.QMetaObject.connectSlotsByName(VentanaMain)

    def retranslateUi(self, VentanaMain):
        _translate = QtCore.QCoreApplication.translate
        VentanaMain.setWindowTitle(_translate("VentanaMain", "Menu Inicial - Farmacia CVI"))
        
    def onActionBtnIngresarCliente(self):
        self.VentanaIngresarCliente = QtWidgets.QMainWindow()
        self.ui = VentanaIngresarCliente()
        self.ui.setupUi(self.VentanaIngresarCliente)
        self.VentanaIngresarCliente.show()
        
    def onActionBtnEditarCliente(self):
        self.VentanaEditarCliente = QtWidgets.QMainWindow()
        self.ui = VentanaEditarCliente()
        self.ui.setupUi(self.VentanaEditarCliente)
        self.VentanaEditarCliente.show()

    def onActionBtnAgregarMedicamentos(self):
        self.VentanaComprarMedicamentos = QtWidgets.QMainWindow()
        self.ui = VentanaComprarMedicamentos()
        self.ui.setupUi(self.VentanaComprarMedicamentos)
        self.VentanaComprarMedicamentos.show()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = VentanaMain()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())