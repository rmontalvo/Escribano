#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, markdown2
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import QtWebKit
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from about import aboutWindow

VERSION = "0.2"
NESTILO = 'styles/default.css' 

class Escribano(QtGui.QWidget):
	
	def __init__(self):
		super(Escribano, self).__init__()
		self.initUI()

	def initUI(self):

		self.setGeometry(1, 1, 1300, 700)
		self.setWindowTitle("Escribano %s" % VERSION)
		self.setWindowIcon(QtGui.QIcon('icons/escribano.png'))
		self.textEdit = QtGui.QTextEdit(self)
		QtCore.QObject.connect(self.textEdit,
			QtCore.SIGNAL('textChanged()'), self.onTextChanged)
		#self.setMinimumWidth(1000)
		#self.setMinimumHeight(1000)
		self.myMenuBar = QtGui.QMenuBar(self)		
		
		fileMenu = self.myMenuBar.addMenu('File')
		toolMenu = self.myMenuBar.addMenu('Tools')
		helpMenu = self.myMenuBar.addMenu('Help')
	
		newfile = QtGui.QAction('New File', self)
		newfile.setShortcut('Ctrl+N')
		newfile.setStatusTip('New file')
		newfile.triggered.connect(self.newFile)
		
		openfile = QtGui.QAction('Open File', self)        
		openfile.setShortcut('Ctrl+O')        
		openfile.setStatusTip('Open file')        
		openfile.triggered.connect(self.openFile)

		saveFile = QtGui.QAction('Save File', self)        
		saveFile.setShortcut('Ctrl+S')        
		saveFile.setStatusTip('Save file')        
		saveFile.triggered.connect(self.saveFile)

		exportPDF = QtGui.QAction('Export as PDF', self)        
		exportPDF.triggered.connect(self.exportPDF)
		
		quitAction = QtGui.QAction('Quit', self)        
		quitAction.setShortcut('Ctrl+Q')        
		quitAction.triggered.connect(self.closeEvent)
		
		landAction = QtGui.QAction('Orientacion ', self)        
		landAction.triggered.connect(self.paintEvent)
		
		helpAction = QtGui.QAction('Help', self)        
		helpAction.setShortcut('F1')        
		helpAction.triggered.connect(self.helpFuc)
		
		aboutAction = QtGui.QAction('About', self)        
		aboutAction.triggered.connect(self.aboutFuc)
		
		themes = toolMenu.addMenu("Styles")
		estilo1Action = QtGui.QAction('Theme gray', self)
		estilo1Action.setShortcut("Ctrl+X") 
		estilo1Action.setStatusTip("Buscar")
		estilo1Action.triggered.connect(self.estilo1)
		themes.addAction(estilo1Action)
		
		estilo2Action = QtGui.QAction('Theme blue', self)
		estilo2Action.setShortcut("Ctrl+X")
		estilo2Action.setStatusTip("theme blue")
		estilo2Action.triggered.connect(self.estilo2)
		themes.addAction(estilo2Action)
		
		estilo3Action = QtGui.QAction('Theme green', self)
		estilo3Action.setShortcut("Ctrl+X")
		estilo3Action.setStatusTip("theme green")
		estilo3Action.triggered.connect(self.estilo3)
		themes.addAction(estilo3Action)
		
		fileMenu.addAction(newfile)
		fileMenu.addAction(openfile)
		fileMenu.addAction(saveFile)
		fileMenu.addAction(exportPDF)
		fileMenu.addAction(quitAction)
		helpMenu.addAction(helpAction)
		helpMenu.addAction(aboutAction)
		
		self.webView = QtWebKit.QWebView(self)
		self.webView.load(QtCore.QUrl('front.html'))
		
		self.split = QtGui.QSplitter(QtCore.Qt.Horizontal, self)
		
		self.split.addWidget(self.textEdit)
		self.split.addWidget(self.webView)
		self.split.setSizes([1, 75])
		self.hbox = QtGui.QHBoxLayout(self)
		self.hbox.addWidget(self.split)

		fg = self.frameGeometry()
		fg.moveCenter(QtGui.QDesktopWidget().availableGeometry().center())
		self.move(fg.topLeft())
		self.show()
		
		self.setStyleSheet("background-color:  #e0e0d1;")
		self.webView.setStyleSheet("background-color:  #ffffff;")
		self.textEdit.setStyleSheet("background-color:  #ffffff;")


	def newFile(self):

		self.textEdit.clear()


	def openFile(self):

		filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '/home')
		f = open(filename, 'r')
		fileData = f.read()
		self.textEdit.setText(fileData)
		f.close()

		
	def saveFile(self):
		
		filename = QtGui.QFileDialog.getSaveFileName(self, "Save file", "", ".conf")
		name =  filename + '.md'
		f = open(name,'w')
		f.write(self.textEdit.toPlainText())
		f.close()	


	def exportPDF(self):		
	
		filename = QtGui.QFileDialog.getSaveFileName(self, "Save file", "", ".conf")
		printer = QPrinter()
		printer.setPageSize(QPrinter.A4)
		printer.setOutputFormat(QPrinter.PdfFormat)
		printer.setOutputFileName(filename+".pdf")
		self.webView.print_(printer)


	def onTextChanged(self):
		print(self.textEdit.toPlainText())	
		t = str(self.textEdit.toPlainText())
		html = markdown2.markdown(str(self.textEdit.toPlainText()))		
		fil = open('index.html','w')
		fil.write('<!DOCTYPE HTML>\n')
		fil.write('<html>\n')
		fil.write('\t<head>\n')
		fil.write('\t\t<title>Escribano </title>\n')
		fil.write('\t\t<link href="'+NESTILO+'" rel="stylesheet" type="text/css">\n')
		fil.write('\t</head>\n')
		fil.write('\t<body>\n')
		fil.write(html)
		fil.write('\n\t</body>\n')
		fil.write('</html>\n')
		fil.close()
		self.webView.load(QtCore.QUrl("index.html"))


	def helpFuc(self):		
		self.webView.load(QtCore.QUrl("https://es.wikipedia.org/wiki/Markdown"))
				
	def aboutFuc(self):		
		aboutWin = aboutWindow().exec_()
		
	def closeEvent(self, event):
		reply = QtGui.QMessageBox.question(self, 'Quit Escribano', "Are you sure to quit Escribano?", 
			QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
		if reply == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
		
		
	def estilo1(self):
		
		global NESTILO
		NESTILO = "styles/gray.css" 
		self.onTextChanged()


	def estilo2(self):

		global NESTILO
		NESTILO = "styles/blue.css"
		self.onTextChanged()

		
	def estilo3(self):

		global NESTILO
		NESTILO = "styles/c.css"
		self.onTextChanged()
        
def main():
	app = QtGui.QApplication(sys.argv)
	ex = Escribano()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
