


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TP3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(523, 429)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(26, 82, 461, 161))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(611, 613)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 10, 641, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 160, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(120, 170, 431, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(6, 242, 61, 31))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 220, 431, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(6, 272, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(120, 270, 431, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 320, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(120, 320, 431, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 370, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setUnderline(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(150, 370, 82, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(350, 370, 82, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(134, 442, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setUnderline(False)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("soumettre")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(364, 442, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Formulaire de contact"))
        self.label_2.setText(_translate("Form", "Nom:"))
        self.label_4.setText(_translate("Form", "Prenom:"))
        self.label_5.setText(_translate("Form", "Matricule:"))
        self.label_6.setText(_translate("Form", "Email:"))
        self.label_7.setText(_translate("Form", "Genre:"))
        self.radioButton.setText(_translate("Form", "Masculin"))
        self.radioButton_2.setText(_translate("Form", "Feminin"))
        
        self.pushButton.setText(_translate("Form", "Soumettre"))
        self.pushButton.clicked.connect(self.afficheDialog)
        
        #self.textEditValue=self.textEdit.toPlainText()
        
        self.pushButton_2.setText(_translate("Form", "Effacer"))
        self.pushButton_2.clicked.connect(self.effacer)
    
    def saisirTexte(self):
        self.textEditValue=self.textEdit.toPlainText()
        #self.textEdit_2.toPlainText()
        #self.textEdit_3.toPlainText()
        #self.textEdit_4.toPlainText()
        print(self.textEditValue)
     #print("textEditValue")
        
    def effacer(self):
        self.textEdit.setText("")        
        self.textEdit_2.setText("")
        self.textEdit_3.setText("")
        self.textEdit_4.setText("")
    

    def afficheDialog(self):
        self.textEditValue=self.textEdit.toPlainText()
        self.textEditValue2=self.textEdit_2.toPlainText()
        self.textEditValue3=self.textEdit_3.toPlainText()
        self.textEditValue4=self.textEdit_4.toPlainText()
        print(self.textEditValue)
        Dialog.show()
        
        
        
        Di.label.setText("votre nom : " + self.textEditValue + "\n" + "votre prenom:" + self.textEditValue2 + "\n" +"votre matricule:" +self.textEditValue3 + "\n" +"votre email:" + self.textEditValue4)
        




import sys

app=QtWidgets.QApplication(sys.argv)
Form=QtWidgets.QWidget()
ui=Ui_Form()
ui.setupUi(Form)


Dialog=QtWidgets.QDialog()
Di=Ui_Dialog()
Di.setupUi(Dialog)




    #afficher
Form.show()
    #les signaux



sys.exit(app.exec_())