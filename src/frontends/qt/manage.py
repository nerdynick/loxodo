'''
Created on Mar 23, 2012

@author: nick
'''
from PyQt4 import uic, QtCore, QtGui
import os
import vault, config

class Manage(QtGui.QMainWindow):
    def __init__(self, filename, password):
        QtGui.QMainWindow.__init__(self)
        path = os.path.dirname(__file__)
        self.ui = uic.loadUi(os.path.join(path, 'interfaces', 'manage.ui'), self)
        
        self.config = config.config
        
        icon = QtGui.QIcon(os.path.join(os.path.dirname(self.config.get_basescript()), 'resources', 'loxodo-icon.png'))
        self.setWindowIcon(icon)
        self.setWindowTitle("Loxodo - Vault "+ filename)
        
        self.vault = vault.Vault(password, filename=filename)
        
        groups = dict()
        for record in self.vault.records:
            if not groups.has_key(record.group):
                groups[record.group] = []
                
            groups[record.group].append(record)
            
        self.groups = []
        for group, records in groups.iteritems():
            self.groups.append(Manage.Group(self.lsGroups, group, records))
            
        self.connect(self.lsGroups, QtCore.SIGNAL("currentItemChanged(QListWidgetItem*, QListWidgetItem*)"), self.changeGroup)
        self.connect(self.tbPasswords, QtCore.SIGNAL("itemDoubleClicked(QTableWidgetItem*)"), self.doubleClick)
        
    def changeGroup(self, new, prev):
        self.tbPasswords.setRowCount(0)
        self.tbPasswords.setRowCount(len(new.records))
        self.tbPasswords.setSortingEnabled(False)
        
        row = 0
        for record in new.records:
            title = Manage.TableWidgetItem(record.title, record)
            user = Manage.TableWidgetItem(record.user, record)
            url = Manage.TableWidgetItem(record.url, record)
            notes = Manage.TableWidgetItem(record.notes, record)
            self.tbPasswords.setItem(row, 0, title)
            self.tbPasswords.setItem(row, 1, user)
            self.tbPasswords.setItem(row, 2, url)
            self.tbPasswords.setItem(row, 3, notes)
            row+=1
            
        self.tbPasswords.setSortingEnabled(True)
        
    def doubleClick(self, item):
        password = item.record.passwd
        QtGui.QApplication.clipboard().setText(password)
        statusbar = self.statusBar()
        statusbar.showMessage("Password copied to clipboard")
            
    class Group(QtGui.QListWidgetItem):
        def __init__(self, parent, name, records):
            QtGui.QListWidgetItem.__init__(self, QtCore.QString(name), parent)
            
            self.records = records
            
    class TableWidgetItem(QtGui.QTableWidgetItem):
        def __init__(self, value, record):
            QtGui.QTableWidgetItem.__init__(self, QtCore.QString(value))
            self.record = record