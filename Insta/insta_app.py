#!/usr/bin/python

"""
Python GUI Project 1: Insta_App

Version: 1.0.0

07/29/20

Programmer: Edward Moon

"""

#####################################################
# This is the Insta_App written in Python
#   A simple GUI desktop app that allows users to
#   download instagram profile pictures
#
#####################################################


# Import
import sys
import instaloader
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QApplication, QWidget, QTextEdit, QAction, QFileDialog,
                             QMainWindow, QPushButton, QLineEdit, QInputDialog, QLineEdit, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from pathlib import Path


#class
class mainDialog(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.btn = QPushButton('Instagram Dialog', self)
        self.btn.move(150, 20)
        self.btn.clicked.connect(self.showDialog)

        self.palette = self.palette()
        self.palette.setColor(QPalette.Window, QColor(3, 18, 14))

        self.palette.setColor(QPalette.Button, QColor('blue'))
        self.setPalette(self.palette)

        self.setGeometry(150, 150, 400, 150)
        self.setWindowTitle('Instagram Profile Pic Download')
        self.setWindowIcon(QIcon('dl_mrX_icon.ico'))
        self.show()

    def showDialog(self):

        text, ok = QInputDialog.getText(self, "Instagram Profile Pic Download",'Enter username')
        mod = instaloader.Instaloader()
        mod.download_profile(text, profile_pic_only=True)

        if ok:
            self.le.setText(str(text))

    def keyPressEvent(self, e):

        #If user hits 'esc' key application closes
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    mDl = mainDialog()
    sys.exit(app.exec_())
