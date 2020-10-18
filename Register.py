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
from pyisemail import is_email
from config import firebase

auth = firebase.auth()
user = None


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"Resources\Ui\Register.ui", self)
        self.center()
        flags = QtCore.Qt.WindowFlags(
            QtCore.Qt.FramelessWindowHint)
        #
        # DEF imports
        #
        self.call_childs()
        self.set_images()
        self.child_functions()

        # DEF imports end here

        self.setWindowFlags(flags)
        self.oldPos = self.pos()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def call_childs(self):
        self.sign_up = self.sign_up
        self.email = self.email_edit
        self.password = self.password_edit
        self.login_bt = self.login_here
        self.password_repeat = self.password_edit_2
        self.min1 = self.minimize
        self.close2 = self.close1

    def child_functions(self):
        self.login_bt.clicked.connect(self.credentials)
        self.sign_up.clicked.connect(self.sign_in_click)
        self.min1.clicked.connect(self.get_mini)
        self.close2.clicked.connect(self.close_window)

    def set_images(self):
        self.min1.setIcon(QtGui.QIcon(
            r'Resources\Ui\Images\minimize-svgrepo-com 1.png'))
        self.min1.setIconSize(QtCore.QSize(66, 66))
        self.close2.setIcon(QtGui.QIcon(r'Resources\Ui\Images\close.png'))
        self.close2.setIconSize(QtCore.QSize(43, 43))

    # child_functions Defs
    def credentials(self):
        email_check_test = str(self.email.text())

        bool_result_with_dns = is_email(email_check_test, check_dns=True)
        #print(bool_result_with_dns)
        if bool_result_with_dns is not True:
            #print("LEL")
            msg = QMessageBox()
            msg.setWindowTitle("Error In Email")
            msg.setText("Wrong Email Or Dns Is Not Valid")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
        else:
            passw = str(self.password.text())
            passw1 = str(self.password_repeat.text())
            if passw == passw1:
                #print("Reache Here 1")
                try:
                    user = auth.create_user_with_email_and_password(
                    self.email.text(), self.password.text())
                except HTTPError as e:
                    logging.basicConfig(filename='error.log', filemode='w', format='%(name)s - %(asctime)s - %(levelname)s - %(message)s')
                    logging.error(e)
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setInformativeText("This Email Is Already Registered")
                    msg.setText("For More information please see The log file")
                    msg.setIcon(QMessageBox.Critical)
                    x = msg.exec_()
                if user:
                    status = False
                    auth.send_email_verification(user['idToken'])
                    status = True
                    try:
                        if status is True:
                            msg = QMessageBox()
                            msg.setWindowTitle("Registering Done")
                            msg.setText("Please Check Your Email Account For Confirming Email Registration")
                            msg.setIcon(QMessageBox.Warning)
                            x = msg.exec_()
                    except Exception as e:
                        logging.basicConfig(filename='error.log', filemode='w', format='%(name)s - %(asctime)s - %(levelname)s - %(message)s')
                        logging.error(e)
                        msg = QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setInformativeText("Please CHeck The Logs For More Information")
                        msg.setText("An Unexpected Error occurred!")
                        msg.setIcon(QMessageBox.Critical)
                        x = msg.exec_()
                else:
                    #print("Reache Here 3")
                    logging.basicConfig(filename='error.log', filemode='w', format='%(name)s - %(asctime)s - %(levelname)s - %(message)s')
                    logging.error(e)
                    msg = QMessageBox()
                    msg.setWindowTitle("Error While Registering")
                    msg.setText("Please Check Your Connection Or The Password Is Not Same!")
                    msg.setIcon(QMessageBox.Critical)
                    x = msg.exec_()

    def get_mini(self):
        self.showMinimized()

    def close_window(self):
        self.close()

    def sign_in_click(self):
        self.close()
        os.system('Login.py')

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    # child_functions Defs end here


app = QApplication(sys.argv)
window = UI()
app.exec_()
#END HERE