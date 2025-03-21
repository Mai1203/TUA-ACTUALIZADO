# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\sildebar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sildebar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(203, 602)
        MainWindow.setStyleSheet("background-color: rgb(143, 167, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(150, 0))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(150, 60))
        self.label.setMaximumSize(QtCore.QSize(150, 60))
        self.label.setStyleSheet(" background-color: #16344D; /* Color de fondo */")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\../../assets/icono.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(140, 25))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: #16344D; /* Color de fondo */\n"
"    border-radius: 2px; /* Bordes redondeados */\n"
"    color: white; /* Color del texto */\n"
"    padding: 5px 10px; /* Espaciado interno */\n"
"    border: none; /* Elimina el borde predeterminado */\n"
"    font-size: 10px; /* Tamaño de fuente */\n"
"    text-align: left; /* Alinea el texto a la izquierda */\n"
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
        icon.addPixmap(QtGui.QPixmap(".\\../../assets/iconos/expediente (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(140, 25))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: #16344D; /* Color de fondo */\n"
"    border-radius: 2px; /* Bordes redondeados */\n"
"    color: white; /* Color del texto */\n"
"    padding: 5px 10px; /* Espaciado interno */\n"
"    border: none; /* Elimina el borde predeterminado */\n"
"    font-size: 10px; /* Tamaño de fuente */\n"
"    text-align: left; /* Alinea el texto a la izquierda */\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\../../assets/iconos/grafico-de-barras.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(140, 25))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #16344D; /* Color de fondo */\n"
"    border-radius: 2px; /* Bordes redondeados */\n"
"    color: white; /* Color del texto */\n"
"    padding: 5px 10px; /* Espaciado interno */\n"
"    border: none; /* Elimina el borde predeterminado */\n"
"    font-size: 10px; /* Tamaño de fuente */\n"
"    text-align: left; /* Alinea el texto a la izquierda */\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\../../assets/iconos/nuevo-usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        spacerItem1 = QtWidgets.QSpacerItem(20, 220, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
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
"    text-align: center\n"
"; /* Alinea el texto a la izquierda */\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\../../assets/iconos/cerrar-sesion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 203, 18))
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
        self.pushButton_4.setText(_translate("MainWindow", "Expediente"))
        self.pushButton_3.setText(_translate("MainWindow", "Reportes"))
        self.pushButton.setText(_translate("MainWindow", "Control de usuarios"))
        self.pushButton_2.setText(_translate("MainWindow", "Salir"))
