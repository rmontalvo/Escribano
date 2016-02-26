import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import QtWebKit
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

class aboutWindow(QDialog):
	
	
    def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		self.setWindowTitle("Escribano 0.2")
		self.resize(400,200)
		layout = QVBoxLayout()
		self.setLayout(layout)
		
		btnExit = QPushButton("Exit",None)
		#btnExit.resize(btnExit.sizeHint())
		
		label = QtGui.QLabel(self)
		label.setAlignment(QtCore.Qt.AlignCenter)
		label.setText('Version: 0.1\n Id. de compilacion: xxxxx:Xxxxxx\n Escribano es un procesador sencillo.')
		layout.addWidget(label)
		layout.addWidget(btnExit)
		self.connect(btnExit, SIGNAL("clicked()"), self.exit_about)
 
		self.setStyleSheet("background-color:  #d6d6c2;")
 
    def exit_about(self):
        exit()



















class helpWindow(QWidget):
	
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
	
		self.setGeometry(0, 0, 700, 700)
		self.setWindowTitle("Help")
		#self.setWindowIcon(QtGui.QIcon('iconos/escribano.png'))
		self.webView = QtWebKit.QWebView(self)
		self.webView.load(QtCore.QUrl('about:blank'))
		self.show()
	
	def exit_about(self):
		exit()


