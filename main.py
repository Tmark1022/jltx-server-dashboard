#-*- coding:UTF-8 -*-
#===================================================
# author    : Tmark
# date         : 2022年3月21日
# module    : main
#===================================================
import sys
from PyQt5 import QtWidgets
import MainWindowMgr
import os
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

APP_NAME = "jltx-dashboard"
CURRENT_PWD = os.getcwd()
ROOT_POS = CURRENT_PWD.rfind(APP_NAME)
ROOT_DIR = CURRENT_PWD[:ROOT_POS - 1] if ROOT_POS >= 0 else ""
LOGIC_DIR = ROOT_DIR + os.sep + "logic"
ENGINE_DIR = ROOT_DIR + os.sep + "engine"
GIT_BASH_PATH = "C:\Program Files\Git\git-bash.exe"

def PrintMarco():
    print("----------------------marco------------------------")
    print("app name       :", APP_NAME)
    print("cur dir        :", CURRENT_PWD)
    print("logic dir      :", LOGIC_DIR)
    print("engine dir     :", ENGINE_DIR)
    print("---------------------------------------------------\n")

def CheckSystem(mainWindowObj):
    #if ROOT_POS < 0:
    #    QtWidgets.QMessageBox.critical(mainWindowObj, "critical", "path config invalid")
    #    sys.exit(-1)
    
    p = os.system("docker version")
    if p:
        QtWidgets.QMessageBox.critical(mainWindowObj, "critical", "docker engine not running")
        sys.exit(-1)

def dockerMachinePkillNtpd():
    p = os.system('docker-machine.exe ssh default "sudo pkill ntpd"')
    if p:
        print("--- ntpd already killed")
    else:
        print("--- pkill ntpd successfully")
            

if __name__ == "__main__":
    PrintMarco()
    app = QtWidgets.QApplication(sys.argv)
    mainWindowObj = MainWindowMgr.MainWindow()
    mainWindowObj.setFixedSize(600, 820)
    mainWindowObj.show()
    CheckSystem(mainWindowObj)
    dockerMachinePkillNtpd()
    
    p = os.system("docker inspect game")
    if p:
        QtWidgets.QMessageBox.information(mainWindowObj, "info", "检测到没有启动相关容器， 点击OK开始启动流程（第一次启动需要下载相应镜像， 请耐心等待）")
        res = os.system("docker run --rm --name game -it -d -v /c/Users/jltx:/code -p 9010:9010 --privileged tmark1022/ubuntu")
        if res:
            QtWidgets.QMessageBox.critical(mainWindowObj, "critical", "启动失败， 散了吧")
            sys.exit(-1)
        else:
            QtWidgets.QMessageBox.information(mainWindowObj, "info", "启动成功， 可以开始愉快地玩耍")
            
    mainWindowObj.refreshServerStatusFunc()
    mainWindowObj.refreshNowDateTime()
    sys.exit(app.exec_())