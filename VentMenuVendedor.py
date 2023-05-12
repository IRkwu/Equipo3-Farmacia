from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
from VentIngresarCliente import VentIngresarCliente
from VentComprarMedicamentos import VentComprarMedicamentos

class VentMenuVendedor(object):
    def setupUi(self, VentMenuVendedor):
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        ImagenFondo = QtGui.QPixmap('Imagenes/menu_vendedor.png')
        
        VentMenuVendedor.setWindowIcon(IconoTitulo)
        
        VentMenuVendedor.resize(700, 395)
        VentMenuVendedor.setMinimumSize(QtCore.QSize(700, 395))
        VentMenuVendedor.setMaximumSize(QtCore.QSize(700, 395))
        
        # Etiqueta imagen fondo
        self.imagen_fondoLabel = QtWidgets.QLabel(VentMenuVendedor)
        self.imagen_fondoLabel.setGeometry(QtCore.QRect(0, 0, 700, 395))
        self.imagen_fondoLabel.setText("")
        self.imagen_fondoLabel.setPixmap(ImagenFondo)
        
        # Boton Ingresar Cliente
        self.BtnIngresarCliente = QtWidgets.QPushButton(VentMenuVendedor)
        self.BtnIngresarCliente.setGeometry(QtCore.QRect(115, 211, 200, 50))
        self.BtnIngresarCliente.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnIngresarCliente.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Carrito
        self.BtnCarrito = QtWidgets.QPushButton(VentMenuVendedor)
        self.BtnCarrito.setGeometry(QtCore.QRect(358, 211, 200, 50))
        self.BtnCarrito.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnCarrito.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Boton Cerrar Menu
        self.BtnCerrarMenu = QtWidgets.QPushButton(VentMenuVendedor)
        self.BtnCerrarMenu.setGeometry(QtCore.QRect(648, 10, 40, 40))
        self.BtnCerrarMenu.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.BtnCerrarMenu.setCursor(QtCore.Qt.PointingHandCursor)
        
        # Acción clickear botones
        self.BtnIngresarCliente.clicked.connect(lambda: self.cambiarVent(VentIngresarCliente))
        self.BtnCarrito.clicked.connect(lambda: self.cambiarVent(VentComprarMedicamentos))
        self.BtnCerrarMenu.clicked.connect(VentMenuVendedor.close)
        
        self.retranslateUi(VentMenuVendedor)
        QtCore.QMetaObject.connectSlotsByName(VentMenuVendedor)

    def retranslateUi(self, VentMenuVendedor):
        _translate = QtCore.QCoreApplication.translate
        VentMenuVendedor.setWindowTitle(_translate("VentMenuVendedor", "Menu Inicial - Farmacia CVI"))
        
    def cambiarVent(self, nombre_Vent):
        self.nombre_Vent = QtWidgets.QMainWindow()
        self.ui = nombre_Vent()
        self.ui.setupUi(self.nombre_Vent)
        self.nombre_Vent.show()