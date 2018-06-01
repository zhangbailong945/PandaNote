# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\eric6Projects\demo2\NoteMain.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_NoteMain(object):
    def setupUi(self, NoteMain):
        NoteMain.setObjectName("NoteMain")
        NoteMain.resize(315, 484)
        NoteMain.setMinimumSize(QtCore.QSize(0, 484))
        NoteMain.setMaximumSize(QtCore.QSize(335, 484))
        NoteMain.setWindowIcon(QIcon(":/pic/images/16x16.ico"))
        self.verticalLayout = QtWidgets.QVBoxLayout(NoteMain)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imageLabel = QtWidgets.QLabel(NoteMain)
        self.imageLabel.setText("")
        self.imageLabel.setPixmap(QtGui.QPixmap(":/pic/images/panda.png"))
        self.imageLabel.setObjectName("imageLabel")
        self.verticalLayout.addWidget(self.imageLabel)
        self.noteText = QtWidgets.QTextEdit(NoteMain)
        self.noteText.setObjectName("noteText")
        self.verticalLayout.addWidget(self.noteText)
        self.saveBtn = QtWidgets.QPushButton(NoteMain)
        self.saveBtn.setObjectName("saveBtn")
        self.verticalLayout.addWidget(self.saveBtn)
        self.pushButton_2 = QtWidgets.QPushButton(NoteMain)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(NoteMain)
        self.pushButton_2.clicked.connect(NoteMain.close)
        QtCore.QMetaObject.connectSlotsByName(NoteMain)
        NoteMain.setTabOrder(self.noteText, self.saveBtn)
        NoteMain.setTabOrder(self.saveBtn, self.pushButton_2)

    def retranslateUi(self, NoteMain):
        _translate = QtCore.QCoreApplication.translate
        NoteMain.setWindowTitle(_translate("NoteMain", "记仇日记"))
        self.saveBtn.setText(_translate("NoteMain", "生成"))
        self.pushButton_2.setText(_translate("NoteMain", "退出"))

import note_qrc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NoteMain = QtWidgets.QWidget()
    ui = Ui_NoteMain()
    ui.setupUi(NoteMain)
    NoteMain.show()
    sys.exit(app.exec_())

