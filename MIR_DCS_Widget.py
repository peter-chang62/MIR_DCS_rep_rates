# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MIR_DCS_Widget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1112, 733)
        MainWindow.setMinimumSize(QtCore.QSize(1112, 733))
        MainWindow.setMaximumSize(QtCore.QSize(1112, 733))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_6.addWidget(self.checkBox)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.verticalLayout_6.addLayout(self.formLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_3.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_3.addWidget(self.radioButton_6)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_4)
        self.lcdNumber.setMinimumSize(QtCore.QSize(671, 60))
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_4.addWidget(self.lcdNumber)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.groupBox_4)
        self.lcdNumber_2.setMinimumSize(QtCore.QSize(671, 60))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout_2.addWidget(self.lcdNumber_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(spacerItem1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_7)
        self.tableWidget.setMaximumSize(QtCore.QSize(371, 415))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_19.addWidget(self.tableWidget)
        self.verticalLayout_20.addWidget(self.groupBox_7)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(spacerItem2)
        self.gridLayout.addLayout(self.verticalLayout_20, 0, 1, 2, 1)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setMaximumSize(QtCore.QSize(594, 153))
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_6.setMaximumSize(QtCore.QSize(284, 70))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.verticalLayout_10.addLayout(self.formLayout_2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_6)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.verticalLayout_10.addLayout(self.formLayout_3)
        self.verticalLayout_15.addWidget(self.groupBox_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_15)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_5.setMaximumSize(QtCore.QSize(280, 111))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.formLayout_10 = QtWidgets.QFormLayout()
        self.formLayout_10.setObjectName("formLayout_10")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setObjectName("label_7")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.verticalLayout_8.addLayout(self.formLayout_10)
        self.formLayout_11 = QtWidgets.QFormLayout()
        self.formLayout_11.setObjectName("formLayout_11")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setObjectName("label_8")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.verticalLayout_8.addLayout(self.formLayout_11)
        self.formLayout_12 = QtWidgets.QFormLayout()
        self.formLayout_12.setObjectName("formLayout_12")
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setObjectName("label_6")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        self.verticalLayout_8.addLayout(self.formLayout_12)
        spacerItem4 = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        self.horizontalLayout_3.addWidget(self.groupBox_5)
        self.verticalLayout_16.addLayout(self.horizontalLayout_3)
        self.verticalLayout_18.addWidget(self.groupBox_8)
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setMaximumSize(QtCore.QSize(574, 221))
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_13 = QtWidgets.QLabel(self.groupBox_9)
        self.label_13.setObjectName("label_13")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.horizontalLayout_5.addLayout(self.formLayout_8)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_9 = QtWidgets.QLabel(self.groupBox_9)
        self.label_9.setObjectName("label_9")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.horizontalLayout_5.addLayout(self.formLayout_4)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_10 = QtWidgets.QLabel(self.groupBox_9)
        self.label_10.setObjectName("label_10")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(141, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.verticalLayout_9.addLayout(self.formLayout_5)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_11 = QtWidgets.QLabel(self.groupBox_9)
        self.label_11.setObjectName("label_11")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(141, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.verticalLayout_9.addLayout(self.formLayout_6)
        self.horizontalLayout_9.addLayout(self.verticalLayout_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_9)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_13.addWidget(self.label_14)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_13.addWidget(self.lineEdit_12)
        self.horizontalLayout_6.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_9)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_14.addWidget(self.label_15)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_14.addWidget(self.lineEdit_13)
        self.horizontalLayout_6.addLayout(self.verticalLayout_14)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_12 = QtWidgets.QLabel(self.groupBox_9)
        self.label_12.setObjectName("label_12")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_9)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_7.setChecked(True)
        self.radioButton_7.setObjectName("radioButton_7")
        self.horizontalLayout_4.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_8.setObjectName("radioButton_8")
        self.horizontalLayout_4.addWidget(self.radioButton_8)
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.groupBox_3)
        self.horizontalLayout_7.addLayout(self.formLayout_7)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        self.verticalLayout_17.addLayout(self.verticalLayout_11)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.formLayout_9 = QtWidgets.QFormLayout()
        self.formLayout_9.setObjectName("formLayout_9")
        self.label_16 = QtWidgets.QLabel(self.groupBox_9)
        self.label_16.setObjectName("label_16")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_8.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.verticalLayout_12.addLayout(self.formLayout_9)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_9)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_12.addWidget(self.checkBox_2)
        self.horizontalLayout_8.addLayout(self.verticalLayout_12)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayout_17.addLayout(self.horizontalLayout_8)
        self.verticalLayout_18.addWidget(self.groupBox_9)
        self.gridLayout.addLayout(self.verticalLayout_18, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1112, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Counter Read Out"))
        self.checkBox.setText(_translate("MainWindow", "Mixing Down Rep-Rate"))
        self.label.setText(_translate("MainWindow", "Synthesizer Frequency (MHz)"))
        self.lineEdit.setText(_translate("MainWindow", "1010"))
        self.groupBox.setTitle(_translate("MainWindow", "Comb 1"))
        self.radioButton.setText(_translate("MainWindow", "Synthesizer > frep"))
        self.radioButton_2.setText(_translate("MainWindow", "Synthesizer < frep"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Comb 2"))
        self.radioButton_5.setText(_translate("MainWindow", "Synthesizer > frep"))
        self.radioButton_6.setText(_translate("MainWindow", "Synthesizer < frep"))
        self.label_3.setText(_translate("MainWindow", "Comb 1 Rep Rate"))
        self.label_2.setText(_translate("MainWindow", "Comb 2 Rep Rate"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Suggested Parameters"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "N Comb 1 Closest to CW"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "N Comb 2 Closest to CW"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Delta N"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Comb 1 Rep Rate (MHz)"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Comb 2 Rep Rate (MHz)"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Delta Rep Rate (MHz)"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Optical Nyquist Range (THz)"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "# Teeth Comb 1 in 2 x Nyquist"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "# Teeth Comb 2 in 2 x Nyquist"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "Points per IFG"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "Prime Factors"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "Region lower bound (nm)"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "Region upper bound (nm)"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Best Co-Averaging Conditions"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Preferred Nyquist Window"))
        self.label_4.setText(_translate("MainWindow", "Region Upper Bound (nm)"))
        self.label_5.setText(_translate("MainWindow", "Region Lower Bound (nm)"))
        self.label_7.setText(_translate("MainWindow", "Region Lower Freq (THz)"))
        self.label_8.setText(_translate("MainWindow", "Region Upper Freq (THz)"))
        self.label_6.setText(_translate("MainWindow", "Region Bandwidth (THz)"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Input Parameters"))
        self.label_13.setText(_translate("MainWindow", "CW wavelength (nm)"))
        self.label_9.setText(_translate("MainWindow", "CW frequency (THz)"))
        self.label_10.setText(_translate("MainWindow", "Comb 1 Rep Rate (MHz)"))
        self.label_11.setText(_translate("MainWindow", "Comb 2 Rep Rate (MHz)"))
        self.label_14.setText(_translate("MainWindow", "N Comb 1 closest to CW"))
        self.label_15.setText(_translate("MainWindow", "N Comb 2 closest to CW"))
        self.label_12.setText(_translate("MainWindow", "Clocking Comb"))
        self.radioButton_7.setText(_translate("MainWindow", "Comb 1"))
        self.radioButton_8.setText(_translate("MainWindow", "Comb 2"))
        self.label_16.setText(_translate("MainWindow", "Desired delta N"))
        self.checkBox_2.setText(_translate("MainWindow", "Use Rep Rates from Counter"))