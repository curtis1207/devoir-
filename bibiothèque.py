# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3


#Devoir fait par SIMO CURIS 23086 ET EHODE YANNICK 23069

class cinquiemeFenetre(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(597, 593)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 250, 531, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 47, 13))
        self.label_3.setObjectName("label_3")
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(70, 130, 258, 101))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout.addWidget(self.textEdit_2)
        self.textEdit_3 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout.addWidget(self.textEdit_3)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 10, 541, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(416, 170, 151, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 51, 41))
        self.label_2.setObjectName("label_2")
        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(410, 200, 161, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(410, 130, 161, 23))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(120, 430, 311, 151))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "INSCRIRE"))
        self.pushButton_3.setText(_translate("Form", "MODIFIER"))
        self.pushButton_4.setText(_translate("Form", "DESINSCRIRE"))
        self.label_3.setText(_translate("Form", "NOM"))
        self.label_4.setText(_translate("Form", "PRENOM"))
        self.label.setText(_translate("Form", "GESTION  DES ENSEIGNANTS"))
        self.label_5.setText(_translate("Form", "RECHERCHER"))
        self.label_2.setText(_translate("Form", "Matricule"))
        self.pushButton.setText(_translate("Form", "ACTUALISER"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Matricule"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "NOM"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "PRENOM"))

        self.pushButton_4.clicked.connect(self.supprimer)
        self.pushButton.clicked.connect(self.actualiser)
        self.pushButton_3.clicked.connect(self.modifier)
        self.loaddata()
        self.pushButton_2.clicked.connect(self.enregistre4)
       
    def actualiser(self):
        self.textEdit.setText("")
        self.textEdit_2.setText("")
        self.textEdit_3.setText("")
        self.loaddata()
        
    def loaddata(self):
        connection = sqlite3.connect("biblo.db")
        curseur = connection.cursor()
        sqlstr = 'SELECT * FROM Enseignant LIMIT 40'

        tablerow=0
        results = curseur.execute(sqlstr)
        self.tableWidget.setRowCount(40)
        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow+=1
   
    def supprimer(self):
        connexion=sqlite3.connect("biblo.db")
        curseur =connexion.cursor()
        sql='DELETE FROM Livre WHERE Matricule=?'
        curseur.execute(sql)
        connexion.commit()
        print('Enregistrement supprimé')
        curseur.close()
        connexion.close()   
        
    def modifier(self):
        connexion=sqlite3.connect("biblo.db")
        curseur =connexion.cursor()
        sql='UPDATE Enseigant SET Nom=nom,Prenom=prenom WHERE Matricule=matricule'
        curseur.execute(sql)
        connexion.commit()
        print('Enregistrement modifié')
        curseur.close()
        connexion.close()
    
    def enregistre4(self):
             
        Matricule=self.textEdit.toPlainText()
        Nom=self.textEdit_2.toPlainText()
        Prenom=self.textEdit_3.toPlainText()
         
        
        print(Matricule,Nom,Prenom)
        connexion=sqlite3.connect("biblo.db")
        curseur =connexion.cursor()
        curseur.execute('''CREATE TABLE IF NOT EXISTS Enseignant( Matricule INTEGER PRIMARY KEY  UNIQUE, Nom TEXT, Prenom Text )''')
        curseur.execute("INSERT INTO Enseignant(Matricule,Nom,Prenom)VALUES(?,?,?)",(Matricule,Nom,Prenom))
        connexion.commit() 
        print('données enregistrées avec succés:')  
   
        
        connexion.close()            

class quatriemeFenetre(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(596, 592)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 51, 41))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 220, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(446, 180, 151, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 270, 531, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(440, 210, 161, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(100, 130, 258, 111))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout.addWidget(self.textEdit_2)
        self.textEdit_3 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout.addWidget(self.textEdit_3)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(440, 140, 161, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 20, 541, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(150, 380, 301, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "NOM"))
        self.label_2.setText(_translate("Form", "Matricule"))
        self.label_4.setText(_translate("Form", "PRENOM"))
        self.label_5.setText(_translate("Form", "RECHERCHER"))
        self.pushButton_2.setText(_translate("Form", "INSCRIRE"))
        self.pushButton_3.setText(_translate("Form", "MODIFIER"))
        self.pushButton_4.setText(_translate("Form", "DESINSCRIRE"))
        self.pushButton.setText(_translate("Form", "ACTUALISER"))
        self.label.setText(_translate("Form", "GESTION  DES ETUDIANTS"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Matricule"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "NOM"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "PRENOM"))

        self.pushButton_4.clicked.connect(self.supprimer)
        self.pushButton.clicked.connect(self.actualiser)
        self.pushButton_3.clicked.connect(self.modifier)
        self.loaddata()

        self.pushButton_2.clicked.connect(self.enregistre3)
        
    def actualiser(self):
        self.textEdit.setText("")
        self.textEdit_2.setText("")
        self.textEdit_3.setText("")
        self.loaddata()
        
    def loaddata(self):
        connection = sqlite3.connect("biblo.db")
        curseur = connection.cursor()
        sqlstr = 'SELECT * FROM Etudiant LIMIT 40'

        tablerow=0
        results = curseur.execute(sqlstr)
        self.tableWidget.setRowCount(40)
        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow+=1
   
    def supprimer(self):
        connexion=sqlite3.connect("biblo.db")
        curseur =connexion.cursor()
        sql='DELETE FROM Etudiant WHERE Matricule=?'
        curseur.execute(sql)
        connexion.commit()
        print('Enregistrement supprimé')
        self.loaddata()
        curseur.close()
        connexion.close()   
        
    def modifier(self):
        connexion=sqlite3.connect("biblo.db")
        curseur =connexion.cursor()
        sql='UPDATE Etudiant SET Nom=nom,Prenom=prenom WHERE Matricule=matricule'
        curseur.execute(sql)
        connexion.commit()
        self.loaddata()
        print('Enregistrement modifié')
        curseur.close()
        connexion.close()
        
        
    def enregistre3(self):
             
        Matricule=self.textEdit.toPlainText()
        Nom=self.textEdit_2.toPlainText()
        Prenom=self.textEdit_3.toPlainText()
         
        
        print(Matricule,Nom,Prenom)
        connexion=sqlite3.connect("biblo.db")
        curseur =connexion.cursor()
        curseur.execute('''CREATE TABLE IF NOT EXISTS Etudiant( Matricule INTEGER PRIMARY KEY  UNIQUE, Nom TEXT, Prenom Text )''')
        curseur.execute("INSERT INTO Etudiant(Matricule,Nom,Prenom)VALUES(?,?,?)",(Matricule,Nom,Prenom))
        connexion.commit() 
        self.loaddata()
        print('données enregistrées avec succés:')  
        self.textEdit.setText("")
        self.textEdit_2.setText("")
        self.textEdit_3.setText("")
       
        
        connexion.close()            

class troisiemeFenetre(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(599, 573)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 320, 531, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(80, 160, 221, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(420, 200, 161, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 61, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 61, 20))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 47, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 210, 71, 20))
        self.label_7.setObjectName("label_7")
        self.textEdit_5 = QtWidgets.QTextEdit(Form)
        self.textEdit_5.setGeometry(QtCore.QRect(80, 200, 221, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 10, 541, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 61, 41))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(426, 170, 151, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(420, 130, 161, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(80, 120, 221, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_6 = QtWidgets.QTextEdit(Form)
        self.textEdit_6.setGeometry(QtCore.QRect(80, 240, 221, 31))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(80, 70, 221, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(10, 290, 47, 13))
        self.label_8.setObjectName("label_8")
        self.textEdit_7 = QtWidgets.QTextEdit(Form)
        self.textEdit_7.setGeometry(QtCore.QRect(80, 280, 221, 31))
        self.textEdit_7.setObjectName("textEdit_7")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 460, 581, 101))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "AJOUTER"))
        self.pushButton_3.setText(_translate("Form", "MODIFIER"))
        self.pushButton_4.setText(_translate("Form", "SUPRIMER"))
        self.label_3.setText(_translate("Form", "Date-debut"))
        self.label_4.setText(_translate("Form", "Date-fin"))
        self.label_6.setText(_translate("Form", "Rendu"))
        self.label_7.setText(_translate("Form", "Date-prolongé"))
        self.label.setText(_translate("Form", "GESTION  DES EMPRUNTS"))
        self.label_2.setText(_translate("Form", "ID_emprunt"))
        self.label_5.setText(_translate("Form", "RECHERCHER"))
        self.pushButton.setText(_translate("Form", "ACTUALISER"))
        self.label_8.setText(_translate("Form", "ID_livre"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID_emprunt"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Date-debut"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Date-fin"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Date-prolongé"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Rendu"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "ID_livre"))
        
        self.pushButton_4.clicked.connect(self.supprimer)
        self.pushButton.clicked.connect(self.actualiser)
        self.pushButton_3.clicked.connect(self.modifier)
        self.loaddata()
        self.pushButton_2.clicked.connect(self.enregistre2)
        
    def actualiser(self):
        self.textEdit.setText("")
        self.textEdit_3.setText("")
        self.textEdit_2.setText("")
        self.textEdit_5.setText("")
        self.textEdit_6.setText("")
        self.textEdit_6.setText("")
        self.loaddata()
        
    def loaddata(self):
        connection = sqlite3.connect("biblo.db")
        curseur = connection.cursor()
        sqlstr = 'SELECT * FROM Emprunt LIMIT 40'

        tablerow=0
        results = curseur.execute(sqlstr)
        self.tableWidget.setRowCount(40)
        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
        
            tablerow+=1
   
    def supprimer(self):
        connexion=sqlite3.connect("biblo.db")
        curseur =connexion.cursor()
        sql='DELETE FROM Emprunt WHERE Id_emprunt=?'
        curseur.execute(sql)
        connexion.commit()
        self.loaddata()
        print('Enregistrement supprimé')
        self.loaddata()
        curseur.close()
        connexion.close()   
        
    def modifier(self):
        connexion=sqlite3.connect("biblo.db")
        curseur =connexion.cursor()
        sql='UPDATE Emprunt SET Id_Emprunt=id_Emprunt,Date_debut=date_debut,Date_fin=dat_fin,Date_prolongé=date_prolongé,Rendu=rendu WHERE Id_emprunte=id_emprunt'
        curseur.execute(sql)
        connexion.commit()
        self.loaddata()
        self.loaddata()
        print('Enregistrement modifié')
        curseur.close()
        connexion.close()
        
    def enregistre2(self):   
        Id_Emprunt=self.textEdit.toPlainText()
        Date_debut=self.textEdit_3.toPlainText()
        Date_fin=self.textEdit_2.toPlainText()
        Date_prolongé=self.textEdit_5.toPlainText()
        Rendu=self.textEdit_6.toPlainText() 
        Id_livre=self.textEdit_7.toPlainText() 
        print(Id_Emprunt,Date_debut,Date_fin,Date_prolongé,Rendu)
        connexion=sqlite3.connect("biblo.db")
        curseur =connexion.cursor()
        curseur.execute('''CREATE TABLE IF NOT EXISTS Emprunt( Id_Emprunt INTEGER PRIMARY KEY  UNIQUE, Date_debut TEXT, Date_fin Text,Date_prolongé,Rendu )''')
        curseur.execute("INSERT INTO Emprunt(Id_Emprunt,Date_debut,Date_fin,Date_prolongé,Rendu)VALUES(?,?,?,?,?)",(Id_Emprunt,Date_debut,Date_fin,Date_prolongé,Rendu))
        connexion.commit() 
        print('données enregistrées avec succés:')  
        self.loaddata()
        
        connexion.close()            

        
class Deuxieme_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 599)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 230, 47, 13))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 150, 161, 23))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 150, 258, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_4.setObjectName("textEdit_4")
        self.verticalLayout_3.addWidget(self.textEdit_4)
        self.textEdit_5 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_5.setObjectName("textEdit_5")
        self.verticalLayout_3.addWidget(self.textEdit_5)
        self.textEdit_6 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_6.setObjectName("textEdit_6")
        self.verticalLayout_3.addWidget(self.textEdit_6)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 40, 541, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(406, 190, 151, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 270, 531, 111))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_4.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_4.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_4.addWidget(self.pushButton_7)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 51, 41))
        self.label_2.setObjectName("label_2")
        self.textEdit_7 = QtWidgets.QTextEdit(Form)
        self.textEdit_7.setGeometry(QtCore.QRect(400, 220, 161, 31))
        self.textEdit_7.setObjectName("textEdit_7")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(110, 420, 321, 61))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "AUTEUR"))
        self.pushButton.setText(_translate("Form", "ACTUALISER"))
        self.label.setText(_translate("Form", "GESTION  DES LIVRES"))
        self.label_3.setText(_translate("Form", "TITRE"))
        self.label_5.setText(_translate("Form", "RECHERCHER"))
        self.pushButton_5.setText(_translate("Form", "AJOUTER"))
        self.pushButton_6.setText(_translate("Form", "MODIFIER"))
        self.pushButton_7.setText(_translate("Form", "SUPPRIMER"))
        self.label_2.setText(_translate("Form", "ID_livre"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID_livre"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "TITRE"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "AUTEUR"))
        
        
        self.pushButton_5.clicked.connect(self.enregistre)
        self.pushButton_7.clicked.connect(self.supprimer)
        self.pushButton.clicked.connect(self.actualiser)
        self.pushButton_6.clicked.connect(self.modifier)
        self.loaddata()

    def enregistre(self):
        Id_livre=self.textEdit_4.toPlainText()
        Titre=self.textEdit_5.toPlainText()
        Auteur=self.textEdit_6.toPlainText()
        print(Id_livre,Titre,Auteur)
        connexion=sqlite3.connect("biblo.db")
        curseur =connexion.cursor()
        curseur.execute('''CREATE TABLE IF NOT EXISTS Livre( Id_livre INTEGER PRIMARY KEY  UNIQUE, Titre TEXT, Auteur Text )''')
        curseur.execute("INSERT INTO Livre(Id_livre,Titre,Auteur)VALUES(?,?,?)",(Id_livre,Titre,Auteur))
        connexion.commit() 
        print('données enregistrées avec succés:')  
       
        connexion.close() 
    def actualiser(self):
         self.textEdit_4.setText("")
         self.textEdit_5.setText("")
         self.textEdit_6.setText("")
         self.loaddata()
        
    def supprimer(self):
        connexion=sqlite3.connect("biblo.db")
        curseur =connexion.cursor()
        sql='DELETE FROM Livre WHERE Id_livre=?'
        curseur.execute(sql)
        connexion.commit()
        print('Enregistrement supprimé')
        curseur.close()
        connexion.close()
    
    def modifier(self):
        connexion=sqlite3.connect("biblo.db")
        curseur =connexion.cursor()
        sql='UPDATE Livre SET Titre=titre,auteur=Auteur WHERE Id_livre=Id_Livre'
        curseur.execute(sql)
        connexion.commit()
        print('Enregistrement modifié')
        curseur.close()
        connexion.close()
        
    
    def loaddata(self):
        connection = sqlite3.connect("biblo.db")
        curseur = connection.cursor()
        sqlstr = 'SELECT * FROM Livre LIMIT 40'

        tablerow=0
        results = curseur.execute(sqlstr)
        self.tableWidget.setRowCount(40)
        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            
            
            tablerow+=1
                      

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(584, 513)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 10, 581, 501))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Bibliothèque "))
        self.pushButton.setText(_translate("Form", "LIVRE"))
        self.pushButton_2.setText(_translate("Form", "EMPRUNT"))
        self.pushButton_3.setText(_translate("Form", "ETUDIANT"))
        self.pushButton_4.setText(_translate("Form", "ENSEIGNANT"))
        
       # connexion=sqlite3.connect("biblio.db")
        
        self.pushButton.clicked.connect(self.deuxiemeFenetre)
        self.pushButton_2.clicked.connect(self.troisiemeFenetre)
        self.pushButton_3.clicked.connect(self.quatriemeFenetre)
        self.pushButton_4.clicked.connect(self.cinquiemeFenetre)
       
        
        
    # C'est ici que je crée la méthode permettant d'ouvrir la seconde interface
    # c'est pareil que dans la méthode main sauf qu'on utilise le self    
    def deuxiemeFenetre(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Deuxieme_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()
        
    def troisiemeFenetre(self):
        self.Form = QtWidgets.QWidget()
        self.ui = troisiemeFenetre()
        self.ui.setupUi(self.Form)
        self.Form.show()  
        
        
    def quatriemeFenetre(self):
        self.Form = QtWidgets.QWidget()
        self.ui = quatriemeFenetre()
        self.ui.setupUi(self.Form)
        self.Form.show()   
        
        
    def cinquiemeFenetre(self):
        self.Form = QtWidgets.QWidget()
        self.ui = cinquiemeFenetre()
        self.ui.setupUi(self.Form)
        self.Form.show()
        
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    
    Form.show()
    sys.exit(app.exec_())    
    