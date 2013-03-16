#!/usr/bin/python -d
import sys
from PyQt4 import QtCore, QtGui
from fish_ui import Ui_MainWindow
#import FiSH

import progress
reload(progress)

class MyForm(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_MainWindow()
    
    self.ui.setupUi(self)
    self.ui.listWidget_users.currentItemChanged.connect(self.populateTable)
    self.ui.tableWidget_filelist.itemDoubleClicked.connect(self.beginDownload)
    self.ui.tableWidget_filelist.cellClicked.connect(self.selectRow)
    #self.ui.tableWidget_filelist.setContextMenuPolicy(QtGui.QTreeWidget.CustomContextMenu)
    #self.ui.tableWidget_filelist.customContextMenuRequested.connect(self.popup)
    checklist = ["0", "1", "2"]
    for elem in checklist:
    	self.ui.listWidget_users.addItem(elem)
  def popup(self, pos):
    
    menu = QMenu()
    downAction = menu.addAction("Download")
    action = menu.exec_(self.mapToGlobal(pos))
    if action == downAction:
    	self.progress(self.ui.tableWidget_filelist.item(activeRow, 0).text())  
  def beginDownload(self):
    self.progress(self.ui.tableWidget_filelist.item(self.ui.tableWidget_filelist.currentItem().row(), 0).text())  
  
  def selectRow(self):
    activeRow =  self.ui.tableWidget_filelist.currentItem().row()
    self.ui.tableWidget_filelist.selectRow(activeRow)
    
    
  def populateTable(self):
    
    if self.ui.listWidget_users.currentItem().text()=="0":
	    lister={}
	    lister[0] = ["1", "2", "fgsdkfgsdkgfsdkjfgsdjkfgsdfsdf"]
	    lister[1] = ["4", "5", "fsdfdsjkfhkdsjfhsdlkjfhdskjf"]
	    lister[2] = ["7", "8", "assjkhdsakljdhsalkjdhsalkjd"]
    elif self.ui.listWidget_users.currentItem().text()=="1":
	    lister={}
	    lister[0] = ["9", "12", "fgsdkfgsdkgfsdkjfgsdjkfgsdfsdf"]
	    lister[1] = ["41", "15", "fsdfdsjkfhkdsjfhsdlkjfhdskjf"]
	    lister[2] = ["17", "18", "assjkhdsakljdhsalkjdhsalkjd"]
    elif self.ui.listWidget_users.currentItem().text()=="2":
	    lister={}
	    lister[0] = ["91", "121", "f111gsdkfgsdkjfgsdjkfgsdfsdf"]
	    lister[1] = ["411", "151", "fsdfdsjkffhsdlkjfhdsk111jf"]
	    lister[2] = ["171", "181", "a1111hdsakljdhsalkjdhsalkjd"]
    
    self.ui.tableWidget_filelist.setColumnCount(3)
    self.ui.tableWidget_filelist.setRowCount(3)
    for row in range(3):
	for column in range(3):
		item = QtGui.QTableWidgetItem(lister[row][column])
		
		self.ui.tableWidget_filelist.setItem(row, column, item)
  def progress(self, Name):
	  
	  item = QtGui.QListWidgetItem(self.ui.listWidget)
	  item_widget = progress.Ui_(Name)
	  item.setSizeHint(item_widget.sizeHint())
	  self.ui.listWidget.addItem(item)
	  self.ui.listWidget.setItemWidget(item,item_widget)


if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = MyForm()
  myapp.show()
  sys.exit(app.exec_())
