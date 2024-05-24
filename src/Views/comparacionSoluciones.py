import sys
from Controllers.escaladaSimple import calcularEscaladaSimple
from PyQt5.QtGui import QFont
from Controllers.maximaPendiente import calcularMaximaPendiente
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QPushButton, QTextEdit

class EmittingStream:
    def __init__(self, text_edit):
        self.text_edit = text_edit

    def write(self, text):
        cursor = self.text_edit.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(text)
        self.text_edit.setTextCursor(cursor)
        self.text_edit.ensureCursorVisible()

    def flush(self):
        pass  # No hacemos nada aquí, pero es necesario implementar este método

class ComparacionSoluciones(QWidget):
    def __init__(self, nodos):
        super().__init__()
        self.setWindowTitle("Comparacion de Escalada Simple y Maxima Pendiente")
        self.setGeometry(100, 100, 800, 400)
        self.nodos = nodos
        layout = QVBoxLayout()

        # Layout horizontal para los cuadros de texto
        text_layout = QHBoxLayout()

        # Primer QTextEdit
        self.text_edit1 = QTextEdit(self)
        self.text_edit1.setReadOnly(True)
        self.text_edit1.setFont(QFont('Arial', 9))
        text_layout.addWidget(self.text_edit1)

        # Segundo QTextEdit
        self.text_edit2 = QTextEdit(self)
        self.text_edit2.setReadOnly(True)
        self.text_edit2.setFont(QFont('Arial', 9))
        text_layout.addWidget(self.text_edit2)

        layout.addLayout(text_layout)

        self.button = QPushButton("Cerrar", self)
        self.button.clicked.connect(self.cerrarVentana)
        layout.addWidget(self.button)

        self.setLayout(layout)

        # Redirigir stdout a los QTextEdit correspondientes
        self.emitting_stream1 = EmittingStream(self.text_edit1)
        self.emitting_stream2 = EmittingStream(self.text_edit2)

        self.generarSalida()

    def generarSalida(self):
        sys.stdout = self.emitting_stream1
        calcularEscaladaSimple(self.nodos)
   
        sys.stdout = self.emitting_stream2
        calcularMaximaPendiente(self.nodos)
        sys.stdout = sys.__stdout__  # Restaurar stdout original
    
    def cerrarVentana(self):
        self.close()