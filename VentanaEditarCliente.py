import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from PyQt5.QtGui import QIntValidator, QIcon


class VentanaEditarCliente(object):
    def setupUi(self, VentanaEditarCliente):
        ImagenBanner = QtGui.QPixmap('Imagenes/banner_cvi.png')
        IconoRegresar = QtGui.QIcon('Imagenes/boton_regresar.png')
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')

        VentanaEditarCliente.setWindowIcon(IconoTitulo)
        
        VentanaEditarCliente.resize(865, 565)
        VentanaEditarCliente.setMinimumSize(QtCore.QSize(865, 565))
        VentanaEditarCliente.setMaximumSize(QtCore.QSize(865, 565))
        
        # Etiqueta imagen superior
        self.imagen_on_topLabel = QtWidgets.QLabel(VentanaEditarCliente)
        self.imagen_on_topLabel.setGeometry(QtCore.QRect(0, 0, 865, 96))
        self.imagen_on_topLabel.setText("")
        self.imagen_on_topLabel.setPixmap(ImagenBanner.scaled(865, 96))

        # Boton regresar y accion al pulsar
        self.btnRegresar = QtWidgets.QPushButton(VentanaEditarCliente)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.btnRegresar.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.btnRegresar.setIcon(IconoRegresar)
        self.btnRegresar.setIconSize(QtCore.QSize(60, 60))
        self.btnRegresar.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnRegresar.clicked.connect(VentanaEditarCliente.close)
        
        # Tabla con columnas y filas y que sean 9 columnas [ID, Nombres, Apellidos, Genero, Fecha_Nacimiento, Rut, Telefono, Email, Domicilio]
        self.tableWidget = QtWidgets.QTableWidget(VentanaEditarCliente)
        self.tableWidget.setGeometry(QtCore.QRect(10, 140, 845, 342))
        self.tableWidget.setColumnCount(9) 
        
        # Posicionar Encabezados
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        
        # Para que no se puedan editar a no ser que se de click en el boton editar
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Boton editar y accion al pulsar
        self.btnEditar = QtWidgets.QPushButton(VentanaEditarCliente)
        self.btnEditar.setGeometry(QtCore.QRect(20, 500, 121, 50))
        self.btnEditar.clicked.connect(self.onActionBtnEditar)
        
        # Boton eliminar y accion al pulsar
        self.btnEliminar = QtWidgets.QPushButton(VentanaEditarCliente)
        self.btnEliminar.setGeometry(QtCore.QRect(160, 500, 121, 50))
        self.btnEliminar.clicked.connect(self.onActionBtnEliminar)
        
        # Boton guardar y accion al pulsar
        self.btnGuardar = QtWidgets.QPushButton(VentanaEditarCliente)
        self.btnGuardar.setGeometry(QtCore.QRect(725, 500, 121, 50))
        self.btnGuardar.clicked.connect(self.onActionBtnGuardar)
        
        # Etiqueta de instruccion para editar clientes
        self.mensajeEditarLabel = QtWidgets.QLabel(VentanaEditarCliente)
        self.mensajeEditarLabel.setGeometry(QtCore.QRect(14, 94, 865, 50))
        
        # Etiqueta de instruccion para eliminar clientes
        self.mensajeEliminarLabel = QtWidgets.QLabel(VentanaEditarCliente)
        self.mensajeEliminarLabel.setGeometry(QtCore.QRect(460, 94, 865, 50))
        
        self.retranslateUi(VentanaEditarCliente)
        QtCore.QMetaObject.connectSlotsByName(VentanaEditarCliente)
        
        # Cargar Clientes del CSV
        self.cargarClienteCSV()
        
    # Metodo definir textos
    def retranslateUi(self, VentanaEditarCliente):
        # Fuente de texto
        fuenteEstado = QtGui.QFont()
        fuenteEstado.setPointSize(9)
        fuenteEstado.setBold(True)
        self.mensajeEditarLabel.setFont(fuenteEstado)
        
        # Definiendo textos
        _translate = QtCore.QCoreApplication.translate
        VentanaEditarCliente.setWindowTitle(_translate("VentanaEditarCliente", "Ventana - Editar Cliente"))
        self.btnEditar.setText(_translate("VentanaEditarCliente", "Editar"))
        self.btnEliminar.setText(_translate("VentanaEditarCliente", "Eliminar"))
        self.btnGuardar.setText(_translate("VentanaEditarCliente", "Guardar Cambios"))
        self.mensajeEditarLabel.setText(_translate("VentanaEditarCliente", "Para editar el cliente seleccione una celda y haga click en Editar"))
        self.mensajeEditarLabel.setFont(fuenteEstado)
        self.mensajeEliminarLabel.setText(_translate("VentanaEditarCliente", "Para eliminar el cliente seleccione una ID y haga click en Eliminar"))
        self.mensajeEliminarLabel.setFont(fuenteEstado)
        
        
    # Accion al clickear boton eliminar
    def onActionBtnEliminar(self):
    # Obtiene la fila y columna seleccionadas
        fila = self.tableWidget.currentRow()
        columna = self.tableWidget.currentColumn()
        if columna == 0:  # Verifica si la columna es la del ID
            if fila != -1:
                # Elimina la fila seleccionada
                self.tableWidget.removeRow(fila)
        else:
            self.alertBox("Debe seleccionar una 'ID' para borrar el cliente", "Instrucciones para borrar")
    
    # Accion al clickear boton editar
    def onActionBtnEditar(self):
        # Obtiene la celda seleccionada
        celda = self.tableWidget.currentItem() 
        if celda is None:
            # Si no hay una celda seleccionada, imprime el siguiente mensaje
            self.alertBox("Debe seleccionar una celda", "Intrucciones para editar")
        else:
            # Comprueba que la celda no sea nula
            columna = self.tableWidget.currentColumn()
            fila = self.tableWidget.currentRow()
            # Permite editar la celda seleccionada
            self.tableWidget.editItem(celda) 
            
    # Accion al clickear boton guardar
    def onActionBtnGuardar(self):
        # Abre el archivo CSV
        with open('ArchivosCSV/Cliente.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            # Escribe los encabezados de las columnas
            encabezados = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(self.tableWidget.columnCount())]
            writer.writerow(encabezados)
            # Sobreescribe los datos de los clientes con los nuevos valores (Cliente editado o eliminado)
            for fila in range(self.tableWidget.rowCount()):
                datos_de_la_fila = []
                for columna in range(self.tableWidget.columnCount()):
                    celda = self.tableWidget.item(fila, columna)
                    if celda is not None:
                        datos_de_la_fila.append(celda.text())
                    else:
                        datos_de_la_fila.append('')
                writer.writerow(datos_de_la_fila)
        # Mensaje de que los cambios se guardaron correctamente
        self.alertBox("Se han guardado los cambios exitosamente!", "Se han completado los cambios")

    # Metodo para que cargue los clientes desde el archivo CSV
    def cargarClienteCSV(self):
        # Abre el archivo CSV
        with open('ArchivosCSV/Cliente.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            #  Lee la primera fila como los encabezados de las columnas y los posiciona en el tableWidget
            encabezados = next(reader)
            self.tableWidget.setHorizontalHeaderLabels(encabezados)
            # Recorre las filas para obtener los datos que se muestran en el tableWidget
            for fila in reader:
                posicionFila = self.tableWidget.rowCount()
                self.tableWidget.insertRow(posicionFila)
                for columna, value in enumerate(fila):
                    item = QtWidgets.QTableWidgetItem(value)
                    self.tableWidget.setItem(posicionFila, columna, item)
                    
        # Ajusta el tamaño de las celdas automaticamente
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        
    # Mensajes de alerta, ventana emergente
    def alertBox(self, Mensaje, Titulo):
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        alert = QMessageBox()
        alert.setText(Mensaje)
        alert.setWindowTitle(Titulo)
        alert.setWindowIcon(IconoTitulo)
        alert.exec_()