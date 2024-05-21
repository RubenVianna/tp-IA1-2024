from PyQt5.QtWidgets import QListView, QComboBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt

class CheckableComboBox(QComboBox):
    def __init__(self, parent=None):
        super(CheckableComboBox, self).__init__(parent)
        self.setModel(CheckableComboBoxModel(self))
        self.view().pressed.connect(self.handleItemPressed)
        self.setEditable(False)
        # Añadir la leyenda "Seleccionar"
        item = QStandardItem("Seleccionar")
        item.setFlags(Qt.ItemIsEnabled)
        self.model().appendRow(item)

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item and item.text() == "Seleccionar":
            return  # Ignorar el ítem "Seleccionar"
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)

    def checkedItems(self):
        checked_items = []
        for index in range(1, self.count()):  # Comenzar desde 1 para ignorar "Seleccionar"
            if self.model().item(index).checkState() == Qt.Checked:
                checked_items.append(self.model().item(index).text())
        return checked_items


class CheckableComboBoxModel(QStandardItemModel):
    def flags(self, index):
        item = self.item(index.row())
        if item and item.text() == "Seleccionar":
            return Qt.ItemIsEnabled  # Solo habilitado, no seleccionable
        return Qt.ItemIsUserCheckable | Qt.ItemIsEnabled

    def data(self, index, role=Qt.DisplayRole):
        item = self.item(index.row())
        if role == Qt.CheckStateRole and item and item.text() != "Seleccionar":
            return item.checkState()
        return super(CheckableComboBoxModel, self).data(index, role)
    
