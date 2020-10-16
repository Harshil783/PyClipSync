from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import QtCore
import sys
import os
import time
import logging


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"Resources\Ui\Main Screen.ui", self)
        self.center()
        flags = QtCore.Qt.WindowFlags(
            QtCore.Qt.FramelessWindowHint
        )
        #
        # DEF imports
        #
        self.call_childs()
        self.set_images()
        self.child_functions()

        # DEF imports end here

        self.setWindowFlags(flags)
        self.oldpos = self.pos()
        self.show()
    # PUSH BUTTON FUNCTIONS

    def get_mini(self):
        self.showMinimized()

    def close_window(self):
        self.close()

    def call_childs(self):
        self.min1 = self.minimize
        self.close2 = self.close1

    def set_images(self):
        self.min1.setIconSize(QtCore.QSize(50, 50))
        self.min1.setIcon(QtGui.QIcon(
            r'Resources\Ui\Images\minimize-svgrepo-com 1 2.png'))
        self.close2.setIconSize(QtCore.QSize(50, 50))
        self.close2.setIcon(QtGui.QIcon(r'Resources\Ui\Images\Group.png'))

    def child_functions(self):
        self.min1.clicked.connect(self.get_mini)
        self.close2.clicked.connect(self.close_window)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


app = QApplication(sys.argv)
window = UI()
app.exec_()
