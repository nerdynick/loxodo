'''
Created on Mar 23, 2012

@author: nick
'''
from PyQt4 import uic, QtCore, QtGui
import os

class Manage(QtGui.QMainWindow):
    def __init__(self, filename, password):
        QtGui.QMainWindow.__init__(self)
        
        path = os.path.dirname(__file__)
        self.ui = uic.loadUi(os.path.join(path, 'interfaces', 'manage.ui'), self)