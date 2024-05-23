import sys
from PyQt5.QtWidgets import QApplication
from Views.vistaInicial import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventanaPrincipal = Inicio()
    ventanaPrincipal.show()
    sys.exit(app.exec_())