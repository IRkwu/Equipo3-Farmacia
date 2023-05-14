from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
import csv

class VentComprarMedicamentos(object):
    def __init__(self):
        self.carrito = []  # Lista para almacenar los medicamentos del carrito
    
    def setupUi(self, VentComprarMedicamentos):
        ImagenBanner = QtGui.QPixmap('Imagenes/banner_carrito.png')
        IconoRegresar = QtGui.QIcon('Imagenes/boton_regresar.png')
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        
        VentComprarMedicamentos.setWindowIcon(IconoTitulo)
        
        VentComprarMedicamentos.resize(930, 770)
        VentComprarMedicamentos.setMinimumSize(QtCore.QSize(930, 770))
        VentComprarMedicamentos.setMaximumSize(QtCore.QSize(930, 770))
        
        # Etiqueta imagen superior
        self.imagen_on_topLabel = QtWidgets.QLabel(VentComprarMedicamentos)
        self.imagen_on_topLabel.setGeometry(QtCore.QRect(0, 0, 930, 144))
        self.imagen_on_topLabel.setText("")
        self.imagen_on_topLabel.setPixmap(ImagenBanner.scaled(930, 144))
        
        # Boton regresar y accion al pulsar
        self.btnRegresar = QtWidgets.QPushButton(VentComprarMedicamentos)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.btnRegresar.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.btnRegresar.setIcon(IconoRegresar)
        self.btnRegresar.setIconSize(QtCore.QSize(60, 60))
        self.btnRegresar.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnRegresar.clicked.connect(VentComprarMedicamentos.close)
        
        # Tabla con columnas y filas para el carrito
        self.tableWidgetCarrito = QtWidgets.QTableWidget(VentComprarMedicamentos)
        self.tableWidgetCarrito.setGeometry(QtCore.QRect(620, 210, 300, 180))
        self.tableWidgetCarrito.setColumnCount(4)
        self.tableWidgetCarrito.setHorizontalHeaderLabels(["ID", "Nombre", "Precio", "Lote"])
        
        # Para que no se puedan editar los elementos del carrito
        self.tableWidgetCarrito.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        # Ajusta el tamaño de las celdas a un tamaño predefini en el carrito
        self.tableWidgetCarrito.setColumnWidth(0, 20)
        self.tableWidgetCarrito.setColumnWidth(1, 144)
        self.tableWidgetCarrito.setColumnWidth(2, 100)
        # Para ocultar el lote del producto que fue agregado al carrito
        self.tableWidgetCarrito.setColumnHidden(3, True) 
        
        # Tabla con columnas y filas y que sean 9 columnas [ID, Nombre, Precio, Stock, Descripcion], carga las demás columnas, las de vencimiento y lote pero no las muestra, es para que al guardar no se vacien
        self.tableWidget = QtWidgets.QTableWidget(VentComprarMedicamentos)
        self.tableWidget.setGeometry(QtCore.QRect(10, 210, 600, 545))
        self.tableWidget.setColumnCount(9)
        
        # Columnas a ocultar
        columnas_ocultar = [5, 6, 7, 8]
        for columna in columnas_ocultar:
            self.tableWidget.setColumnHidden(columna, True)

        # Para que no se puedan editar los medicamentos de la lista de medicamentos
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        # CheckBox de necesita_envio y acción al cambiar su estado
        self.necesita_envioCheckBox = QtWidgets.QCheckBox(VentComprarMedicamentos)
        self.necesita_envioCheckBox.setGeometry(QtCore.QRect(665, 648, 250, 30))
        self.necesita_envioCheckBox.stateChanged.connect(self.actualizarDatos)
        
        # CheckBox de tiene_receta y acción al cambiar su estado
        self.tiene_recetaCheckbox = QtWidgets.QCheckBox(VentComprarMedicamentos)
        self.tiene_recetaCheckbox.setGeometry(QtCore.QRect(665, 678, 250, 30))
        self.tiene_recetaCheckbox.stateChanged.connect(self.actualizarDatos)
        
        # Etiqueta cantidad_medicamentos y LineEdit
        self.cantidad_medicamentosLabel = QtWidgets.QLabel(VentComprarMedicamentos)
        self.cantidad_medicamentosLabel.setGeometry(QtCore.QRect(670, 410, 101, 31))
        self.cantidad_medicamentosLineEdit = QtWidgets.QLineEdit(VentComprarMedicamentos)
        self.cantidad_medicamentosLineEdit.setGeometry(QtCore.QRect(770, 410, 113, 31))
        self.cantidad_medicamentosLineEdit.setReadOnly(True)
        
        # Etiqueta subtotal y LineEdit
        self.subtotalLabel = QtWidgets.QLabel(VentComprarMedicamentos)
        self.subtotalLabel.setGeometry(QtCore.QRect(670, 460, 101, 31))
        self.subtotalLineEdit = QtWidgets.QLineEdit(VentComprarMedicamentos)
        self.subtotalLineEdit.setGeometry(QtCore.QRect(770, 460, 113, 31))
        self.subtotalLineEdit.setReadOnly(True)
        
        # Etiqueta descuento y LineEdit
        self.descuentoLabel = QtWidgets.QLabel(VentComprarMedicamentos)
        self.descuentoLabel.setGeometry(QtCore.QRect(670, 510, 101, 31))
        self.descuentoLineEdit = QtWidgets.QLineEdit(VentComprarMedicamentos)
        self.descuentoLineEdit.setGeometry(QtCore.QRect(770, 510, 113, 31))
        self.descuentoLineEdit.setReadOnly(True)
        
        # Etiqueta costo_envio y LineEdit
        self.costo_envioLabel = QtWidgets.QLabel(VentComprarMedicamentos)
        self.costo_envioLabel.setGeometry(QtCore.QRect(670, 560, 101, 31))
        self.costo_envioLineEdit = QtWidgets.QLineEdit(VentComprarMedicamentos)
        self.costo_envioLineEdit.setGeometry(QtCore.QRect(770, 560, 113, 31))
        self.costo_envioLineEdit.setReadOnly(True)
        
        # Etiqueta total y LineEdit
        self.totalLabel = QtWidgets.QLabel(VentComprarMedicamentos)
        self.totalLabel.setGeometry(QtCore.QRect(670, 610, 101, 31))
        self.totalLineEdit = QtWidgets.QLineEdit(VentComprarMedicamentos)
        self.totalLineEdit.setGeometry(QtCore.QRect(770, 610, 113, 31))
        self.totalLineEdit.setReadOnly(True)
        
        # Boton mas y accion al pulsar
        self.btnMas = QtWidgets.QPushButton(VentComprarMedicamentos)
        self.btnMas.setGeometry(QtCore.QRect(722, 150, 96, 50))
        self.btnMas.clicked.connect(self.onActionBtnMas)
        
        # Boton menos y accion al pulsar
        self.btnMenos = QtWidgets.QPushButton(VentComprarMedicamentos)
        self.btnMenos.setGeometry(QtCore.QRect(620, 150, 90, 50))
        self.btnMenos.clicked.connect(self.onActionBtnMenos)
        
        # Boton informacion y accion al pulsar
        self.btnInfo = QtWidgets.QPushButton(VentComprarMedicamentos)
        self.btnInfo.setGeometry(QtCore.QRect(830, 150, 90, 50))
        self.btnInfo.clicked.connect(self.onActionBtnInfo)
        
        # Boton comprar y accion al pulsar
        self.btnComprar = QtWidgets.QPushButton(VentComprarMedicamentos)
        self.btnComprar.setGeometry(QtCore.QRect(660, 713, 231, 45))
        self.btnComprar.clicked.connect(self.onActionBtnComprar)

        # Barra de busqueda y accion al actualizar el texto
        self.buscarLineEdit = QtWidgets.QLineEdit(VentComprarMedicamentos)
        self.buscarLineEdit.setGeometry(QtCore.QRect(10, 150, 600, 50))
        self.buscarLineEdit.setPlaceholderText("Ingrese el nombre o ID del medicamento")
        self.buscarLineEdit.setStyleSheet("font-size: 16px;")
        self.buscarLineEdit.textChanged.connect(self.buscarMedicamentos)

        self.retranslateUi(VentComprarMedicamentos)
        QtCore.QMetaObject.connectSlotsByName(VentComprarMedicamentos)
        
        # Cargar lista de medicamentos del CSV y actualiar datos (subtotal, total, entre otros)
        self.cargarMedicamentosCSV()
        self.actualizarDatos()
        
    # Metodo definir textos
    def retranslateUi(self, VentComprarMedicamentos):
        _translate = QtCore.QCoreApplication.translate
        VentComprarMedicamentos.setWindowTitle(_translate("VentComprarMedicamentos", "Vent - Agregar medicamentos al carrito"))
        self.cantidad_medicamentosLabel.setText(_translate("VentComprarMedicamentos", "Cantidad de\nMedicamentos:"))
        self.subtotalLabel.setText(_translate("VentComprarMedicamentos", "Subtotal:"))
        self.descuentoLabel.setText(_translate("VentComprarMedicamentos", "Descuento:"))
        self.costo_envioLabel.setText(_translate("VentComprarMedicamentos", "Costo Envio:"))
        self.totalLabel.setText(_translate("VentComprarMedicamentos", "Total:"))
        self.necesita_envioCheckBox.setText(_translate("VentComprarMedicamentos", "Seleccione si necesita envio. Precio: $2000\nEl envío es gratis si el subtotal es > $30000"))
        self.tiene_recetaCheckbox.setText(_translate("VentComprarMedicamentos", "Seleccione si tiene receta, en caso de\ntener receta, se aplica 10% de descuento"))
        self.btnComprar.setText(_translate("VentComprarMedicamentos", "Confirmar Compra"))
        self.btnMas.setText(_translate("VentComprarMedicamentos", "Agregar \nMedicamento\n(+)"))
        self.btnMenos.setText(_translate("VentComprarMedicamentos", "Quitar \nMedicamento\n(-)"))
        self.btnInfo.setText(_translate("VentComprarMedicamentos", "Instrucciones\n(!)"))
        
    # Accion al clickear boton comprar
    def onActionBtnComprar(self):
        if self.tableWidgetCarrito.rowCount() == 0:
            self.alertBox("No se han agregado medicamentos al carrito\npor lo que no se ha comprado nada", "Falta ingresar medicamentos")
        else:
            for fila in range(self.tableWidget.rowCount()):
                if self.tableWidget.item(fila, 5).text() == '0':
                    self.actualizarLotes(fila)
            # Abre el archivo CSV para guardar los datos
            with open('ArchivosCSV/Medicamentos.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                # Escribe los encabezados de las columnas
                encabezados = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(self.tableWidget.columnCount())]
                writer.writerow(encabezados)
                # Sobreescribe los datos de los medicamentos con los nuevos valores (El nuevo stock despues de comprar medicamentos)
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
            self.alertBox("Se han comprado los medicamentos.\nLa lista de medicamentos se ha actualizado", "Compra exitosa")
            self.tableWidgetCarrito.setRowCount(0)
            # Aqui se borra, pero en verdad se tendría que guardar para la boleta, pero no es tarea nuestra wuejeje
            self.carrito = []
            self.actualizarDatos()
            
    def actualizarLotes(self, fila):
        # Si el stock del lote 1 es igual a 0 copia el stock y vencimiento del lote 2 al lote 1, dejando el lote 2 libre para agregar un nuevo lote de medicamentos
        if self.tableWidget.item(fila, 7) is not None:
            stock_lote_2 = self.tableWidget.item(fila, 7).text()
            self.tableWidget.setItem(fila, 5, QTableWidgetItem(stock_lote_2))
            self.tableWidget.setItem(fila, 7, QTableWidgetItem("0"))
            
            vencimiento_lote_2 = self.tableWidget.item(fila, 8).text()
            self.tableWidget.setItem(fila, 6, QTableWidgetItem(vencimiento_lote_2))
            self.tableWidget.setItem(fila, 8, QTableWidgetItem(""))
            if (self.tableWidget.item(fila, 5).text() == "0"):
                self.tableWidget.setItem(fila, 6, QTableWidgetItem(""))
            
        
    def onActionBtnInfo(self):
        self.alertBox("- Para comprar un medicamento debe seleccionarlo desde la lista de\nmedicamentos y hacer click en Agregar Medicamento\n"
                      "\n- Para quitar un medicamento del carrito, debe seleccionarlo y dar click\nen Quitar Medicamento\n"
                      "\n- Para comprar los medicamentos debe haber agregado al menos un\nmedicamento al carrito, de lo contrario la compra no se va efectuar\n"
                      "\n- Si necesita envio, debe marcar la opción: [Seleccione si necesita envío]\nEl costo del envío son $2000 pero si el total supera los $30000 el envío es gratis\n"
                      "\n- Si usted tiene una receta, debe marcar la opción: [Seleccione si tiene receta]\nSi el cliente tiene receta se aplica un 10% de descuento, este es aplicado\nen el subtotal por lo que no afecta el costro de envío", "Lista de Instrucciones")

    # Metodo para que cargue los clientes desde el archivo CSV
    def cargarMedicamentosCSV(self):
        # Abre el archivo CSV
        with open('ArchivosCSV/Medicamentos.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            #  Lee la primera fila como los encabezados de las columnas y los posiciona en el tableWidget
            encabezados = next(reader)
            self.tableWidget.setHorizontalHeaderLabels(encabezados)
            # Recorre las filas para obtener los datos que se muestran en el tableWidget
            for fila in reader:
                posicionFila = self.tableWidget.rowCount()
                self.tableWidget.insertRow(posicionFila)
                # Recorre las columnas para obtener los datos que se muestran en el tableWidget
                for columna, value in enumerate(fila):
                    item = QtWidgets.QTableWidgetItem(value)
                    self.tableWidget.setItem(posicionFila, columna, item)
                    
        # Ajusta el tamaño de las celdas automaticamente
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
    
    # Mensajes de alerta, Vent emergente
    def alertBox(self, Mensaje, Titulo):
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        alert = QMessageBox()
        alert.setText(Mensaje)
        alert.setWindowTitle(Titulo)
        alert.setWindowIcon(IconoTitulo)
        alert.exec_()

    # Metodo para la barra de busqueda
    def buscarMedicamentos(self):
        # Busca los medicamentos que coinciden con la búsqueda y los muestra en la tabla
        texto = self.buscarLineEdit.text().strip().lower()
        if texto:
            for i in range(self.tableWidget.rowCount()):
                found = False
                id_medicamento = self.tableWidget.item(i, 0)
                nombre_medicamento = self.tableWidget.item(i, 1)
                # Si la id del medicamento existe la muestra
                if id_medicamento and texto in id_medicamento.text().lower():
                    found = True
                # Si el nombre del medicamento existe la muestra
                elif nombre_medicamento and texto in nombre_medicamento.text().lower():
                    found = True
                # Oculta los elementos que no tengan texto o numeros similares a los ingresados
                self.tableWidget.setRowHidden(i, not found)
        else:
            # Muestra todas las filas si no se ha ingresado ningún texto
            for i in range(self.tableWidget.rowCount()):
                self.tableWidget.setRowHidden(i, False)
                
    # Accion al pulsar boton mas, agrega medicamentos de la tableWidget de medicamentos a la tableWidgetCarrito (La del carrilo lol) y resta el stock
    def onActionBtnMas(self):
        fila_seleccionada = self.tableWidget.currentRow()
        
        if fila_seleccionada == -1:
            self.alertBox("Debe seleccionar un medicamento para agregarlo al Carrito", "Agregar Medicamentos")
        
        # Si se ha seleccionado un medicamento
        if fila_seleccionada != -1:  
            # Obtiene los datos del medicamento seleccionado
            id_medicamento = int(self.tableWidget.item(fila_seleccionada, 0).text())
            nombre_medicamento = self.tableWidget.item(fila_seleccionada, 1).text()
            precio_medicamento = int(self.tableWidget.item(fila_seleccionada, 2).text())
            stock_medicamento = int(self.tableWidget.item(fila_seleccionada, 3).text())
            
            # Si el stock es igual a 0 muestra un mensaje de alerta
            if stock_medicamento == 0:
                self.alertBox("El medicamento seleccionado no tiene stock disponible, lamentamos las molestias", "No hay stock Disponible")
            else:
                
                # Resta 1 al stock del medicamento agregado
                stock_lote_1 = int(self.tableWidget.item(fila_seleccionada, 5).text())
                stock_lote_2 = int(self.tableWidget.item(fila_seleccionada, 7).text())
                if (stock_lote_1>0):
                    # Retira 1 al stock del medicamento seleccionado en el Lote 1 y actualiza Stock
                    stock_lote_1 -= 1
                    self.tableWidget.setItem(fila_seleccionada, 5, QTableWidgetItem(str(stock_lote_1)))
                    self.tableWidget.setItem(fila_seleccionada, 3, QTableWidgetItem(str(stock_lote_1+stock_lote_2)))
                    lote = 1
                elif (stock_lote_2>0):
                    # Retira 1 al stock del medicamento seleccionado en el Lote 2 y actualiza Stock
                    stock_lote_2 -= 1
                    self.tableWidget.setItem(fila_seleccionada, 7, QTableWidgetItem(str(stock_lote_2)))
                    self.tableWidget.setItem(fila_seleccionada, 3, QTableWidgetItem(str(stock_lote_1+stock_lote_2)))
                    lote = 2
                else:
                    self.alertBox("No se puede retirar más stock", "Alerta Stock")
                
                # Agrega el medicamento al carrito
                self.carrito.append((id_medicamento, nombre_medicamento, precio_medicamento, lote))

                # Actualiza la tabla de carrito
                self.actualizarTablaCarrito()

                # Calcula los valores de la boleta, cantidad medicamentos, subtotal, descuento y precio
                self.actualizarDatos()                

    # Accion al pulsar boton menos, elimina medicamentos de la tableWidgetCarrito y agrega el stock devuelta en el tableWidget de medicamentos
    def onActionBtnMenos(self):
        # Obtiene la fila seleccionada en el widgetTableCarrito
        fila_seleccionada = self.tableWidgetCarrito.currentRow()

        # Verificar que se haya seleccionado una fila
        if fila_seleccionada == -1:
            self.alertBox("Debe seleccionar un medicamento del carrito para\ndevolverlo a la lista de medicamentos", "Seleccione un medicamento del carrito")
        else:
            # Obtiene los datos del medicamento seleccionado en el carrito
            id_medicamento = int(self.tableWidgetCarrito.item(fila_seleccionada, 0).text())

            # Recorre las filas del tableWidget de medicamentos y obtiene la ID
            for fila in range(self.tableWidget.rowCount()):
                if int(self.tableWidget.item(fila, 0).text()) == id_medicamento:
                    break
            else:
                fila = self.tableWidget.rowCount()
                self.tableWidget.setRowCount(fila + 1)
                self.tableWidget.setItem(fila, 0, QTableWidgetItem(str(id_medicamento)))

            # Obtiene el stock del lote 1 y 2
            stock_lote_1 = int(self.tableWidget.item(fila, 5).text())
            stock_lote_2 = int(self.tableWidget.item(fila, 7).text())
            lote = int(self.tableWidgetCarrito.item(fila_seleccionada, 3).text())
            # Si el medicamento provenia del lote 2, lo devuelve al propio lote 2
            if lote == 2:
                stock_lote_2 += 1
                self.tableWidget.setItem(fila, 7, QTableWidgetItem(str(stock_lote_2)))
                self.tableWidget.setItem(fila, 3, QTableWidgetItem(str(stock_lote_1+stock_lote_2)))
            else:
            # Sino lo devuelve al lote 1
                stock_lote_1 += 1
                self.tableWidget.setItem(fila, 5, QTableWidgetItem(str(stock_lote_1)))
                self.tableWidget.setItem(fila, 3, QTableWidgetItem(str(stock_lote_1+stock_lote_2)))
            
            # Elimina el medicamento del carrito
            self.carrito.pop(fila_seleccionada)

            # Actualiza la tabla de carrito con el medicamento eliminado
            self.actualizarTablaCarrito()

            # Calcula los valores de la boleta, cantidad medicamentos, subtotal, descuento y precio
            self.actualizarDatos()
        
    def actualizarTablaCarrito(self):
        cantidad_de_filas = len(self.carrito)
        self.tableWidgetCarrito.setRowCount(cantidad_de_filas)
        for i, (id_medicamento, nombre_medicamento, precio_medicamento, lote) in enumerate(self.carrito):
            self.tableWidgetCarrito.setItem(i, 0, QTableWidgetItem(str(id_medicamento)))
            self.tableWidgetCarrito.setItem(i, 1, QTableWidgetItem(nombre_medicamento))
            self.tableWidgetCarrito.setItem(i, 2, QTableWidgetItem(str(precio_medicamento)))
            self.tableWidgetCarrito.setItem(i, 3, QTableWidgetItem(str(lote)))
        
    def actualizarDatos(self):
        cantidad_medicamentos = len(self.carrito)
        subtotal = 0
        costo_envio = 0
        for medicamento in self.carrito:
            subtotal = subtotal + medicamento[2]
        self.cantidad_medicamentosLineEdit.setText(str(cantidad_medicamentos))
        self.subtotalLineEdit.setText("$"+str(subtotal))
        if self.tiene_recetaCheckbox.isChecked():
            descuento = int(subtotal * 0.1)
        else:
            descuento = 0
        total = subtotal - descuento
        if total > 30000:
            if self.necesita_envioCheckBox.isChecked():
                costo_envio = 0
        else:
            if self.necesita_envioCheckBox.isChecked():
                costo_envio = 2000
        total += costo_envio
        self.descuentoLineEdit.setText("$"+str(descuento))
        self.costo_envioLineEdit.setText("$"+str(costo_envio))
        self.totalLineEdit.setText("$"+str(total))

        # Desactiva el botón "-" si el carrito está vacío
        if len(self.carrito) > 0:
            self.btnMenos.setEnabled(True)
        else:
            self.btnMenos.setEnabled(False)