#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2022年3月21日
# module	: UIModule.TimeWindowMgr
#===================================================
from UIModule import UITime
from PyQt5 import QtWidgets, QtCore, QtGui
import os 

class TimeWindow(UITime.Ui_Dialog, QtWidgets.QMainWindow):
    def __init__(self, parent_window):
        super(TimeWindow, self).__init__()
        self.setupUi(self)
        self.setupUiManual()
        self.setupSignalSlot()
        
        self.parent_window = parent_window
            
    def setupUiManual(self):
        pass

    def setupSignalSlot(self):
        self.buttonBox.accepted.connect(self.doOk)
        self.buttonBox.rejected.connect(self.doCancel)
    
    def doOk(self):
        dt = self.dateTimeEdit.dateTime()
        strBuffer = dt.toString("yyyy-MM-dd hh:mm:ss")
        p = os.system('docker exec game date -s "%s"' % strBuffer)
        if p:
            QtWidgets.QMessageBox.critical(self, "critical", "change time failed")
        else:
            self.parent_window.refreshNowDateTime()
            QtWidgets.QMessageBox.information(self, "info", "change time successfully")
            self.close()
        
    def doCancel(self):
        self.close()
