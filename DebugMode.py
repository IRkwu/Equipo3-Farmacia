import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MenuSeleccion import MenuSeleccion
from VentanaIngresarCliente import VentanaIngresarCliente

class DebugMode(object):
    def setupUi(self, DebugMode):
        DebugMode.setObjectName("DebugMode")
        DebugMode.resize(400, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(DebugMode)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.PanelGrid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.PanelGrid.setContentsMargins(0, 0, 0, 0)
        self.Boton1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PanelGrid.addWidget(self.Boton1, 0, 0, 1, 1)
        self.Boton2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PanelGrid.addWidget(self.Boton2, 0, 1, 1, 1)
        self.Boton3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PanelGrid.addWidget(self.Boton3, 0, 2, 1, 1)
        self.Boton4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PanelGrid.addWidget(self.Boton4, 1, 0, 1, 1)
        self.Boton5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PanelGrid.addWidget(self.Boton5, 1, 1, 1, 1)
        self.Boton6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PanelGrid.addWidget(self.Boton6, 1, 2, 1, 1)
        self.Boton7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PanelGrid.addWidget(self.Boton7, 2, 0, 1, 1)
        self.Boton8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PanelGrid.addWidget(self.Boton8, 2, 1, 1, 1)
        self.Boton9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PanelGrid.addWidget(self.Boton9, 2, 2, 1, 1)
        
        # Agrandar botones
        botones = [self.Boton1, self.Boton2, self.Boton3, self.Boton4, self.Boton5, self.Boton6, self.Boton7, self.Boton8, self.Boton9]
        for boton in botones:
            boton.setFixedHeight(2 * boton.height())
            
        # Acción clickear botones
        self.Boton1.clicked.connect(self.onActionBoton1)
        self.Boton2.clicked.connect(self.onActionBoton2)
        self.Boton3.clicked.connect(self.onActionBoton3)
        self.Boton4.clicked.connect(self.onActionBoton4)
        self.Boton5.clicked.connect(self.onActionBoton5)
        self.Boton6.clicked.connect(self.onActionBoton6)
        self.Boton7.clicked.connect(self.onActionBoton7)
        self.Boton8.clicked.connect(self.onActionBoton8)
        self.Boton9.clicked.connect(self.onActionBoton9)

        self.retranslateUi(DebugMode)
        QtCore.QMetaObject.connectSlotsByName(DebugMode)

    def retranslateUi(self, DebugMode):
        _translate = QtCore.QCoreApplication.translate
        DebugMode.setWindowTitle(_translate("DebugMode", "Debug Mode"))
        self.Boton1.setText(_translate("DebugMode", "Ingresar Cliente"))
        self.Boton2.setText(_translate("DebugMode", "Menu Seleccion"))
        self.Boton3.setText(_translate("DebugMode", "Boton3"))
        self.Boton4.setText(_translate("DebugMode", "Boton4"))
        self.Boton5.setText(_translate("DebugMode", "Boton5"))
        self.Boton6.setText(_translate("DebugMode", "Boton6"))
        self.Boton7.setText(_translate("DebugMode", "Boton7"))
        self.Boton8.setText(_translate("DebugMode", "Boton8"))
        self.Boton9.setText(_translate("DebugMode", "Boton9"))
        
    def onActionBoton1(self):
        self.VentanaIngresarCliente = QtWidgets.QMainWindow()
        self.ui = VentanaIngresarCliente()
        self.ui.setupUi(self.VentanaIngresarCliente)
        self.VentanaIngresarCliente.show()
        
    def onActionBoton2(self):
        self.MenuSeleccion = QtWidgets.QMainWindow()
        self.ui = MenuSeleccion()
        self.ui.setupUi(self.MenuSeleccion)
        self.MenuSeleccion.show()

    def onActionBoton3(self):
        print("Se ha hecho clic en Boton3")

    def onActionBoton4(self):
        print("Se ha hecho clic en Boton4")

    def onActionBoton5(self):
        print("Se ha hecho clic en Boton5")

    def onActionBoton6(self):
        print("Se ha hecho clic en Boton6")

    def onActionBoton7(self):
        print("Se ha hecho clic en Boton7")

    def onActionBoton8(self):
        print("Se ha hecho clic en Boton8")

    def onActionBoton9(self):
        print("Se ha hecho clic en Boton9") 
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = DebugMode()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())