from PyQt5.QtWidgets import *
from view import Ui_MainWindow
import math


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.CircleButton.clicked.connect(lambda: self.calcCircle())
        self.RectangleButton.clicked.connect(lambda: self.calcRectangle())
        self.SquareButton.clicked.connect(lambda: self.calcSquare())
        self.TriangleButton.clicked.connect(lambda: self.calcTriangle())

    def calcCircle(self):
        """
        Method for checking valid input, calculates the area of a circle, displays said area, then clears the input.
        """
        try:
            givenRadius = int(self.RadiusInput.toPlainText())
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Must be an integer greater than 0")
            msg.setWindowTitle("Bro, come on now...")
            msg.exec_()

        # formatting and displaying answer
        areaString = f'{math.pi * (givenRadius ** 2):.2f}'
        self.CircleAnswer.setText(areaString)

        # clearing inputs
        self.RadiusInput.clear()

    def calcRectangle(self):
        """
        Method for checking valid input, calculates the area of a rectangle, displays said area, then clears the input.
        """
        try:
            givenLength = int(self.LengthInput.toPlainText())
            givenWidth = int(self.WidthInput.toPlainText())
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Must be an integer greater than 0")
            msg.setWindowTitle("Bro, come on now...")
            msg.exec_()

        # formatting and displaying answer
        areaString = f'{givenLength * givenWidth:.2f}'
        self.RectangleAnswer.setText(areaString)

        # clearing inputs
        self.LengthInput.clear()
        self.WidthInput.clear()

    def calcSquare(self):
        """
        Method for checking valid input, calculates the area of a square, displays said area, then clears the input.
        """
        try:
            givenSide = int(self.SideInput.toPlainText())
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Must be an integer greater than 0")
            msg.setWindowTitle("Bro, come on now...")
            msg.exec_()

        # formatting and displaying answer
        areaString = f'{givenSide ** 2:.2f}'
        self.SquareAnswer.setText(areaString)

        # clearing inputs
        self.SideInput.clear()

    def calcTriangle(self):
        """
        Method for checking valid input, calculates the area of a triangle, displays said area, then clears the input.
        """
        try:
            givenBase = int(self.BaseInput.toPlainText())
            givenHeight = int(self.HeightInput.toPlainText())
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Must be an integer greater than 0")
            msg.setWindowTitle("Bro, come on now...")
            msg.exec_()

        # formatting and displaying answer
        areaString = f'{0.5 * givenBase * givenHeight:.2f}'
        self.TriangleAnswer.setText(areaString)

        # clearing inputs
        self.BaseInput.clear()
        self.HeightInput.clear()
