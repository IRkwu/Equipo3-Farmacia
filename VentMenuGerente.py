
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
from VentIngresarCliente import VentIngresarCliente
from VentListaClientes import VentListaClientes
from VentComprarMedicamentos import VentComprarMedicamentos
from VentIngresarUsuario import VentIngresarUsuario
from VentModificarStock import VentModificarStock

class VentMenuGerente(object):
    def setupUi(self, VentMenuGerente):
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        ImagenFondo = QtGui.QPixmap('Imagenes/menu_gerente.png')
        
        VentMenuGerente.setWindowIcon(IconoTitulo)
        
        VentMenuGerente.resize(700, 395)
        VentMenuGerente.setMinimumSize(QtCore.QSize(700, 395))
        VentMenuGerente.setMaximumSize(QtCore.QSize(700, 395))
        
        # Etiqueta imagen fondo
        self.imagen_fondoLabel = QtWidgets.QLabel(VentMenuGerente)
        self.imagen_fondoLabel.setGeometry(QtCore.QRect(0, 0, 700, 395))
        self.imagen_fondoLabel.setText("")
        self.imagen_fondoLabel.setPixmap(ImagenFondo)
        
        # Boton Ingresar Cliente
        self.BtnIngresarCliente = QtWidgets.QPushButton(VentMenuGerente)
        self.BtnIngresarCliente.setGeometry(QtCore.QRect(115, 151, 200, 50))
        self.BtnIngresarCliente.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnIngresarCliente.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Editar Cliente
        self.BtnEditarCliente = QtWidgets.QPushButton(VentMenuGerente)
        self.BtnEditarCliente.setGeometry(QtCore.QRect(358, 151, 200, 50))
        self.BtnEditarCliente.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnEditarCliente.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Editar Cliente
        self.BtnIngresarUsuario = QtWidgets.QPushButton(VentMenuGerente)
        self.BtnIngresarUsuario.setGeometry(QtCore.QRect(115, 228, 200, 50))
        self.BtnIngresarUsuario.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnIngresarUsuario.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Editar Cliente
        self.BtnCarrito = QtWidgets.QPushButton(VentMenuGerente)
        self.BtnCarrito.setGeometry(QtCore.QRect(358, 228, 200, 50))
        self.BtnCarrito.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnCarrito.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton AgregarMedicamentos
        self.BtnModificarStock = QtWidgets.QPushButton(VentMenuGerente)
        self.BtnModificarStock.setGeometry(QtCore.QRect(115, 311, 443, 50))
        self.BtnModificarStock.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnModificarStock.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Cerrar Menu
        self.BtnCerrarMenu = QtWidgets.QPushButton(VentMenuGerente)
        self.BtnCerrarMenu.setGeometry(QtCore.QRect(648, 10, 40, 40))
        self.BtnCerrarMenu.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnCerrarMenu.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Acción clickear botones
        self.BtnIngresarCliente.clicked.connect(lambda: self.cambiarVent(VentIngresarCliente))
        self.BtnEditarCliente.clicked.connect(lambda: self.cambiarVent(VentListaClientes))
        self.BtnIngresarUsuario.clicked.connect(lambda: self.cambiarVent(VentIngresarUsuario))
        self.BtnCarrito.clicked.connect(lambda: self.cambiarVent(VentComprarMedicamentos))
        self.BtnModificarStock.clicked.connect(lambda: self.cambiarVent(VentModificarStock))
        self.BtnCerrarMenu.clicked.connect(VentMenuGerente.close)
        
        
        self.retranslateUi(VentMenuGerente)
        QtCore.QMetaObject.connectSlotsByName(VentMenuGerente)

    def retranslateUi(self, VentMenuGerente):
        _translate = QtCore.QCoreApplication.translate
        VentMenuGerente.setWindowTitle(_translate("VentMenuGerente", "Menu Gerente"))

    def cambiarVent(self, nombre_Vent):
        self.nombre_Vent = QtWidgets.QMainWindow()
        self.ui = nombre_Vent()
        self.ui.setupUi(self.nombre_Vent)
        self.nombre_Vent.show()