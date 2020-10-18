from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import QtCore
import sys
import logging
import os
import time
from create_keys import Credentials
from config import firebase

auth = firebase.auth()
user = None


class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()
		uic.loadUi(r"Resources\Ui\Login.ui", self)

		self.center()
		flags = QtCore.Qt.WindowFlags(
			QtCore.Qt.FramelessWindowHint)

		# DEF imports
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
		self.forget1 = self.pass_forgot
		self.sign_up = self.sign_up_ui
		self.email = self.email_edit
		self.password = self.password_edit
		self.login_bt = self.login_here
		self.min1 = self.minimize
		self.close2 = self.close1

	def child_functions(self):
		self.forget1.clicked.connect(self.pass_forgot1)
		self.login_bt.clicked.connect(self.credentials)
		self.sign_up.clicked.connect(self.sign_in_click)
		self.min1.clicked.connect(self.get_mini)
		self.close2.clicked.connect(self.close_window)

	def set_images(self):
		self.min1.setIcon(QtGui.QIcon(
			r'Resources\Ui\Images\minimize-svgrepo-com 1.png'))
		self.min1.setIconSize(QtCore.QSize(66, 66))
		self.close2.setIcon(QtGui.QIcon(
			r'Resources\Ui\Images\close.png'))
		self.close2.setIconSize(QtCore.QSize(100, 100))

	# child_functions Defs
	def pass_forgot1(self):
		#email1
		auth.send_password_reset_email(self.email.text())

	def credentials(self):
		global user
		try:
			user = auth.sign_in_with_email_and_password(
				self.email.text(), self.password.text())
			if user:
				creds = Credentials()
				creds.username = self.email.text()
				creds.password = self.password.text()
				creds.create_cred()
			else:
				print("Error")
		except Exception as e:
			logging.basicConfig(filename='error.log', filemode='w', format=' %(asctime)s - %(message)s')
			logging.error(e)
			msg = QMessageBox()
			msg.setWindowTitle("Error In Email")
			msg.setText("Please Check Your Connection Or The Password Is Incorrect")
			msg.setIcon(QMessageBox.Critical)
			x = msg.exec_()
			

	def get_mini(self):
		self.showMinimized()

	def close_window(self):
		self.close()

	def sign_in_click(self):
		self.close()
		os.system('Register.py')

	def mousePressEvent(self, event):
		self.oldPos = event.globalPos()

	def mouseMoveEvent(self, event):
		delta = QPoint(event.globalPos() - self.oldPos)
		# print(delta)
		self.move(self.x() + delta.x(), self.y() + delta.y())
		self.oldPos = event.globalPos()

	# child_functions Defs end here


app = QApplication(sys.argv)
window = UI()
app.exec_()
