# -*- coding: utf-8 -*-

import sys
from PySide import QtGui
from MainWindow import MainWindow
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()