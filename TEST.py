import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class Boleta:
    def __init__(self, nombre_cliente, productos, subtotal, descuento, total):
        self.nombre_cliente = nombre_cliente
        self.productos = productos
        self.subtotal = subtotal
        self.descuento = descuento
        self.total = total

class VentanaBoleta(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configuramos la ventana principal
        self.setWindowTitle('Boleta')
        self.setGeometry(100, 100, 400, 350)

        # Creamos los widgets de la interfaz
        self.label_nombre_cliente = QLabel('Nombre del cliente:', self)
        self.label_nombre_cliente.move(50, 50)

        self.lineedit_nombre_cliente = QLineEdit(self)
        self.lineedit_nombre_cliente.move(200, 50)

        self.label_productos = QLabel('Productos:', self)
        self.label_productos.move(50, 100)

        self.lineedit_productos = QLineEdit(self)
        self.lineedit_productos.move(200, 100)

        self.label_subtotal = QLabel('Subtotal:', self)
        self.label_subtotal.move(50, 150)

        self.lineedit_subtotal = QLineEdit(self)
        self.lineedit_subtotal.move(200, 150)

        self.label_descuento = QLabel('Descuento:', self)
        self.label_descuento.move(50, 200)

        self.lineedit_descuento = QLineEdit(self)
        self.lineedit_descuento.move(200, 200)

        self.label_total = QLabel('Total:', self)
        self.label_total.move(50, 250)

        self.lineedit_total = QLineEdit(self)
        self.lineedit_total.move(200, 250)

        self.button_guardar = QPushButton('Guardar', self)
        self.button_guardar.move(150, 300)
        self.button_guardar.clicked.connect(self.guardar_boleta)

    
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana_boleta = VentanaBoleta()
    ventana_boleta.show()
    sys.exit(app.exec_())
