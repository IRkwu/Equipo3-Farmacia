from PyQt5 import QtCore, QtGui, QtWidgets


class MenuSeleccion(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(540, 448)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 521, 431))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.PanelGrid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.PanelGrid.setContentsMargins(0, 0, 0, 0)
        self.PanelGrid.setObjectName("PanelGrid")
        self.BotonFarmacos = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PanelGrid.addWidget(self.BotonFarmacos, 2, 1, 1, 1)
        self.LabelQueDeseaComprar = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LabelQueDeseaComprar.setFont(font)
        self.LabelQueDeseaComprar.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.LabelQueDeseaComprar.setObjectName("LabelQueDeseaComprar")
        self.PanelGrid.addWidget(self.LabelQueDeseaComprar, 1, 0, 1, 2)
        self.BotonMedicamentos = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.BotonMedicamentos.setObjectName("BotonMedicamentos")
        self.PanelGrid.addWidget(self.BotonMedicamentos, 2, 0, 1, 1)
        self.LabelFarmaciaVeterinaria = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LabelFarmaciaVeterinaria.setFont(font)
        self.LabelFarmaciaVeterinaria.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelFarmaciaVeterinaria.setObjectName("LabelFarmaciaVeterinaria")
        self.PanelGrid.addWidget(self.LabelFarmaciaVeterinaria, 0, 0, 1, 2)
        self.BotonRecetaMedicamentos = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.BotonRecetaMedicamentos.setObjectName("BotonRecetaMedicamentos")
        self.PanelGrid.addWidget(self.BotonRecetaMedicamentos, 3, 0, 1, 1)
        self.BotonRecetaFarmacos = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.BotonRecetaFarmacos.setObjectName("BotonRecetaFarmacos")
        self.PanelGrid.addWidget(self.BotonRecetaFarmacos, 3, 1, 1, 1)
        
        self.BotonMedicamentos.setFixedHeight(10 * self.BotonMedicamentos.height())
        self.BotonFarmacos.setFixedHeight(10 * self.BotonFarmacos.height())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ventana seleccion compra"))
        self.BotonFarmacos.setText(_translate("Form", "Farmacos"))
        self.LabelQueDeseaComprar.setText(_translate("Form", "¿Que desea comprar?"))
        self.BotonMedicamentos.setText(_translate("Form", "Medicamentos"))
        self.LabelFarmaciaVeterinaria.setText(_translate("Form", "Farmacia Veterinaria"))
        self.BotonRecetaMedicamentos.setText(_translate("Form", "Con receta"))
        self.BotonRecetaFarmacos.setText(_translate("Form", "Con receta"))
