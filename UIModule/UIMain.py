# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/QTZ/AppData/Local/Temp/mainvnubZv.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 824)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 581, 781))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(340, 20, 171, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.serverStatus = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.serverStatus.setObjectName("serverStatus")
        self.verticalLayout_3.addWidget(self.serverStatus)
        self.startServer = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.startServer.setObjectName("startServer")
        self.verticalLayout_3.addWidget(self.startServer)
        self.stopServer = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.stopServer.setObjectName("stopServer")
        self.verticalLayout_3.addWidget(self.stopServer)
        self.labelServerStatus = QtWidgets.QLabel(self.groupBox)
        self.labelServerStatus.setGeometry(QtCore.QRect(110, 50, 141, 111))
        self.labelServerStatus.setStyleSheet("font: 75 18pt \"Courier New\";\n"
"color: rgb(255, 0, 0);")
        self.labelServerStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelServerStatus.setIndent(-1)
        self.labelServerStatus.setObjectName("labelServerStatus")
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setTitle("Game Log")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(220, 20, 171, 211))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.netdLog = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.netdLog.setObjectName("netdLog")
        self.verticalLayout_4.addWidget(self.netdLog)
        self.userLog = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.userLog.setObjectName("userLog")
        self.verticalLayout_4.addWidget(self.userLog)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(340, 30, 171, 211))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.toOneMinute = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.toOneMinute.setObjectName("toOneMinute")
        self.verticalLayout_5.addWidget(self.toOneMinute)
        self.toTenMinutes = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.toTenMinutes.setObjectName("toTenMinutes")
        self.verticalLayout_5.addWidget(self.toTenMinutes)
        self.toOneHour = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.toOneHour.setObjectName("toOneHour")
        self.verticalLayout_5.addWidget(self.toOneHour)
        self.toCrossDay = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.toCrossDay.setObjectName("toCrossDay")
        self.verticalLayout_5.addWidget(self.toCrossDay)
        self.nowDateTime = QtWidgets.QPushButton(self.groupBox_3)
        self.nowDateTime.setGeometry(QtCore.QRect(90, 140, 131, 31))
        self.nowDateTime.setObjectName("nowDateTime")
        self.nowTimeLabel = QtWidgets.QLabel(self.groupBox_3)
        self.nowTimeLabel.setGeometry(QtCore.QRect(20, 60, 281, 51))
        self.nowTimeLabel.setStyleSheet("font: 75 15pt \"Courier\";\n"
"color: rgb(0, 0, 255);")
        self.nowTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nowTimeLabel.setObjectName("nowTimeLabel")
        self.toSpecificDateTime = QtWidgets.QPushButton(self.groupBox_3)
        self.toSpecificDateTime.setGeometry(QtCore.QRect(90, 190, 131, 31))
        self.toSpecificDateTime.setObjectName("toSpecificDateTime")
        self.verticalLayout.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 602, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionip_addr = QtWidgets.QAction(MainWindow)
        self.actionip_addr.setObjectName("actionip_addr")
        self.actionPron = QtWidgets.QAction(MainWindow)
        self.actionPron.setObjectName("actionPron")
        self.menuHelp.addAction(self.actionip_addr)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionPron)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "????????????????????????"))
        self.groupBox.setTitle(_translate("MainWindow", "Server Status"))
        self.serverStatus.setText(_translate("MainWindow", "refresh status"))
        self.startServer.setText(_translate("MainWindow", " start server"))
        self.stopServer.setText(_translate("MainWindow", " stop server"))
        self.labelServerStatus.setText(_translate("MainWindow", "Running"))
        self.netdLog.setText(_translate("MainWindow", "netd log"))
        self.userLog.setText(_translate("MainWindow", "user log"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Change Time"))
        self.toOneMinute.setText(_translate("MainWindow", "forward one minute"))
        self.toTenMinutes.setText(_translate("MainWindow", "forward ten minutes"))
        self.toOneHour.setText(_translate("MainWindow", "forward one hour"))
        self.toCrossDay.setText(_translate("MainWindow", "to 23:59:00"))
        self.nowDateTime.setText(_translate("MainWindow", "Now Date Time"))
        self.nowTimeLabel.setText(_translate("MainWindow", "time"))
        self.toSpecificDateTime.setText(_translate("MainWindow", "to specific date time"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About me..."))
        self.actionip_addr.setText(_translate("MainWindow", "IP Addr"))
        self.actionPron.setText(_translate("MainWindow", "Sexual Pron"))
import image_rc
