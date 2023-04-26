from PyQt5 import QtCore, QtGui, QtWidgets
from Clases.Cliente import Cliente

class RegistrarCliente(object):
    def setupUi(self, Ventana):
        Ventana.resize(1000, 600)
        
        self.formLayoutWidget = QtWidgets.QWidget(Ventana)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 130, 340, 460))
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        
        # Etiqueta nombre y linetext
        self.nombresLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nombresLabel)
        self.nombresLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nombresLineEdit)
        
        # Etiqueta apellidos y linetext
        self.apellidosLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.apellidosLabel)
        self.apellidosLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.apellidosLineEdit)
        
        # Etiqueta domicilio y linetext
        self.domicilioLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.domicilioLabel)
        self.domicilioLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.domicilioLineEdit)
        
        # Etiqueta genero y combobox
        self.generoLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.generoLabel)
        self.generoComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.generoComboBox.addItem("")
        self.generoComboBox.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.generoComboBox)
        
        # Etiqueta fecha de nacimiento y linetext
        self.fecha_nacimientoLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.fecha_nacimientoLabel)
        self.fecha_nacimientoLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.fecha_nacimientoLineEdit)
        
        # Etiqueta rut y linetext
        self.rutLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.rutLabel)
        self.rutLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.rutLineEdit)
        
        # Etiqueta email y linetext
        self.emailLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.emailLabel)
        self.emailLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.emailLineEdit)
        
        # Etiqueta telefono y linetext
        self.telefonoLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.telefonoLabel)
        self.telefonoLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.telefonoLineEdit)
        
        # Etiqueta ingresar datos
        self.LabelParaIngresar = QtWidgets.QLabel(Ventana)
        self.LabelParaIngresar.setGeometry(QtCore.QRect(30, 90, 300, 30))
        
        # Etiqueta titulo farmacia veterinaria
        self.LabelFarmaciaVeterinaria = QtWidgets.QLabel(Ventana)
        self.LabelFarmaciaVeterinaria.setGeometry(QtCore.QRect(120, 20, 760, 50))
        self.LabelFarmaciaVeterinaria.setAlignment(QtCore.Qt.AlignCenter)
        
        # Boton regresar
        self.BotonRegresar = QtWidgets.QPushButton(Ventana)
        self.BotonRegresar.setGeometry(QtCore.QRect(20, 20, 80, 60))
        
        # Etiqueta titulo desc
        self.TituloDescripcion = QtWidgets.QLabel(Ventana)
        self.TituloDescripcion.setGeometry(QtCore.QRect(510, 120, 340, 30))
        self.TituloDescripcion.setAlignment(QtCore.Qt.AlignCenter)
        
        # Boton guardar datos1
        self.BotonGuardarDatos = QtWidgets.QPushButton(self.formLayoutWidget)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.BotonGuardarDatos)
        
        # Etiqueta descripcion
        self.LabelDescripcion = QtWidgets.QLabel(Ventana)
        self.LabelDescripcion.setGeometry(QtCore.QRect(390, 180, 580, 390))
        self.LabelDescripcion.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        
        # Cambiar el tamaño de los elementos en el formLayoutWidget
        self.nombresLabel.setFixedHeight(int(1.4 * self.nombresLabel.height()))
        self.nombresLineEdit.setFixedHeight(int(1.4 * self.nombresLineEdit.height()))
        self.apellidosLabel.setFixedHeight(int(1.4 * self.apellidosLabel.height()))
        self.apellidosLineEdit.setFixedHeight(int(1.4 * self.apellidosLineEdit.height()))
        self.domicilioLabel.setFixedHeight(int(1.4 * self.domicilioLabel.height()))
        self.domicilioLineEdit.setFixedHeight(int(1.4 * self.domicilioLineEdit.height()))
        self.generoLabel.setFixedHeight(int(1.4 * self.generoLabel.height()))
        self.generoComboBox.setFixedHeight(int(1.4 * self.generoComboBox.height()))
        self.fecha_nacimientoLabel.setFixedHeight(int(1.4 * self.fecha_nacimientoLabel.height()))
        self.fecha_nacimientoLineEdit.setFixedHeight(int(1.4 * self.fecha_nacimientoLineEdit.height()))
        self.rutLabel.setFixedHeight(int(1.4 * self.rutLabel.height()))
        self.rutLineEdit.setFixedHeight(int(1.4 * self.rutLineEdit.height()))
        self.emailLabel.setFixedHeight(int(1.4 * self.emailLabel.height()))
        self.emailLineEdit.setFixedHeight(int(1.4 * self.emailLineEdit.height()))
        self.telefonoLabel.setFixedHeight(int(1.4 * self.telefonoLabel.height()))
        self.telefonoLineEdit.setFixedHeight(int(1.4 * self.telefonoLineEdit.height()))
        self.BotonGuardarDatos.setFixedHeight(int(1.8 * self.BotonGuardarDatos.height()))

        self.retranslateUi(Ventana)
        QtCore.QMetaObject.connectSlotsByName(Ventana)
        
        self.BotonGuardarDatos.clicked.connect(self.onActionBotonGuardar)
        self.BotonRegresar.clicked.connect(Ventana.close)        

    # Definiendo textos
    def retranslateUi(self, Ventana):
        _translate = QtCore.QCoreApplication.translate
        Ventana.setWindowTitle("Ventana - Ingresar Datos")
        self.nombresLabel.setText("Nombres:")
        self.apellidosLabel.setText("Apellidos:")
        self.domicilioLabel.setText("Domicilio:")
        self.generoLabel.setText("Genero:")
        self.fecha_nacimientoLabel.setText("Fecha de Nacimiento:\n(DD/MM/AAAA)")
        self.rutLabel.setText("Rut:\n(XX.XXX.XXX-X)")
        self.emailLabel.setText("Email:")
        self.telefonoLabel.setText("Teléfono:\n(+56 X XXXX XXXX)")
        self.BotonGuardarDatos.setText("Registrar Datos")
        self.generoComboBox.setItemText(0,"Masculino")
        self.generoComboBox.setItemText(1,"Femenino")
        self.LabelParaIngresar.setText("Para ingresar necesita introducir sus Datos")
        self.LabelFarmaciaVeterinaria.setText("Farmacia Veterinaria")
        self.BotonRegresar.setText("Regresar al \nmenu anterior")
        self.TituloDescripcion.setText("Descripción de la Farmacia")
        self.LabelDescripcion.setText("En la farmacia...")

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LabelParaIngresar.setFont(font)
        
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.LabelFarmaciaVeterinaria.setFont(font)
        
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.TituloDescripcion.setFont(font)
        
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelDescripcion.setFont(font)
        
    def onActionBotonGuardar(self):
        nombres = self.nombresLineEdit.text()
        apellidos = self.apellidosLineEdit.text()
        domicilio = self.domicilioLineEdit.text()
        genero = self.generoComboBox.currentText()
        fecha_nacimiento = self.fecha_nacimientoLineEdit.text()
        rut = self.rutLineEdit.text()
        email = self.emailLineEdit.text()
        telefono =self.telefonoLineEdit.text()
                
        Cliente.agregar_cliente(nombres, apellidos, domicilio, genero, fecha_nacimiento, rut, email, telefono)