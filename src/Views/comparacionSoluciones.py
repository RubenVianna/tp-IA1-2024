import sys
from Controllers.escaladaSimple import calcularEscaladaSimple
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
        text_layout.addWidget(self.text_edit1)

        # Segundo QTextEdit
        self.text_edit2 = QTextEdit(self)
        self.text_edit2.setReadOnly(True)
        text_layout.addWidget(self.text_edit2)

        layout.addLayout(text_layout)

        self.button = QPushButton("Ver Análisis", self)
        self.button.clicked.connect(self.generar_salida)
        layout.addWidget(self.button)

        self.setLayout(layout)

        # Redirigir stdout a los QTextEdit correspondientes
        self.emitting_stream1 = EmittingStream(self.text_edit1)
        self.emitting_stream2 = EmittingStream(self.text_edit2)

    def generar_salida(self):
        sys.stdout = self.emitting_stream1
        calcularEscaladaSimple(self.nodos)
   
        sys.stdout = self.emitting_stream2
        calcularMaximaPendiente(self.nodos)
        sys.stdout = sys.__stdout__  # Restaurar stdout original