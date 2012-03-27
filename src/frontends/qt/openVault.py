'''
Created on Mar 23, 2012

@author: nick
'''
from PyQt4 import uic, QtCore, QtGui
import os
import manage
import vault, config

class OpenVault(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        path = os.path.dirname(__file__)
        self.ui = uic.loadUi(os.path.join(path, 'interfaces', 'open.ui'), self)
        
        self.config = config.Config()
        
        icon = QtGui.QIcon(os.path.join(os.path.dirname(self.config.get_basescript()), 'resources', 'loxodo-icon.png'))
        self.setWindowIcon(icon)
        self.setWindowTitle("Loxodo - Open Vault")
        
        self.connect(self.btnBrowse, QtCore.SIGNAL('clicked()'), self.browse)
        self.connect(self.btnNew, QtCore.SIGNAL('clicked()'), self.newVault)
        self.connect(self.btnOpen, QtCore.SIGNAL('clicked()'), self.openVault)
        
        if len(self.config.recentvaults) > 0:
            for vault in self.config.recentvaults:
                self.cbVault.addItem(vault)
        
    def newVault(self):
        filename = QtGui.QFileDialog.getSaveFileName(self.ui, caption=QtCore.QString("Select Password File"), filter=QtCore.QString("PSafe3 (*.psafe3);;All Files (*)"))
        filename = str(filename)
        
        self.cbVault.addItem(filename)
        self.config.recentvaults.append(filename)
    
    def openVault(self):
        filename = str(self.cbVault.currentText())
        password = str(self.txtPassword.text()).encode('latin1', 'replace')
        
        if filename is not None or filename != '':
            try:
                manager = manage.Manage(filename, password)
                manager.show()
                self.close()
            except vault.Vault.BadPasswordError:
                box = QtGui.QMessageBox(self)
                box.setText(QtCore.QString("Vault password is wrong."))
                box.show()
        else:
            box = QtGui.QMessageBox(self)
            box.setText(QtCore.QString("You must provide a vault file to open."))
            box.show()
    
    def browse(self):
        filename = QtGui.QFileDialog.getOpenFileName(self.ui, caption=QtCore.QString("Select Password File"), filter=QtCore.QString("PSafe3 (*.psafe3);;All Files (*)"))
        filename = str(filename)
        
        self.cbVault.addItem(filename)
        self.config.recentvaults.append(filename)