from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator, QFont, QIcon
from PyQt5.QtWidgets import QMessageBox
from Clases.Cliente import Cliente

class VentIngresarCliente(object):
    def setupUi(self, VentIngresarCliente):
        ImagenBanner = QtGui.QPixmap('Imagenes/banner_cvi.png')
        IconoRegresar = QtGui.QIcon('Imagenes/boton_regresar.png')
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        
        VentIngresarCliente.setWindowIcon(IconoTitulo)
        
        VentIngresarCliente.resize(800, 565)
        VentIngresarCliente.setMinimumSize(QtCore.QSize(800, 565))
        VentIngresarCliente.setMaximumSize(QtCore.QSize(800, 565))
        
        # Etiqueta nombres y LineEdit
        self.nombresLabel = QtWidgets.QLabel(VentIngresarCliente)
        self.nombresLabel.setGeometry(QtCore.QRect(14, 137, 42, 50))
        self.nombresLineEdit = QtWidgets.QLineEdit(VentIngresarCliente)
        self.nombresLineEdit.setGeometry(QtCore.QRect(106, 137, 260, 50))
        self.nombresLineEdit.setPlaceholderText("Ingrese Primer y segundo nombre")
        
        # Etiqueta apellidos y LineEdit
        self.apellidosLabel = QtWidgets.QLabel(VentIngresarCliente)
        self.apellidosLabel.setGeometry(QtCore.QRect(399, 137, 42, 50))
        self.apellidosLineEdit = QtWidgets.QLineEdit(VentIngresarCliente)
        self.apellidosLineEdit.setGeometry(QtCore.QRect(504, 137, 260, 50))
        self.apellidosLineEdit.setPlaceholderText("Ingrese apellido paterno y materno")

        # Etiqueta genero y ComboBox
        self.generoLabel = QtWidgets.QLabel(VentIngresarCliente)
        self.generoLabel.setGeometry(QtCore.QRect(14, 229, 35, 50))
        self.generoComboBox = QtWidgets.QComboBox(VentIngresarCliente)
        self.generoComboBox.setGeometry(QtCore.QRect(106, 229, 260, 50))
        self.generoComboBox.setMinimumSize(QtCore.QSize(260, 50))
        self.generoComboBox.setEditable(False)
        self.generoComboBox.addItem("")
        self.generoComboBox.addItem("")
        iconoHombre = QIcon("Imagenes/man.png")
        iconoMujer = QIcon("Imagenes/woman.png")
        self.generoComboBox.setItemIcon(0, iconoHombre)
        self.generoComboBox.setItemIcon(1, iconoMujer)

        # Etiqueta fecha_nacimiento y DateEdit
        self.fecha_nacimientoLabel = QtWidgets.QLabel(VentIngresarCliente)
        self.fecha_nacimientoLabel.setGeometry(QtCore.QRect(399, 229, 99, 50))
        self.fecha_nacimientoDateEdit = QtWidgets.QDateEdit(VentIngresarCliente)
        self.fecha_nacimientoDateEdit.setGeometry(QtCore.QRect(504, 229, 260, 50))
        
        # Etiqueta rut y LineEdit
        self.rutLabel = QtWidgets.QLabel(VentIngresarCliente)
        self.rutLabel.setGeometry(QtCore.QRect(14, 321, 17, 50))
        self.rutLineEdit = QtWidgets.QLineEdit(VentIngresarCliente)
        self.rutLineEdit.setGeometry(QtCore.QRect(106, 321, 200, 50))
        self.rutLineEdit.setMaxLength(8)
        self.rutLineEdit.setValidator(QIntValidator())
        self.rutLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]*")))
        self.rutLineEdit.setPlaceholderText("Ingrese rut sin puntos")
        
        # Etiqueta digito_verificador y LineEdit
        self.digito_verificadorLabel = QtWidgets.QLabel(VentIngresarCliente)
        self.digito_verificadorLabel.setGeometry(QtCore.QRect(312, 321, 17, 50))
        self.digito_verificadorLineEdit = QtWidgets.QLineEdit(VentIngresarCliente)
        self.digito_verificadorLineEdit.setGeometry(QtCore.QRect(326, 321, 40, 50))
        self.digito_verificadorLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9Kk]")))
        self.digito_verificadorLineEdit.setMaxLength(1)
        self.digito_verificadorLineEdit.setPlaceholderText("0-9 | K")
        
        # Etiqueta telefono y LineEdit
        self.telefonoLabel = QtWidgets.QLabel(VentIngresarCliente)
        self.telefonoLabel.setGeometry(QtCore.QRect(399, 321, 42, 50))
        self.telefonoLineEdit = QtWidgets.QLineEdit(VentIngresarCliente)
        self.telefonoLineEdit.setGeometry(QtCore.QRect(504, 321, 260, 50))
        self.telefonoLineEdit.setMaxLength(9)
        self.telefonoLineEdit.setValidator(QIntValidator())
        self.telefonoLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]*")))
        self.telefonoLineEdit.setPlaceholderText("Ingrese su numero de 9 digitos")
        
        # Etiqueta email y LineEdit
        self.emailLabel = QtWidgets.QLabel(VentIngresarCliente)
        self.emailLabel.setGeometry(QtCore.QRect(14, 413, 24, 50))
        self.emailLineEdit = QtWidgets.QLineEdit(VentIngresarCliente)
        self.emailLineEdit.setGeometry(QtCore.QRect(106, 413, 260, 50))
        self.emailLineEdit.setPlaceholderText("Ingrese su email")
        
        # Etiqueta domicilio y LineEdit
        self.domicilioLabel = QtWidgets.QLabel(VentIngresarCliente)
        self.domicilioLabel.setGeometry(QtCore.QRect(399, 413, 40, 50))
        self.domicilioLineEdit = QtWidgets.QLineEdit(VentIngresarCliente)
        self.domicilioLineEdit.setGeometry(QtCore.QRect(504, 413, 260, 50))
        self.domicilioLineEdit.setPlaceholderText("Ingrese domicilio")
        
        # Etiqueta imagen superior
        self.imagen_on_topLabel = QtWidgets.QLabel(VentIngresarCliente)
        self.imagen_on_topLabel.setGeometry(QtCore.QRect(0, 0, 801, 91))
        self.imagen_on_topLabel.setText("")
        self.imagen_on_topLabel.setPixmap(ImagenBanner)
        
        # Btoton ingresar y accion al pulsar
        self.btnIngresar = QtWidgets.QPushButton(VentIngresarCliente)
        self.btnIngresar.setGeometry(QtCore.QRect(14, 500, 85, 50))
        self.btnIngresar.clicked.connect(self.onActionBtnIngresar)
        
        # Boton regresar y accion al pulsar
        self.btnRegresar = QtWidgets.QPushButton(VentIngresarCliente)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.btnRegresar.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.btnRegresar.setIcon(IconoRegresar)
        self.btnRegresar.setIconSize(QtCore.QSize(60, 60))
        self.btnRegresar.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnRegresar.clicked.connect(VentIngresarCliente.close)
        
        # Definir textos
        self.retranslateUi(VentIngresarCliente)

        # Conectar todo
        QtCore.QMetaObject.connectSlotsByName(VentIngresarCliente)

    # Metodo definir textos
    def retranslateUi(self, VentIngresarCliente):
        # Definiendo textos
        _translate = QtCore.QCoreApplication.translate
        VentIngresarCliente.setWindowTitle(_translate("VentIngresarCliente", "Ingresar Cliente"))
        self.nombresLabel.setText(_translate("VentIngresarCliente", "Nombres"))
        self.apellidosLabel.setText(_translate("VentIngresarCliente", "Apellidos"))
        self.generoLabel.setText(_translate("VentIngresarCliente", "Genero"))
        self.generoComboBox.setItemText(0, _translate("VentIngresarCliente", "Masculino"))
        self.generoComboBox.setItemText(1, _translate("VentIngresarCliente", "Femenino"))
        self.generoComboBox.setPlaceholderText("Seleccione género")
        self.fecha_nacimientoLabel.setText(_translate("VentIngresarCliente", "Fecha de Nacimiento"))
        self.rutLabel.setText(_translate("VentIngresarCliente", "Rut"))
        self.digito_verificadorLabel.setText(_translate("VentIngresarCliente", "-"))
        self.telefonoLabel.setText(_translate("VentIngresarCliente", "Telefono"))
        self.emailLabel.setText(_translate("VentIngresarCliente", "Email"))
        self.domicilioLabel.setText(_translate("VentIngresarCliente", "Domicilio"))
        self.btnIngresar.setText(_translate("VentIngresarCliente", "Ingresar Cliente"))
        
    # Mensajes de alerta, Vent emergente
    def alertBox(self, Mensaje, Titulo):
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        alert = QMessageBox()
        alert.setText(Mensaje)
        alert.setWindowTitle(Titulo)
        alert.setWindowIcon(IconoTitulo)
        alert.exec_()

    # Accion al clickear boton ingresar
    def onActionBtnIngresar(self):
        nombres = self.nombresLineEdit.text()
        apellidos = self.apellidosLineEdit.text()
        genero = self.generoComboBox.currentText()
        fecha_nacimiento = self.fecha_nacimientoDateEdit.date().toString("dd/MM/yyyy")
        rut = self.rutLineEdit.text()
        digito_verificador = self.digito_verificadorLineEdit.text()
        telefono =self.telefonoLineEdit.text()
        email = self.emailLineEdit.text()
        domicilio = self.domicilioLineEdit.text()
        # Convertir la k minuscula en mayuscula
        if digito_verificador == "k":
            digito_verificador = digito_verificador.replace("k", "K")
        # Pasar el rut al formato "xx.xxx.xxx-x"
        if len(rut) > 0:
            rutFormatted = "{:,}".format(int(rut)).replace(",", ".")
            rut_con_digito_verificador = rutFormatted + "-" + digito_verificador
        else:
            rut_con_digito_verificador = ""
        if "@" not in email:
            self.alertBox("Falta ingresar el '@' en el email", "Falta un dato")
        elif "." not in email:
            self.alertBox("Falta ingresar el '.' en el email", "Falta un dato")
        # El .strip es para verificar que tenga datos
        elif nombres.strip() == "":
            self.alertBox("Falta ingresar el nombre", "Falta un dato")
        elif apellidos.strip() == "":
            self.alertBox("Falta ingresar el apellido", "Falta un dato")
        elif len(self.rutLineEdit.text()) != 8:
            self.alertBox("Faltan numeros en el rut", "Falta un dato")
        elif len(self.digito_verificadorLineEdit.text()) != 1:
            self.alertBox("Falta ingresar el digito verificador", "Falta un dato")
        elif len(self.telefonoLineEdit.text()) != 9:
            self.alertBox("Faltan numeros en el telefono", "Falta un dato")
        elif email.strip() == "":
            self.alertBox("Falta ingresar el email", "Falta un dato")
        elif domicilio.strip() == "":
            self.alertBox("Falta ingresar el domicilio", "Falta un dato")
        else:
            Cliente.agregar_cliente(nombres, apellidos, domicilio, genero, fecha_nacimiento, rut_con_digito_verificador, email, telefono)
            self.alertBox("El usuario: "+nombres+" "+apellidos+" ha sido ingresado", "Se ha ingresado el cliente")
            
            # Limpiar LineEdit
            self.nombresLineEdit.setText("")
            self.apellidosLineEdit.setText("")
            self.fecha_nacimientoDateEdit.setDate(QtCore.QDate.fromString("01/01/2000", "dd/MM/yyyy"))
            self.rutLineEdit.setText("")
            self.digito_verificadorLineEdit.setText("")
            self.emailLineEdit.setText("")
            self.telefonoLineEdit.setText("")
            self.domicilioLineEdit.setText("")