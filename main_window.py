import PyQt5.QtWidgets as qt
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
import pyqtgraph as pg
from MIR_DCS_Widget import Ui_MainWindow


class Main_Window(qt.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # constrain all lined edit entries to doubles
        self.le_synth_freq.setValidator(qtg.QDoubleValidator())
        self.le_reg_up_nm.setValidator(qtg.QDoubleValidator())
        self.le_reg_lw_nm.setValidator(qtg.QDoubleValidator())
        self.le_reg_up_thz.setValidator(qtg.QDoubleValidator())
        self.le_reg_lw_thz.setValidator(qtg.QDoubleValidator())
        self.le_reg_bdwdth_thz.setValidator(qtg.QDoubleValidator())
        self.le_cw_nm.setValidator(qtg.QDoubleValidator())
        self.le_cw_thz.setValidator(qtg.QDoubleValidator())
        self.le_comb1_frep.setValidator(qtg.QDoubleValidator())
        self.le_comb2_frep.setValidator(qtg.QDoubleValidator())
        self.le_comb1_N_CW.setValidator(qtg.QDoubleValidator())
        self.le_comb2_N_CW.setValidator(qtg.QDoubleValidator())
        self.le_desired_delta_N.setValidator(qtg.QDoubleValidator())

        table_length = 13
        table_entries = [self.tableWidget.verticalHeaderItem(i).text() for i in
                         range(table_length)]
        entries = [None for i in range(table_length)]
        self.table_entries = dict(zip(table_entries, entries))

    def floatValidator(self, string):
        try:
            f = float(string)
            return f
        except:
            return False

    @property
    def synth_freq_MHz(self):
        return float(self.le_synth_freq.text())

    @property
    def synth_g_frep_comb1(self):
        return self.rdbtn_synth_g_frep_comb1.isChecked()

    @property
    def synth_g_frep_comb2(self):
        return self.rdbtn_synth_g_frep_comb2.isChecked()

    @property
    def des_reg_up_nm(self):
        return float(self.le_reg_up_nm.text())

    @property
    def des_reg_lw_nm(self):
        return float(self.le_reg_lw_nm.text())

    @property
    def guessed_cw_nm(self):
        return float(self.le_cw_nm.text())

    @property
    def guessed_cw_thz(self):
        return float(self.le_cw_thz.text())

    @property
    def comb1_rep_rate(self):
        return float(self.le_comb1_frep.text())
    
    @property
    def comb2_rep_rate(self):
        return float(self.le_comb2_frep.text())


if __name__ == '__main__':
    app = qt.QApplication([])
    window = Main_Window()
    app.exec()
