# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PySide.QtCore import Slot
from PySide.QtGui import QMainWindow, QDesktopWidget
from Ui_MainWindow import Ui_MainWindow
import Func


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class of main window.
    """
    def __init__(self, parent=None):
        """
        Constructor of main window.
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.center()
        
    def center(self, parent=None):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
    
    @Slot()
    def on_getIPBtn_clicked(self):
        domainName = self.domainInput.text()
        ipaddress = Func.getIP(domainName)
        self.ipInput.setText(ipaddress)
    
    @Slot()
    def on_atkBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
