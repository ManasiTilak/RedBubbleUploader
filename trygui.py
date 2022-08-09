from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys

def clicked():
    print("I was clicked")

def dialog():
    app = QApplication(sys.argv)
    win = QMainWindow()
    a = uic.loadUi("betterdialog.ui")
    b1 = a.findChild(QPushButton, "BrowseImg")
    b1.clicked.connect(clicked)
    win.show()
    #system waits for you to click close icon and closes the window
    sys.exit(app.exec())

# def window():
#     app = QApplication(sys.argv)
#     win = QMainWindow()
#     # win.setGeometry(xpos, ypos, width, height)
#     win.setGeometry(200,200,500,500)
#     win.setWindowTitle("GUI PYQT5 TRY")

#     #Making a label
#     label = QtWidgets.QLabel(win)
#     label.setText("Try a label")
#     label.move(50,50)

#     #Making a button
#     b1 = QtWidgets.QPushButton(win)
#     b1.setText("Click Me")
#     b1.clicked.connect(clicked)

    
#     win.show()
#     #system waits for you to click close icon and closes the window
#     sys.exit(app.exec())

# window()
dialog()