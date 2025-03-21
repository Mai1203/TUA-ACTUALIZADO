# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Expediente.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Expediente(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridWidget.setStyleSheet("")
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_2 = QtWidgets.QWidget(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(140, 30))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #16344D; /* Color de fondo */\n"
"    border-radius: 2px; /* Bordes redondeados */\n"
"    color: white; /* Color del texto */\n"
"    padding: 5px 10px; /* Espaciado interno */\n"
"    border: none; /* Elimina el borde predeterminado */\n"
"    font-size: 10px; /* Tamaño de fuente */\n"
"    text-align: center; /* Alinea el texto a la izquierda */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1A4567; /* Color de fondo al pasar el mouse */\n"
"    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); /* Sombra al pasar el mouse */\n"
"    transform: scale(1.02); /* Ligero aumento al pasar el mouse */\n"
"    transition: all 0.3s ease-in-out; /* Transición suave */\n"
"}\n"
"\n"
"QPushButton::icon {\n"
"    padding-right: 5px; /* Espaciado entre el icono y el texto */\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../../assets/iconos/anadir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(140, 30))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #16344D; /* Color de fondo */\n"
"    border-radius: 2px; /* Bordes redondeados */\n"
"    color: white; /* Color del texto */\n"
"    padding: 5px 10px; /* Espaciado interno */\n"
"    border: none; /* Elimina el borde predeterminado */\n"
"    font-size: 10px; /* Tamaño de fuente */\n"
"    text-align: center; /* Alinea el texto a la izquierda */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1A4567; /* Color de fondo al pasar el mouse */\n"
"    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); /* Sombra al pasar el mouse */\n"
"    transform: scale(1.02); /* Ligero aumento al pasar el mouse */\n"
"    transition: all 0.3s ease-in-out; /* Transición suave */\n"
"}\n"
"\n"
"QPushButton::icon {\n"
"    padding-right: 10px; /* Espaciado entre el icono y el texto */\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\../../assets/iconos/actualizar-flecha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.gridWidget)
        self.widget.setStyleSheet("background-color: rgb(115, 105, 255);")
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.gridWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 759, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Nuevo Expediente"))
        self.pushButton.setText(_translate("MainWindow", "Actualizar Expediente"))
