from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
import sys
import os
from openpyxl import load_workbook
import RedbubbleUpload

wb = load_workbook("getuserdatatry.xlsx")
obj = wb['datax']


class UI(QMainWindow):

      
    def __init__(self):
        super(UI, self).__init__()

        #loading the GUI Window
        uic.loadUi("betterdialog.ui", self)

        #for the image
        self.browseImage = self.findChild(QPushButton, "BrowseImg")      
        self.labelIm = self.findChild(QLabel, "imagFolder")
        self.browseImage.clicked.connect(self.imgclicker)

        #for the excel file
        self.browseEx = self.findChild(QPushButton, "browseIxl")      
        self.labelXl = self.findChild(QLabel, "excelFile")
        self.browseEx.clicked.connect(self.xlclicker)

    def imgclicker(self):
        # self.label.setText("FInally")
        #Open file dialog. Returns a tuple
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "PNG Files (*.png);;JPG Files(*.jpg)")

        #output filename to screen

        if fname:
            self.labelIm.setText(str(fname))
            a2 = obj['A2']
            a2.value = str(fname[0])
            wb.save("getuserdatatry.xlsx")

               
            # with open("getdir.txt", "w") as f1:
            #     f1.write(str(fname[0]))

    def xlclicker(self):
        pass
        xname = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx))")
        b2 = obj['B2']
        b2.value = xname[0]
        wb.save("getuserdatatry.xlsx")
        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = UI()
    win.show()
   
    sys.exit(app.exec())
    RedbubbleUpload.performSignIn()
    