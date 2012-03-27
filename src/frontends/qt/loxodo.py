'''
Created on Mar 23, 2012

@author: nick
'''
from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
import openVault

def launch():
    app = QtGui.QApplication(sys.argv)
    window = openVault.OpenVault()
    window.show()
    app.connect(app, QtCore.SIGNAL("lastWindowClosed()"), app, QtCore.SLOT("quit()"))
    sys.exit(app.exec_())
    
launch()