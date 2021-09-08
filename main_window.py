import PyQt5.QtWidgets as qt
import pyqtgraph as pg
from MIR_DCS_Widget import Ui_MainWindow


class Main_Window(qt.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = qt.QApplication([])
    window = Main_Window()
    app.exec()
