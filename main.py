import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from VentIniciarSesion import VentIniciarSesion
from VentModificarStock import VentModificarStock

class main(QMainWindow):
           
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = VentModificarStock()
        self.ui.setupUi(self)
                
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    sys.exit(app.exec_())