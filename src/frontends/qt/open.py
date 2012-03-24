'''
Created on Mar 23, 2012

@author: nick
'''
from PyQt4 import uic, QtCore, QtGui
import os
import manage

class Open(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        path = os.path.dirname(__file__)
        self.ui = uic.loadUi(os.path.join(path, 'interfaces', 'open.ui'), self)
        
        self.connect(self.btnBrowse, QtCore.SIGNAL('clicked()'), self.browse)
        self.connect(self.btnNew, QtCore.SIGNAL('clicked()'), self.newVault)
        self.connect(self.btnOpen, QtCore.SIGNAL('clicked()'), self.openVault)
        
    def newVault(self):
        filename = QtGui.QFileDialog.getSaveFileName(self.ui, caption=QtCore.QString("Select Password File"), filter=QtCore.QString("PSafe3 (*.psafe3);;All Files (*.*)"))
        self.cbVault.addItem(filename)
    
    def openVault(self):
        filename = self.cbVault.currentText()
        password = self.txtPassword.text()
        
        if not filename.isEmpty():
            manager = manage.Manage(filename, password)
            manager.show()
            self.close()
        else:
            box = QtGui.QMessageBox(self)
            box.setText(QtCore.QString("You must provide a vault file to open."))
            box.show()
        
    def reShow(self):
        print "Show"
    
    def browse(self):
        filename = QtGui.QFileDialog.getOpenFileName(self.ui, caption=QtCore.QString("Select Password File"), filter=QtCore.QString("PSafe3 (*.psafe3);;All Files (*.*)"))
        self.cbVault.addItem(filename)