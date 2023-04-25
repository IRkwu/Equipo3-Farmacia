from PyQt5 import QtCore, QtGui, QtWidgets


class IngresarDatos(object):
    def setupUi(self, Form):
        Form.resize(1000, 600)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
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
        self.fechaDeNacimientoLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.fechaDeNacimientoLabel)
        self.fechaDeNacimientoLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.fechaDeNacimientoLineEdit)
        
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
        self.LabelParaIngresar = QtWidgets.QLabel(Form)
        self.LabelParaIngresar.setGeometry(QtCore.QRect(30, 90, 300, 30))
        
        # Etiqueta titulo farmacia veterinaria
        self.LabelFarmaciaVeterinaria = QtWidgets.QLabel(Form)
        self.LabelFarmaciaVeterinaria.setGeometry(QtCore.QRect(120, 20, 760, 50))
        self.LabelFarmaciaVeterinaria.setAlignment(QtCore.Qt.AlignCenter)
        
        # Boton regresar
        self.BotonRegresar = QtWidgets.QPushButton(Form)
        self.BotonRegresar.setGeometry(QtCore.QRect(20, 20, 80, 60))
        
        # Etiqueta titulo desc
        self.TituloDescripcion = QtWidgets.QLabel(Form)
        self.TituloDescripcion.setGeometry(QtCore.QRect(510, 120, 340, 30))
        self.TituloDescripcion.setAlignment(QtCore.Qt.AlignCenter)
        
        # Boton guardar datos
        self.BotonGuardarDatos = QtWidgets.QPushButton(self.formLayoutWidget)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.BotonGuardarDatos)
        
        # Etiqueta descripcion
        self.LabelDescripcion = QtWidgets.QLabel(Form)
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
        self.fechaDeNacimientoLabel.setFixedHeight(int(1.4 * self.fechaDeNacimientoLabel.height()))
        self.fechaDeNacimientoLineEdit.setFixedHeight(int(1.4 * self.fechaDeNacimientoLineEdit.height()))
        self.rutLabel.setFixedHeight(int(1.4 * self.rutLabel.height()))
        self.rutLineEdit.setFixedHeight(int(1.4 * self.rutLineEdit.height()))
        self.emailLabel.setFixedHeight(int(1.4 * self.emailLabel.height()))
        self.emailLineEdit.setFixedHeight(int(1.4 * self.emailLineEdit.height()))
        self.telefonoLabel.setFixedHeight(int(1.4 * self.telefonoLabel.height()))
        self.telefonoLineEdit.setFixedHeight(int(1.4 * self.telefonoLineEdit.height()))
        self.BotonGuardarDatos.setFixedHeight(int(1.8 * self.BotonGuardarDatos.height()))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.BotonGuardarDatos.clicked.connect(self.onActionBotonGuardar)
        

    # Definiendo textos
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("Ventana - Ingresar Datos")
        self.nombresLabel.setText("Nombres:")
        self.apellidosLabel.setText("Apellidos:")
        self.domicilioLabel.setText("Domicilio:")
        self.generoLabel.setText("Genero:")
        self.fechaDeNacimientoLabel.setText("Fecha de Nacimiento:\n(DD/MM/AAAA)")
        self.rutLabel.setText("Rut:\n(XX.XXX.XXX-X)")
        self.emailLabel.setText("Email:")
        self.telefonoLabel.setText("Teléfono:\n(+56 X XXXX XXXX)")
        self.BotonGuardarDatos.setText("Guardar Datos")
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
        fechaDeNacimiento = self.fechaDeNacimientoLineEdit.text()
        rut = self.rutLineEdit.text()
        email = self.emailLineEdit.text()
        telefono =self.telefonoLineEdit.text()
        
        # Ejemplo consola
        print("Nombres:", nombres)
        print("Apellidos:", apellidos)
        print("Domicilio:", domicilio)
        print("Género:", genero)
        print("Fecha de Nacimiento:", fechaDeNacimiento)
        print("RUT:", rut)
        print("Email:", email)
        print("Teléfono:", telefono)
