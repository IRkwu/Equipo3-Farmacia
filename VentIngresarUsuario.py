from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator, QFont, QIcon
from PyQt5.QtWidgets import QMessageBox
from Clases.Usuario import Usuario

class VentIngresarUsuario(object):
    def setupUi(self, VentIngresarUsuario):
        ImagenBanner = QtGui.QPixmap('Imagenes/banner_cvi.png')
        IconoRegresar = QtGui.QIcon('Imagenes/boton_regresar.png')
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        
        VentIngresarUsuario.setWindowIcon(IconoTitulo)
        
        VentIngresarUsuario.resize(800, 657)
        VentIngresarUsuario.setMinimumSize(QtCore.QSize(800, 657))
        VentIngresarUsuario.setMaximumSize(QtCore.QSize(800, 657))
        
        # Etiqueta nombres y LineEdit
        self.nombresLabel = QtWidgets.QLabel(VentIngresarUsuario)
        self.nombresLabel.setGeometry(QtCore.QRect(14, 137, 42, 50))
        self.nombresLineEdit = QtWidgets.QLineEdit(VentIngresarUsuario)
        self.nombresLineEdit.setGeometry(QtCore.QRect(106, 137, 260, 50))
        self.nombresLineEdit.setPlaceholderText("Ingrese Primer y segundo nombre")
        
        # Etiqueta apellidos y LineEdit
        self.apellidosLabel = QtWidgets.QLabel(VentIngresarUsuario)
        self.apellidosLabel.setGeometry(QtCore.QRect(399, 137, 42, 50))
        self.apellidosLineEdit = QtWidgets.QLineEdit(VentIngresarUsuario)
        self.apellidosLineEdit.setGeometry(QtCore.QRect(504, 137, 260, 50))
        self.apellidosLineEdit.setPlaceholderText("Ingrese apellido paterno y materno")

        
        # Etiqueta genero y ComboBox
        self.generoLabel = QtWidgets.QLabel(VentIngresarUsuario)
        self.generoLabel.setGeometry(QtCore.QRect(14, 229, 35, 50))
        self.generoComboBox = QtWidgets.QComboBox(VentIngresarUsuario)
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
        self.fecha_nacimientoLabel = QtWidgets.QLabel(VentIngresarUsuario)
        self.fecha_nacimientoLabel.setGeometry(QtCore.QRect(399, 229, 99, 50))
        self.fecha_nacimientoDateEdit = QtWidgets.QDateEdit(VentIngresarUsuario)
        self.fecha_nacimientoDateEdit.setGeometry(QtCore.QRect(504, 229, 260, 50))
        
        # Etiqueta rut y LineEdit
        self.rutLabel = QtWidgets.QLabel(VentIngresarUsuario)
        self.rutLabel.setGeometry(QtCore.QRect(14, 321, 17, 50))
        self.rutLineEdit = QtWidgets.QLineEdit(VentIngresarUsuario)
        self.rutLineEdit.setGeometry(QtCore.QRect(106, 321, 200, 50))
        self.rutLineEdit.setMaxLength(8)
        self.rutLineEdit.setValidator(QIntValidator())
        self.rutLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]*")))
        self.rutLineEdit.setPlaceholderText("Ingrese rut sin puntos")
        
        # Etiqueta digito_verificador y LineEdit
        self.digito_verificadorLabel = QtWidgets.QLabel(VentIngresarUsuario)
        self.digito_verificadorLabel.setGeometry(QtCore.QRect(312, 321, 17, 50))
        self.digito_verificadorLineEdit = QtWidgets.QLineEdit(VentIngresarUsuario)
        self.digito_verificadorLineEdit.setGeometry(QtCore.QRect(326, 321, 40, 50))
        self.digito_verificadorLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9Kk]")))
        self.digito_verificadorLineEdit.setMaxLength(1)
        self.digito_verificadorLineEdit.setPlaceholderText("0-9 | K")
        
        # Etiqueta telefono y LineEdit
        self.telefonoLabel = QtWidgets.QLabel(VentIngresarUsuario)
        self.telefonoLabel.setGeometry(QtCore.QRect(399, 321, 42, 50))
        self.telefonoLineEdit = QtWidgets.QLineEdit(VentIngresarUsuario)
        self.telefonoLineEdit.setGeometry(QtCore.QRect(504, 321, 260, 50))
        self.telefonoLineEdit.setMaxLength(9)
        self.telefonoLineEdit.setValidator(QIntValidator())
        self.telefonoLineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]*")))
        self.telefonoLineEdit.setPlaceholderText("Ingrese su numero de 9 digitos")
        
        # Etiqueta email y LineEdit
        self.emailLabel = QtWidgets.QLabel(VentIngresarUsuario)
        self.emailLabel.setGeometry(QtCore.QRect(14, 413, 24, 50))
        self.emailLineEdit = QtWidgets.QLineEdit(VentIngresarUsuario)
        self.emailLineEdit.setGeometry(QtCore.QRect(106, 413, 260, 50))
        self.emailLineEdit.setPlaceholderText("Ingrese su email")
        
        # Etiqueta domicilio y LineEdit
        self.domicilioLabel = QtWidgets.QLabel(VentIngresarUsuario)
        self.domicilioLabel.setGeometry(QtCore.QRect(399, 413, 40, 50))
        self.domicilioLineEdit = QtWidgets.QLineEdit(VentIngresarUsuario)
        self.domicilioLineEdit.setGeometry(QtCore.QRect(504, 413, 260, 50))
        self.domicilioLineEdit.setPlaceholderText("Ingrese domicilio")
        
        # Etiqueta email y LineEdit
        self.passwordLabel = QtWidgets.QLabel(VentIngresarUsuario)
        self.passwordLabel.setGeometry(QtCore.QRect(14, 505, 80, 50))
        self.passwordLineEdit = QtWidgets.QLineEdit(VentIngresarUsuario)
        self.passwordLineEdit.setGeometry(QtCore.QRect(106, 505, 260, 50))
        self.passwordLineEdit.setPlaceholderText("Ingrese su contraseña")
        
        # Etiqueta genero y ComboBox
        self.cargoLabel = QtWidgets.QLabel(VentIngresarUsuario)
        self.cargoLabel.setGeometry(QtCore.QRect(399, 505, 35, 50))
        self.cargoComboBox = QtWidgets.QComboBox(VentIngresarUsuario)
        self.cargoComboBox.setGeometry(QtCore.QRect(504, 505, 260, 50))
        self.cargoComboBox.setMinimumSize(QtCore.QSize(260, 50))
        self.cargoComboBox.setEditable(False)
        self.cargoComboBox.addItem("")
        self.cargoComboBox.addItem("")
        
        # Etiqueta imagen superior
        self.imagen_on_topLabel = QtWidgets.QLabel(VentIngresarUsuario)
        self.imagen_on_topLabel.setGeometry(QtCore.QRect(0, 0, 801, 91))
        self.imagen_on_topLabel.setText("")
        self.imagen_on_topLabel.setPixmap(ImagenBanner)
        
        # Btoton ingresar y accion al pulsar
        self.btnIngresar = QtWidgets.QPushButton(VentIngresarUsuario)
        self.btnIngresar.setGeometry(QtCore.QRect(14, 592, 85, 50))
        self.btnIngresar.clicked.connect(self.onActionBtnIngresar)
        
        # Boton regresar y accion al pulsar
        self.btnRegresar = QtWidgets.QPushButton(VentIngresarUsuario)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.btnRegresar.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.btnRegresar.setIcon(IconoRegresar)
        self.btnRegresar.setIconSize(QtCore.QSize(60, 60))
        self.btnRegresar.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnRegresar.clicked.connect(VentIngresarUsuario.close)
        
        # Definir textos
        self.retranslateUi(VentIngresarUsuario)

        # Conectar todo
        QtCore.QMetaObject.connectSlotsByName(VentIngresarUsuario)

    # Metodo definir textos
    def retranslateUi(self, VentIngresarUsuario):
        # Definiendo textos
        _translate = QtCore.QCoreApplication.translate
        VentIngresarUsuario.setWindowTitle(_translate("VentIngresarUsuario", "Ingresar Usuario"))
        self.nombresLabel.setText(_translate("VentIngresarUsuario", "Nombres"))
        self.apellidosLabel.setText(_translate("VentIngresarUsuario", "Apellidos"))
        self.generoLabel.setText(_translate("VentIngresarUsuario", "Genero"))
        self.generoComboBox.setItemText(0, _translate("VentIngresarUsuario", "Masculino"))
        self.generoComboBox.setItemText(1, _translate("VentIngresarUsuario", "Femenino"))
        self.generoComboBox.setPlaceholderText("Seleccione género")
        self.fecha_nacimientoLabel.setText(_translate("VentIngresarUsuario", "Fecha de Nacimiento"))
        self.rutLabel.setText(_translate("VentIngresarUsuario", "Rut"))
        self.digito_verificadorLabel.setText(_translate("VentIngresarUsuario", "-"))
        self.telefonoLabel.setText(_translate("VentIngresarUsuario", "Telefono"))
        self.emailLabel.setText(_translate("VentIngresarUsuario", "Email"))
        self.domicilioLabel.setText(_translate("VentIngresarUsuario", "Domicilio"))
        self.passwordLabel.setText(_translate("VentIngresarUsuario", "Contraseña"))
        self.cargoLabel.setText(_translate("VentIngresarUsuario", "Cargo"))
        self.cargoComboBox.setItemText(0, _translate("VentIngresarUsuario", "Gerente"))
        self.cargoComboBox.setItemText(1, _translate("VentIngresarUsuario", "Vendedor"))
        self.cargoComboBox.setPlaceholderText("Seleccione género")
        self.btnIngresar.setText(_translate("VentIngresarUsuario", "Ingresar \nUsuario"))
        
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
        password = self.passwordLineEdit.text()
        cargo = self.cargoComboBox.currentText()
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
        elif password.strip() == "":
            self.alertBox("Falta ingresar la contraseña", "Falta un dato")
        else:
            Usuario.agregar_usuario(nombres, apellidos, domicilio, genero, fecha_nacimiento, rut_con_digito_verificador, email, password, telefono, cargo, )
            self.alertBox("El usuario: "+nombres+" "+apellidos+" ha sido ingresado", "Se ha ingresado el Usuario")
            
            # Limpiar LineEdit
            self.nombresLineEdit.setText("")
            self.apellidosLineEdit.setText("")
            self.fecha_nacimientoDateEdit.setDate(QtCore.QDate.fromString("01/01/2000", "dd/MM/yyyy"))
            self.rutLineEdit.setText("")
            self.digito_verificadorLineEdit.setText("")
            self.emailLineEdit.setText("")
            self.telefonoLineEdit.setText("")
            self.domicilioLineEdit.setText("")
            self.passwordLineEdit.setText("")