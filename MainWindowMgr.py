#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2022年3月21日
# module	: UIModule.MainWindowMgr
#===================================================
from UIModule import UIMain
from PyQt5 import QtWidgets, QtCore, QtGui
from main import LOGIC_DIR, ENGINE_DIR, GIT_BASH_PATH
import os
import time
import socket
import TimeWindowMgr

class MainWindow(UIMain.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setupUiManual()
        self.setupSignalSlot()
        
        self.tailPath = ENGINE_DIR + os.sep + "tail.exe"
        self.netdLog = ENGINE_DIR + os.sep + "netd.log"
        self.userLog = ENGINE_DIR + os.sep + "gamed_user.log"
        self.cmdPath = GIT_BASH_PATH if os.path.isfile(GIT_BASH_PATH) else ""
        
        self.status = False
        
    def setupUiManual(self):
        self.timeWindowObj = TimeWindowMgr.TimeWindow(self)

    def setupSignalSlot(self):
        self.serverStatus.clicked.connect(self.refreshServerStatusFunc)
        self.startServer.clicked.connect(self.startServerFunc)
        self.stopServer.clicked.connect(self.stopServerFunc)
        self.netdLog.clicked.connect(self.tailNetdLog)
        self.userLog.clicked.connect(self.tailUserLog)
        self.actionip_addr.triggered.connect(self.actionIPAddr)
        self.actionAbout.triggered.connect(self.actionAboutFunc)
        self.actionPron.triggered.connect(self.actionPronFunc)
        self.nowDateTime.clicked.connect(self.refreshNowDateTime)
        self.toOneMinute.clicked.connect(self.toOneMinuteFunc)
        self.toTenMinutes.clicked.connect(self.toTenMinutesFunc)
        self.toOneHour.clicked.connect(self.toOneHourFunc)
        self.toCrossDay.clicked.connect(self.toCrossDayFunc)
        self.toSpecificDateTime.clicked.connect(self.toSpecificDateTimeFunc)
        
    def refreshServerStatusFunc(self):
        p = os.popen('docker exec game bash -c "ps -u root | grep -E [n]etd | wc -l"')
        retStr = p.read()
        retStatus = p.close()
        if retStatus is None and 1 == int(retStr):
            self.labelServerStatus.setStyleSheet("font: 75 18pt \"Courier New\";\n"
"color: rgb(0, 255, 0);")
            self.labelServerStatus.setText("Running")
            self.status = True
        else:
            self.labelServerStatus.setStyleSheet("font: 75 18pt \"Courier New\";\n"
"color: rgb(255, 0, 0);")
            self.labelServerStatus.setText("Exited")
            self.status = False
            
    def startServerFunc(self):
        self.refreshServerStatusFunc()
        if self.status:
            QtWidgets.QMessageBox.information(self, "info", "already running")
            return 
        p = os.system('docker exec game bash -c "cd /code/engine && bash start.sh"')
        self.refreshServerStatusFunc()
        if p:
            QtWidgets.QMessageBox.information(self, "info", "start server failed, something wrong happened")
        else:
            QtWidgets.QMessageBox.information(self, "info", "start server successfully")
    
    def stopServerFunc(self):
        self.refreshServerStatusFunc()
        if not self.status:
            QtWidgets.QMessageBox.information(self, "info", "already exited")
            return
        p = os.system('docker exec game bash -c "cd /code/engine && bash stop.sh"')
        self.refreshServerStatusFunc()
        if p:
            QtWidgets.QMessageBox.information(self, "info", "stop server failed, something wrong happened")
        else:
            # 鉴于docker 容器的配置较差， 关进程时可能要存盘很久， 故需要定时查看剩余进程数量， 以准确提示关服完成
            for _ in range(60):
                p2 = os.popen('docker exec game bash -c "ps -u root | grep -E [c]oc | wc -l"')
                retStr = p2.read()
                retStatus = p2.close()
                print("code : %s, remain running process : %s" % (retStatus, int(retStr)))
                if retStatus is None and 0 == int(retStr):
                    break
                time.sleep(1)
            QtWidgets.QMessageBox.information(self, "info", "stop server successfully")
    
    def _transfer_path_win2unix(self, path):
        path = path.replace(":", "")
        path = path.replace("\\", "/")
        path = "/%s" % path
        return path
    
    def tailLog(self, logFile):
        if os.path.isfile(logFile):
            if self.cmdPath:
                # git-bash
                cmdStr = 'start "Git Bash Open Tail" "%s" -c "%s -f %s"' % (self.cmdPath, self._transfer_path_win2unix(self.tailPath), self._transfer_path_win2unix(logFile))
            else:
                cmdStr = "start %s -f %s" % (self.tailPath, logFile)
            print(cmdStr)
            os.system(cmdStr)
        else:
            QtWidgets.QMessageBox.information(self, "info", "log file not exists")
            
    def tailNetdLog(self):
        self.tailLog(self.netdLog)
    
    def tailUserLog(self):
        self.tailLog(self.userLog)
    
    def actionIPAddr(self):
        hostname = socket.gethostname()
        localip = socket.gethostbyname(hostname)
        p = os.popen("docker-machine ip default")
        vmip = p.read()  
        QtWidgets.QMessageBox.information(self, "info", "local host ip : %s\ndocker engine host ip : %s" % (localip, vmip))
    
    def actionAboutFunc(self):
        QtWidgets.QMessageBox.information(self, "info", "fxxk the world!")
        
    def actionPronFunc(self):
        QtWidgets.QMessageBox.warning(self, "FBI WARNING", "大水逼，你在想啥")
        QtGui.QDesktopServices.openUrl(QtCore.QUrl("http://hk.tmark.top:8912/"))
        
    def refreshNowDateTime(self):
        p = os.popen('docker exec game date "+%Y-%m-%d %H:%M:%S"')
        retStr = p.read()
        retStatus = p.close()
        retStr = retStr.replace('\n', '').replace('\r', '')     # 去掉換行
        if retStatus is None:
            self.nowTimeLabel.setText(retStr)
        else:
            self.nowTimeLabel.setText("1990-01-01 00:00:00")
        
    def _change_time(self, dateStr):
        p = os.system('docker exec game date -s "%s"' % dateStr)
        if p:
            QtWidgets.QMessageBox.critical(self, "critical", "change time failed")
        else:
            QtWidgets.QMessageBox.information(self, "info", "change time successfully")
        self.refreshNowDateTime()
                
    def toOneMinuteFunc(self):
        self._change_time("1 minute")
        
    def toTenMinutesFunc(self):
        self._change_time("10 minute")
        
    def toOneHourFunc(self):
        self._change_time("1 hour")
        
    def toCrossDayFunc(self):
        self._change_time("23:59:00")
        
    def toSpecificDateTimeFunc(self):
        sstime = QtCore.QDateTime.fromString(self.nowTimeLabel.text(), "yyyy-MM-dd hh:mm:ss")
        self.timeWindowObj.dateTimeEdit.setDateTime(sstime)
        self.timeWindowObj.show()
        