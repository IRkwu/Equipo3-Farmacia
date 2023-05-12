from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
import csv, sys

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

        # Tabla con columnas y filas y que sean 5 columnas [ID, Nombre, Precio, Stock, Descripcion]
        self.tableWidget = QtWidgets.QTableWidget(VentModificarStock)
        self.tableWidget.setGeometry(QtCore.QRect(10, 210, 674, 450))
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
        self.tableWidget.setColumnHidden(4, True)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        
        # Para que no se puedan editar los medicamentos de la lista de medicamentos
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        # Boton informacion y accion al pulsar
        self.btnInfo = QtWidgets.QPushButton(VentModificarStock)
        self.btnInfo.setGeometry(QtCore.QRect(694, 210, 180, 60))
        self.btnInfo.clicked.connect(self.onActionBtnInfo)
        
        # Boton agregar stock y accion al pulsar
        self.BtnAgregar = QtWidgets.QPushButton(VentModificarStock)
        self.BtnAgregar.setGeometry(QtCore.QRect(694, 290, 180, 60))
        self.BtnAgregar.clicked.connect(self.onActionBtnAgregar)
        
        # Boton retirar stock y accion al pulsar
        self.BtnRetirar = QtWidgets.QPushButton(VentModificarStock)
        self.BtnRetirar.setGeometry(QtCore.QRect(694, 370, 180, 60))
        self.BtnRetirar.clicked.connect(self.onActionBtnRetirar)
        
        # Boton revisar caducidad y accion al pulsar
        self.btnCaducidad = QtWidgets.QPushButton(VentModificarStock)
        self.btnCaducidad.setGeometry(QtCore.QRect(694, 450, 180, 60))
        self.btnCaducidad.clicked.connect(self.onActionBtnCaducidad)
        
        # Boton guardar stock y accion al pulsar
        self.btnGuardar = QtWidgets.QPushButton(VentModificarStock)
        self.btnGuardar.setGeometry(QtCore.QRect(694, 600, 180, 60))
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
        self.BtnAgregar.setText(_translate("VentModificarStock", "Agregar 1 al Stock del\nproducto seleccionado (+)"))
        self.BtnRetirar.setText(_translate("VentModificarStock", "Retirar 1 al Stock del\nproducto seleccionado (-)"))
        self.btnInfo.setText(_translate("VentModificarStock", "Instrucciones (!)"))
        self.btnCaducidad.setText(_translate("VentModificarStock", "Revisar caducidad del stock \n(!!!)"))
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
        # Buscar los medicamentos que coinciden con la cadena de búsqueda y mostrarlos en la tabla
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
            # Obtiene el stock del medicamento seleccionado
            stock_medicamento = int(self.tableWidget.item(fila_seleccionada, 3).text())

            # Agrega 1 al stock del medicamento seleccionado
            stock_medicamento += 1
            self.tableWidget.setItem(fila_seleccionada, 3, QTableWidgetItem(str(stock_medicamento)))          

    # Accion al pulsar boton menos, elimina medicamentos de la tableWidgetCarrito y agrega el stock devuelta en el tableWidget de medicamentos
    def onActionBtnRetirar(self):
        fila_seleccionada = self.tableWidget.currentRow()
        
        if fila_seleccionada == -1:
            self.alertBox("Debe seleccionar un medicamento para retirar stock", "Retirar Stock")
        
        # Si se ha seleccionado un medicamento
        if fila_seleccionada != -1:
            # Obtiene el stock del medicamento seleccionado
            stock_medicamento = int(self.tableWidget.item(fila_seleccionada, 3).text())
             
            if (stock_medicamento>0):
                # Retira 1 al stock del medicamento seleccionado
                stock_medicamento -= 1
                self.tableWidget.setItem(fila_seleccionada, 3, QTableWidgetItem(str(stock_medicamento)))
            else:
                self.alertBox("No se puede retirar más stock", "Alerta Stock")
            
    def onActionBtnInfo(self):
        self.alertBox("- Para agregar stock debe seleccionarlo desde la lista de medicamentos y \nhacer click en Agregar 1 al Stock\n"
                      "\n- Para retirar stock debe seleccionarlo desde la lista de medicamentos y \nhacer click en Retirar 1 al Stock\n"
                      "\n- Para ver en cuanto tiempo caducen cierto productos, hacer click en \nRevisar Caducidad del Stock\n"
                      "\n- Para guardar los cambios hechos haga click en Confirmar Cambios", "Lista de Instrucciones")
        
    def onActionBtnCaducidad(self):
        print("La cudacidad :)")
        
    def onActionBtnGuardar(self):
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
        self.alertBox("Se han guardado los cambios","Stock Actulizado")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = VentModificarStock()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())