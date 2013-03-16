# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fish.ui'
#
# Created: Wed Mar 13 19:55:32 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(799, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidget_filelist = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget_filelist.setGeometry(QtCore.QRect(240, 0, 551, 321))
        self.tableWidget_filelist.setMaximumSize(QtCore.QSize(571, 16777215))
        self.tableWidget_filelist.setColumnCount(3)
        self.tableWidget_filelist.setObjectName(_fromUtf8("tableWidget_filelist"))
        self.tableWidget_filelist.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_filelist.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_filelist.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_filelist.setHorizontalHeaderItem(2, item)
        self.listWidget_users = QtGui.QListWidget(self.centralwidget)
        self.listWidget_users.setGeometry(QtCore.QRect(10, 0, 221, 321))
        self.listWidget_users.setObjectName(_fromUtf8("listWidget_users"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 329, 781, 201))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.listWidget = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.horizontalLayout.addWidget(self.listWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionDiscover = QtGui.QAction(MainWindow)
        self.actionDiscover.setCheckable(True)
        self.actionDiscover.setObjectName(_fromUtf8("actionDiscover"))
        self.actionShare = QtGui.QAction(MainWindow)
        self.actionShare.setObjectName(_fromUtf8("actionShare"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionSettings_2 = QtGui.QAction(MainWindow)
        self.actionSettings_2.setObjectName(_fromUtf8("actionSettings_2"))
        self.toolBar.addAction(self.actionDiscover)
        self.toolBar.addAction(self.actionShare)
        self.toolBar.addAction(self.actionSettings_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.tableWidget_filelist.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Filename", None))
        item = self.tableWidget_filelist.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Size", None))
        item = self.tableWidget_filelist.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Hash", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionDiscover.setText(_translate("MainWindow", "Discover", None))
        self.actionShare.setText(_translate("MainWindow", "Share", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionSettings_2.setText(_translate("MainWindow", "Settings", None))

