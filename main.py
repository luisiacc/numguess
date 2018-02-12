from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import qdarkstyle
import logic
import icon

class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setWindowIcon(QIcon(':numguess_1.png'))

        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.row_count = 0

        self.entered_data()
        self.progressBar = QProgressBar()
        self.progressBar.setValue (0)
        self.mainLayout = QVBoxLayout(self)
        self.buttonsLayout = QHBoxLayout()
        # elements
        self.resetButton = QPushButton('Reiniciar', clicked=self.resetFields)
        self.addButton = QPushButton('Añadir', clicked=self.addElemToList)
        self.quitButton = QPushButton('Salir', clicked=self.close)

        self.buttonsLayout.addStretch(1)
        self.buttonsLayout.addWidget(self.addButton)
        self.buttonsLayout.addWidget(self.resetButton)
        self.buttonsLayout.addWidget(self.quitButton)
        self.buttonsLayout.addStretch (1)

        self.mainLayout.addWidget(self.parameters_box())
        self.mainLayout.addLayout(self.buttonsLayout)
        self.mainLayout.addLayout(self.fieldsLay)
        self.mainLayout.addWidget(self.progressBar)

        action.finished.connect(self.updateResults)


    def parameters_box(self):
        box = QGroupBox('Datos')

        self.numberLabel = QLabel('Número')
        self.numberEdit = QSpinBox()
        self.numberEdit.setMaximum(9999)
        self.numberEdit.setMinimum(1023)
        self.cowsLabel = QLabel('Vacas')
        self.cowsSpin = QSpinBox()
        self.cowsSpin.setMaximum(4)
        self.bullLabel = QLabel('Toros')
        self.bullSpin = QSpinBox()
        self.bullSpin.setMaximum(3)

        self.lay = QGridLayout(box)
        self.lay.addWidget(self.numberLabel, 0, 0)
        self.lay.addWidget(self.numberEdit, 1, 0)
        self.lay.addWidget(self.cowsLabel, 0, 2)
        self.lay.addWidget(self.cowsSpin, 1, 2)
        self.lay.addWidget(self.bullLabel, 0, 1)
        self.lay.addWidget(self.bullSpin, 1, 1)

        return box

    def entered_data(self):
        TableLabel = QLabel('Historial')
        self.viewEntrance = QTableWidget()
        self.viewEntrance.setFixedWidth(235)
        self.viewEntrance.setColumnCount(3)
        self.viewEntrance.setRowCount(1)
        self.viewEntrance.setRowHeight(0, 20)
        self.viewEntrance.setColumnWidth(1, 44)
        self.viewEntrance.setColumnWidth (2, 43)
        self.viewEntrance.setHorizontalHeaderLabels(['Números', 'Toros', 'Vacas'])

        results = QLabel('Posibles resultados')
        self.viewResults = QTextBrowser()
        self.viewResults.setFixedWidth(100)

        self.fieldsLay = QGridLayout()
        self.fieldsLay.addWidget(results, 0, 0)
        self.fieldsLay.addWidget(self.viewResults, 1, 0)
        self.fieldsLay.addWidget(TableLabel, 0, 1)
        self.fieldsLay.addWidget(self.viewEntrance, 1, 1)

    def addElemToList(self):
        self.viewEntrance.setRowCount(self.row_count + 1)
        self.viewEntrance.setRowHeight(self.row_count, 20)
        self.viewEntrance.setItem(self.row_count, 0, QTableWidgetItem(str(self.numberEdit.value())))
        self.viewEntrance.setItem (self.row_count, 1, QTableWidgetItem (str (self.bullSpin.value ())))
        self.viewEntrance.setItem (self.row_count, 2, QTableWidgetItem (str (self.cowsSpin.value ())))
        self.row_count += 1

        AI.addStatistics(str(self.numberEdit.value()), self.bullSpin.value (), self.cowsSpin.value ())

        action.start()

    def resetFields(self):
        self.progressBar.setValue(0)
        self.viewEntrance.clear()
        self.viewEntrance.setHorizontalHeaderLabels (['Números', 'Toros', 'Vacas'])
        self.viewEntrance.setRowCount(1)
        self.row_count = 0
        self.viewResults.clear()
        self.numberEdit.setValue(1023)
        self.cowsSpin.setValue(0)
        self.bullSpin.setValue(0)
        AI.results = AI.numTable
        AI.statistics = []
        action.finished.connect (self.updateResults)

    def updateResults(self, li):
        self.viewResults.clear()
        self.progressBar.setMaximum(len(li))
        self.progressBar.setValue(0)
        for elem in li:
            self.progressBar.setValue(self.progressBar.value()+1)
            self.viewResults.append(elem)

        if not self.viewResults.toPlainText():
            QMessageBox.information(self, 'Error', 'Pusiste un dato mal soquete')

    def updateLogic(self):
        pass


class ActionThread(QThread):
    finished = pyqtSignal(list)
    def __init__(self):
        super(ActionThread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        self.finished.emit(AI.resolve())

if __name__ == '__main__':
    AI = logic.Results()
    action = ActionThread()
    app = QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    form = MainForm()
    form.show()
    app.exec_()