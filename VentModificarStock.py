from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox, QDialog
import csv, datetime
from VentAgregarStock import AgregarStockDialog

class VentModificarStock(object):
    def __init__(self):
        self.carrito = []  # Lista para almacenar los medicamentos del carrito
    
    def setupUi(self, VentModificarStock):
        ImagenBanner = QtGui.QPixmap('Imagenes/banner_modificar_stock.png')
        IconoRegresar = QtGui.QIcon('Imagenes/boton_regresar.png')
        IconoTitulo = QtGui.QIcon('Imagenes/icono_titulo.png')
        
        VentModificarStock.setWindowIcon(IconoTitulo)
        
        VentModificarStock.resize(884, 675)
        VentModificarStock.setMinimumSize(QtCore.QSize(884, 675))
        VentModificarStock.setMaximumSize(QtCore.QSize(884, 675))
        
        # Etiqueta imagen superior
        self.imagen_on_topLabel = QtWidgets.QLabel(VentModificarStock)
        self.imagen_on_topLabel.setGeometry(QtCore.QRect(0, 0, 884, 144))
        self.imagen_on_topLabel.setText("")
        self.imagen_on_topLabel.setPixmap(ImagenBanner.scaled(884, 144))
        
        # Boton regresar y accion al pulsar
        self.btnRegresar = QtWidgets.QPushButton(VentModificarStock)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.btnRegresar.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.btnRegresar.setIcon(IconoRegresar)
        self.btnRegresar.setIconSize(QtCore.QSize(60, 60))
        self.btnRegresar.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnRegresar.clicked.connect(VentModificarStock.close)

        # Tabla con columnas y filas y que sean 9 columnas [ID, Nombre, Precio, Stock, Descripcion, Stock Lote 1, Caducidad Lote 1, Stock Lote 2, Caducidad Lote 2]
        self.tableWidget = QtWidgets.QTableWidget(VentModificarStock)
        self.tableWidget.setGeometry(QtCore.QRect(10, 210, 680, 450))
        self.tableWidget.setColumnCount(9)
        
        # Ocultar columna de descripción
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setColumnHidden(4, True)
        
        # Para que no se puedan editar los medicamentos de la lista de medicamentos
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        # Boton informacion y accion al pulsar
        self.btnInfo = QtWidgets.QPushButton(VentModificarStock)
        self.btnInfo.setGeometry(QtCore.QRect(697, 210, 180, 60))
        self.btnInfo.clicked.connect(self.onActionBtnInfo)
        
        # Boton agregar stock y accion al pulsar
        self.BtnAgregar = QtWidgets.QPushButton(VentModificarStock)
        self.BtnAgregar.setGeometry(QtCore.QRect(697, 290, 180, 60))
        self.BtnAgregar.clicked.connect(self.onActionBtnAgregar)
        
        # Boton retirar stock y accion al pulsar
        self.BtnRetirar = QtWidgets.QPushButton(VentModificarStock)
        self.BtnRetirar.setGeometry(QtCore.QRect(697, 370, 180, 60))
        self.BtnRetirar.clicked.connect(self.onActionBtnRetirar)
        
        # Boton revisar caducidad y accion al pulsar
        self.btnCaducidad = QtWidgets.QPushButton(VentModificarStock)
        self.btnCaducidad.setGeometry(QtCore.QRect(697, 450, 180, 60))
        self.btnCaducidad.clicked.connect(self.onActionBtnCaducidad)
        
        # Boton guardar stock y accion al pulsar
        self.btnGuardar = QtWidgets.QPushButton(VentModificarStock)
        self.btnGuardar.setGeometry(QtCore.QRect(697, 600, 180, 60))
        self.btnGuardar.clicked.connect(self.onActionBtnGuardar)
        
        # Barra de busqueda y accion al actualizar el texto
        self.buscarLineEdit = QtWidgets.QLineEdit(VentModificarStock)
        self.buscarLineEdit.setGeometry(QtCore.QRect(10, 150, 864, 50))
        self.buscarLineEdit.setPlaceholderText("Ingrese el nombre o ID del medicamento")
        self.buscarLineEdit.setStyleSheet("font-size: 16px;")
        self.buscarLineEdit.textChanged.connect(self.buscarMedicamentos)

        self.retranslateUi(VentModificarStock)
        QtCore.QMetaObject.connectSlotsByName(VentModificarStock)
        
        # Cargar lista de medicamentos del CSV y actualiar datos (subtotal, total, entre otros)
        self.cargarMedicamentosCSV()
        
    # Metodo definir textos
    def retranslateUi(self, VentModificarStock):
        _translate = QtCore.QCoreApplication.translate
        VentModificarStock.setWindowTitle(_translate("VentModificarStock", "Vent - Modificar Stock de Productos"))
        self.BtnAgregar.setText(_translate("VentModificarStock", "Agregar Lote al Medicamento del\nproducto seleccionado (+)"))
        self.BtnRetirar.setText(_translate("VentModificarStock", "Retirar 1 al Stock del\nproducto seleccionado (-)"))
        self.btnInfo.setText(_translate("VentModificarStock", "Instrucciones (!)"))
        self.btnCaducidad.setText(_translate("VentModificarStock", "Revisar caducidad cercana de\nlos Medicamentos (!!!)"))
        self.btnGuardar.setText(_translate("VentModificarStock", "Confirmar Cambios"))

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
    def onActionBtnAgregar(self):
        fila_seleccionada = self.tableWidget.currentRow()

        if fila_seleccionada == -1:
            self.alertBox("Debe seleccionar un medicamento para agregar stock", "Agregar Stock")

        # Si se ha seleccionado un medicamento
        if fila_seleccionada != -1:
            if (int(self.tableWidget.item(fila_seleccionada, 7).text()) == 0):
                # Se abre una nueva ventana para ingresar la cantidad de stock y fecha de caducidad del Lote a agregar
                dialog = AgregarStockDialog()
                if dialog.exec_() == QDialog.Accepted:
                    nuevo_stock = dialog.get_stock()
                    fecha_caducidad = dialog.get_fecha_caducidad()

                    # Actualiza el stock en la tabla
                    self.tableWidget.setItem(fila_seleccionada, 7, QTableWidgetItem(nuevo_stock))
                    self.tableWidget.setItem(fila_seleccionada, 8, QTableWidgetItem(fecha_caducidad))
            else:
                self.alertBox("No puede agregar stock hasta que un Lote esté vacio\nEsto es para evitar la acumulación de Medicamentos", "Alerta")


    # Accion al pulsar boton menos, elimina medicamentos de la tableWidgetCarrito y agrega el stock devuelta en el tableWidget de medicamentos
    def onActionBtnRetirar(self):
        fila_seleccionada = self.tableWidget.currentRow()
        
        if fila_seleccionada == -1:
            self.alertBox("Debe seleccionar un medicamento para retirar stock", "Retirar Stock")
        
        # Si se ha seleccionado un medicamento
        if fila_seleccionada != -1:
            # Obtiene el stock del medicamento seleccionado
            stock_medicamento = int(self.tableWidget.item(fila_seleccionada, 3).text())
            stock_lote_1 = int(self.tableWidget.item(fila_seleccionada, 5).text())
            stock_lote_2 = int(self.tableWidget.item(fila_seleccionada, 7).text())
             
            if (stock_lote_1>0):
                # Retira 1 al stock del medicamento seleccionado en el Lote 1 y actualiza el Stock
                stock_lote_1 -= 1
                self.tableWidget.setItem(fila_seleccionada, 5, QTableWidgetItem(str(stock_lote_1)))
                self.tableWidget.setItem(fila_seleccionada, 3, QTableWidgetItem(str(stock_lote_1+stock_lote_2)))
            elif (stock_lote_2>0):
                # Retira 1 al stock del medicamento seleccionado en el Lote 2 y actualiza el Stock
                stock_lote_2 -= 1
                self.tableWidget.setItem(fila_seleccionada, 7, QTableWidgetItem(str(stock_lote_2)))
                self.tableWidget.setItem(fila_seleccionada, 3, QTableWidgetItem(str(stock_lote_1+stock_lote_2)))
            else:
                self.alertBox("No se puede retirar más stock", "Alerta Stock")
            
    def onActionBtnInfo(self):
        self.alertBox("- Para agregar nuevo stock debe un medicamento con Lote libre desde \nla lista de medicamentos y hacer click en Agregar nuevo Lote\n"
                      "\n- Para retirar stock debe seleccionarlo desde la lista de medicamentos y \nhacer click en Retirar 1 al Stock\n"
                      "\n- Para ver en cuales productos están por vencer, hacer click en \nRevisar caducidad cercana de los Medicamentos\n"
                      "\n- Para guardar los cambios hechos haga click en Confirmar Cambios", "Lista de Instrucciones")
        
    def onActionBtnCaducidad(self):
        # Toma la fecha actual y pone como limite un mes para caducidad cercana
        fecha_actual = datetime.date.today()
        limite_mes = fecha_actual + datetime.timedelta(days=30)

        # Arreglos para imprimir los datos en una alertBox
        medicamentos_por_caducar = []
        dias_para_caducar = []

        # Obtiene la caducidad cercana de los medicamentos y si es menor a un mes la guarda como medicamentos_por_caducar
        for fila in range(self.tableWidget.rowCount()):
            caducidad = self.tableWidget.item(fila, 6).text()
            caducidad = datetime.datetime.strptime(caducidad, "%d/%m/%Y").date()

            if caducidad < limite_mes:
                medicamentos = self.tableWidget.item(fila, 1).text()
                medicamentos_por_caducar.append(medicamentos)

                dias_restantes = (caducidad - fecha_actual).days
                dias_para_caducar.append(dias_restantes)

        # Si el medicamento esta por caducar manda alertbox
        if medicamentos_por_caducar:
            mensaje = "Medicamentos por caducar:\n\n"
            for i in range(len(medicamentos_por_caducar)):
                medicamento = medicamentos_por_caducar[i]
                dias_restantes = dias_para_caducar[i]
                mensaje += medicamento+": "+(str(dias_restantes))+" días\n"
            self.alertBox(mensaje, "Medicamentos por caducar")
        else:
            self.alertBox("No hay medicamentos cercanos por caducar", "Medicamentos por caducar")
            
    def onActionBtnGuardar(self):
        for fila in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(fila, 5).text() == '0':
                self.actualizarLotes(fila)
        # Abre el archivo CSV para guardar los datos
        with open('ArchivosCSV/Medicamentos.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # Escribe los encabezados de las columnas
            encabezados = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(self.tableWidget.columnCount())]
            writer.writerow(encabezados)
            # Sobreescribe los datos de los medicamentos con los nuevos valores (El nuevo stock despues de modificar el stock)
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
        self.alertBox("Se han guardado los cambios","Stock Actulizado")
        
    def actualizarLotes(self, fila):
        # Lo que hace es que si el stock del lote 1 es igual a 0 copia los datos del lote 2 al lote 1, dejando el lote 2 libre para agregar un nuevo lote de medicamentos
        if self.tableWidget.item(fila, 7) is not None:
            stock_lote_2 = self.tableWidget.item(fila, 7).text()
            self.tableWidget.setItem(fila, 5, QTableWidgetItem(stock_lote_2))
            self.tableWidget.setItem(fila, 7, QTableWidgetItem("0"))
            
            vencimiento_lote_2 = self.tableWidget.item(fila, 8).text()
            self.tableWidget.setItem(fila, 6, QTableWidgetItem(vencimiento_lote_2))
            self.tableWidget.setItem(fila, 8, QTableWidgetItem(""))
            if (self.tableWidget.item(fila, 5).text() == "0"):
                self.tableWidget.setItem(fila, 6, QTableWidgetItem(""))
    
    # Ventana para agregar nuevo stock en el Lote disponible 
    def agregarStockDialog(self):
        dialog = AgregarStockDialog()
        if dialog.exec_():
            cantidad = int(dialog.stock_edit.text())
            fecha_caducidad = dialog.fecha_edit.date().toString("yyyy-MM-dd")