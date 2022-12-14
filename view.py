# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 485)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 581, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.CircleTab = QtWidgets.QWidget()
        self.CircleTab.setObjectName("CircleTab")
        self.CirclePic = QtWidgets.QLabel(self.CircleTab)
        self.CirclePic.setGeometry(QtCore.QRect(30, 20, 301, 281))
        self.CirclePic.setText("")
        self.CirclePic.setPixmap(QtGui.QPixmap("../../Downloads/Circle.jpg"))
        self.CirclePic.setScaledContents(True)
        self.CirclePic.setObjectName("CirclePic")
        self.RadiusLabel = QtWidgets.QLabel(self.CircleTab)
        self.RadiusLabel.setGeometry(QtCore.QRect(370, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(24)
        self.RadiusLabel.setFont(font)
        self.RadiusLabel.setObjectName("RadiusLabel")
        self.RadiusInput = QtWidgets.QPlainTextEdit(self.CircleTab)
        self.RadiusInput.setGeometry(QtCore.QRect(480, 20, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.RadiusInput.setFont(font)
        self.RadiusInput.setAutoFillBackground(True)
        self.RadiusInput.setObjectName("RadiusInput")
        self.CircleButton = QtWidgets.QPushButton(self.CircleTab)
        self.CircleButton.setGeometry(QtCore.QRect(430, 260, 131, 51))
        self.CircleButton.setObjectName("CircleButton")
        self.CircleAreaLabel = QtWidgets.QLabel(self.CircleTab)
        self.CircleAreaLabel.setGeometry(QtCore.QRect(230, 330, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(24)
        self.CircleAreaLabel.setFont(font)
        self.CircleAreaLabel.setObjectName("CircleAreaLabel")
        self.CircleAnswer = QtWidgets.QLineEdit(self.CircleTab)
        self.CircleAnswer.setGeometry(QtCore.QRect(310, 340, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CircleAnswer.setFont(font)
        self.CircleAnswer.setObjectName("CircleAnswer")
        self.tabWidget.addTab(self.CircleTab, "")
        self.RectangleTab = QtWidgets.QWidget()
        self.RectangleTab.setObjectName("RectangleTab")
        self.RectanglePic = QtWidgets.QLabel(self.RectangleTab)
        self.RectanglePic.setGeometry(QtCore.QRect(10, 40, 371, 251))
        self.RectanglePic.setText("")
        self.RectanglePic.setPixmap(QtGui.QPixmap("../../Downloads/Rectangle.jpg"))
        self.RectanglePic.setScaledContents(True)
        self.RectanglePic.setObjectName("RectanglePic")
        self.LengthLabel = QtWidgets.QLabel(self.RectangleTab)
        self.LengthLabel.setGeometry(QtCore.QRect(370, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(24)
        self.LengthLabel.setFont(font)
        self.LengthLabel.setObjectName("LengthLabel")
        self.LengthInput = QtWidgets.QPlainTextEdit(self.RectangleTab)
        self.LengthInput.setGeometry(QtCore.QRect(480, 20, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.LengthInput.setFont(font)
        self.LengthInput.setAutoFillBackground(True)
        self.LengthInput.setObjectName("LengthInput")
        self.WidthInput = QtWidgets.QPlainTextEdit(self.RectangleTab)
        self.WidthInput.setGeometry(QtCore.QRect(480, 110, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.WidthInput.setFont(font)
        self.WidthInput.setAutoFillBackground(True)
        self.WidthInput.setObjectName("WidthInput")
        self.WidthLabel = QtWidgets.QLabel(self.RectangleTab)
        self.WidthLabel.setGeometry(QtCore.QRect(370, 110, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(24)
        self.WidthLabel.setFont(font)
        self.WidthLabel.setObjectName("WidthLabel")
        self.RectangleButton = QtWidgets.QPushButton(self.RectangleTab)
        self.RectangleButton.setGeometry(QtCore.QRect(430, 260, 131, 51))
        self.RectangleButton.setObjectName("RectangleButton")
        self.RectangleAreaLabel = QtWidgets.QLabel(self.RectangleTab)
        self.RectangleAreaLabel.setGeometry(QtCore.QRect(230, 330, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(24)
        self.RectangleAreaLabel.setFont(font)
        self.RectangleAreaLabel.setObjectName("RectangleAreaLabel")
        self.RectangleAnswer = QtWidgets.QLineEdit(self.RectangleTab)
        self.RectangleAnswer.setGeometry(QtCore.QRect(310, 340, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.RectangleAnswer.setFont(font)
        self.RectangleAnswer.setObjectName("RectangleAnswer")
        self.tabWidget.addTab(self.RectangleTab, "")
        self.SquareTab = QtWidgets.QWidget()
        self.SquareTab.setObjectName("SquareTab")
        self.SquarePic = QtWidgets.QLabel(self.SquareTab)
        self.SquarePic.setGeometry(QtCore.QRect(-60, 0, 481, 311))
        self.SquarePic.setText("")
        self.SquarePic.setPixmap(QtGui.QPixmap("../../Downloads/Square.jpg"))
        self.SquarePic.setScaledContents(True)
        self.SquarePic.setObjectName("SquarePic")
        self.SideInput = QtWidgets.QPlainTextEdit(self.SquareTab)
        self.SideInput.setGeometry(QtCore.QRect(480, 20, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.SideInput.setFont(font)
        self.SideInput.setAutoFillBackground(True)
        self.SideInput.setObjectName("SideInput")
        self.SideLabel = QtWidgets.QLabel(self.SquareTab)
        self.SideLabel.setGeometry(QtCore.QRect(400, 20, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(24)
        self.SideLabel.setFont(font)
        self.SideLabel.setObjectName("SideLabel")
        self.SquareButton = QtWidgets.QPushButton(self.SquareTab)
        self.SquareButton.setGeometry(QtCore.QRect(430, 260, 131, 51))
        self.SquareButton.setObjectName("SquareButton")
        self.SquareAreaLabel = QtWidgets.QLabel(self.SquareTab)
        self.SquareAreaLabel.setGeometry(QtCore.QRect(230, 330, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(24)
        self.SquareAreaLabel.setFont(font)
        self.SquareAreaLabel.setObjectName("SquareAreaLabel")
        self.SquareAnswer = QtWidgets.QLineEdit(self.SquareTab)
        self.SquareAnswer.setGeometry(QtCore.QRect(310, 340, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SquareAnswer.setFont(font)
        self.SquareAnswer.setObjectName("SquareAnswer")
        self.tabWidget.addTab(self.SquareTab, "")
        self.TriangleTab = QtWidgets.QWidget()
        self.TriangleTab.setObjectName("TriangleTab")
        self.TrianglePic = QtWidgets.QLabel(self.TriangleTab)
        self.TrianglePic.setGeometry(QtCore.QRect(-40, -10, 441, 331))
        self.TrianglePic.setText("")
        self.TrianglePic.setPixmap(QtGui.QPixmap("../../Downloads/Triangle.jpg"))
        self.TrianglePic.setScaledContents(True)
        self.TrianglePic.setObjectName("TrianglePic")
        self.HeightInput = QtWidgets.QPlainTextEdit(self.TriangleTab)
        self.HeightInput.setGeometry(QtCore.QRect(480, 110, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.HeightInput.setFont(font)
        self.HeightInput.setAutoFillBackground(True)
        self.HeightInput.setObjectName("HeightInput")
        self.HeightLabel = QtWidgets.QLabel(self.TriangleTab)
        self.HeightLabel.setGeometry(QtCore.QRect(370, 110, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(24)
        self.HeightLabel.setFont(font)
        self.HeightLabel.setObjectName("HeightLabel")
        self.BaseInput = QtWidgets.QPlainTextEdit(self.TriangleTab)
        self.BaseInput.setGeometry(QtCore.QRect(480, 20, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.BaseInput.setFont(font)
        self.BaseInput.setAutoFillBackground(True)
        self.BaseInput.setObjectName("BaseInput")
        self.BaseLabel = QtWidgets.QLabel(self.TriangleTab)
        self.BaseLabel.setGeometry(QtCore.QRect(370, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(24)
        self.BaseLabel.setFont(font)
        self.BaseLabel.setObjectName("BaseLabel")
        self.TriangleButton = QtWidgets.QPushButton(self.TriangleTab)
        self.TriangleButton.setGeometry(QtCore.QRect(430, 260, 131, 51))
        self.TriangleButton.setObjectName("TriangleButton")
        self.TriangleAreaLabel = QtWidgets.QLabel(self.TriangleTab)
        self.TriangleAreaLabel.setGeometry(QtCore.QRect(230, 330, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(24)
        self.TriangleAreaLabel.setFont(font)
        self.TriangleAreaLabel.setObjectName("TriangleAreaLabel")
        self.TriangleAnswer = QtWidgets.QLineEdit(self.TriangleTab)
        self.TriangleAnswer.setGeometry(QtCore.QRect(310, 340, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TriangleAnswer.setFont(font)
        self.TriangleAnswer.setObjectName("TriangleAnswer")
        self.tabWidget.addTab(self.TriangleTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AreaCalculator"))
        self.RadiusLabel.setText(_translate("MainWindow", "Radius:"))
        self.CircleButton.setText(_translate("MainWindow", "Calculate! "))
        self.CircleAreaLabel.setText(_translate("MainWindow", "Area:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CircleTab), _translate("MainWindow", "Circle"))
        self.LengthLabel.setText(_translate("MainWindow", "Length:"))
        self.WidthLabel.setText(_translate("MainWindow", "Width:"))
        self.RectangleButton.setText(_translate("MainWindow", "Calculate! "))
        self.RectangleAreaLabel.setText(_translate("MainWindow", "Area:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RectangleTab), _translate("MainWindow", "Rectangle"))
        self.SideLabel.setText(_translate("MainWindow", "Side:"))
        self.SquareButton.setText(_translate("MainWindow", "Calculate! "))
        self.SquareAreaLabel.setText(_translate("MainWindow", "Area:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SquareTab), _translate("MainWindow", "Square"))
        self.HeightLabel.setText(_translate("MainWindow", "Height:"))
        self.BaseLabel.setText(_translate("MainWindow", "Base:"))
        self.TriangleButton.setText(_translate("MainWindow", "Calculate! "))
        self.TriangleAreaLabel.setText(_translate("MainWindow", "Area:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TriangleTab), _translate("MainWindow", "Triangle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
