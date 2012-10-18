# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

import socket
from PySide import QtCore, QtGui
from Ui_MainWindow import Ui_MainWindow


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.center()
    
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
        
    @QtCore.Slot()
    def on_getIPBtn_clicked(self):
        """
        get ip address by domain name, using socket
        """
        domainName = self.domainInput.text()
        ipAddress = socket.gethostbyname(domainName)
        self.ipInput.setText(ipAddress)