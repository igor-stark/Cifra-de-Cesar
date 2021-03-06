# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caesarcipher.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import images_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1162, 833)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 10, 1111, 801))
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(340, 70, 681, 651))
        self.label_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(18, 14, 30, 255), stop:1 rgba(61, 124, 120, 200));\n"
            "border-radius: 50px;"
        )
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.Titulo = QtWidgets.QLabel(self.widget)
        self.Titulo.setGeometry(QtCore.QRect(510, 160, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.Titulo.setFont(font)
        self.Titulo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Titulo.setAutoFillBackground(False)
        self.Titulo.setStyleSheet("color: rgba(255, 255, 255, 220);")
        self.Titulo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Titulo.setObjectName("Titulo")
        self.DecryptText = QtWidgets.QLineEdit(self.widget)
        self.DecryptText.setGeometry(QtCore.QRect(730, 240, 241, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DecryptText.setFont(font)
        self.DecryptText.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "border: 2px solid rgba(0, 0, 0, 0);\n"
            "border-bottom-color: rgba(0,0,0,255);\n"
            "color: rgba(255,255,255, 200);\n"
            "paddling-bottom: 7px;"
        )
        self.DecryptText.setText("")
        self.DecryptText.setObjectName("DecryptText")
        self.EncryptText = QtWidgets.QLineEdit(self.widget)
        self.EncryptText.setGeometry(QtCore.QRect(370, 240, 251, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EncryptText.setFont(font)
        self.EncryptText.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "border: 2px solid rgba(0, 0, 0, 0);\n"
            "border-bottom-color: rgba(0,0,0,255);\n"
            "color: rgba(255,255,255, 200);\n"
            "paddling-bottom: 7px;"
        )
        self.EncryptText.setText("")
        self.EncryptText.setObjectName("EncryptText")
        self.EncryptKey = QtWidgets.QLineEdit(self.widget)
        self.EncryptKey.setGeometry(QtCore.QRect(440, 320, 81, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.EncryptKey.setFont(font)
        self.EncryptKey.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "border: 2px solid rgba(0, 0, 0, 0);\n"
            "border-bottom-color: rgba(0,0,0,255);\n"
            "color: rgba(255,255,255, 200);\n"
            "paddling-bottom: 7px;"
        )
        self.EncryptKey.setText("")
        self.EncryptKey.setObjectName("EncryptKey")
        self.DecryptKey = QtWidgets.QLineEdit(self.widget)
        self.DecryptKey.setGeometry(QtCore.QRect(730, 320, 81, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DecryptKey.setFont(font)
        self.DecryptKey.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "border: 2px solid rgba(0, 0, 0, 0);\n"
            "border-bottom-color: rgba(0,0,0,255);\n"
            "color: rgba(255,255,255, 200);\n"
            "paddling-bottom: 7px;"
        )
        self.DecryptKey.setText("")
        self.DecryptKey.setObjectName("DecryptKey")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(670, 250, 1, 381))
        self.line.setStyleSheet("background-color: rgba(0,0,0,255);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.EncryptResult = QtWidgets.QLineEdit(self.widget)
        self.EncryptResult.setGeometry(QtCore.QRect(370, 500, 241, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EncryptResult.setFont(font)
        self.EncryptResult.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "border: 2px solid rgba(0, 0, 0, 0);\n"
            "border-bottom-color: rgba(0,0,0,255);\n"
            "color: rgba(255,255,255, 200);\n"
            "paddling-bottom: 7px;"
        )
        self.EncryptResult.setText("")
        self.EncryptResult.setReadOnly(True)
        self.EncryptResult.setObjectName("EncryptResult")
        self.DecryptResult = QtWidgets.QLineEdit(self.widget)
        self.DecryptResult.setGeometry(QtCore.QRect(730, 500, 241, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DecryptResult.setFont(font)
        self.DecryptResult.setAutoFillBackground(False)
        self.DecryptResult.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "border: 2px solid rgba(0, 0, 0, 0);\n"
            "border-bottom-color: rgba(0,0,0,255);\n"
            "color: rgba(255,255,255, 200);\n"
            "paddling-bottom: 7px;"
        )
        self.DecryptResult.setInputMask("")
        self.DecryptResult.setText("")
        self.DecryptResult.setFrame(True)
        self.DecryptResult.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.DecryptResult.setDragEnabled(False)
        self.DecryptResult.setReadOnly(True)
        self.DecryptResult.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.DecryptResult.setClearButtonEnabled(False)
        self.DecryptResult.setObjectName("DecryptResult")
        self.EncryptButton = QtWidgets.QPushButton(self.widget)
        self.EncryptButton.setGeometry(QtCore.QRect(370, 420, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.EncryptButton.setFont(font)
        self.EncryptButton.setStyleSheet(
            "QPushButton#EncryptButton{\n"
            "border-style:outset;\n"
            "border-radius: 15px;\n"
            "border-width: 2px;\n"
            "border-color: black;\n"
            "color: rgba(255,255,255,200);\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(61, 124, 120, 150));\n"
            "}\n"
            "QPushButton#EncryptButton:hover{\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(0, 0, 0, 190));\n"
            "}\n"
            "QPushButton#EncryptButton:pressed{\n"
            "paddling-left: 5px;\n"
            "paddling-top: 5px;\n"
            "background-color: rgba(248, 248, 255, 100);\n"
            "}"
        )
        self.EncryptButton.setObjectName("EncryptButton")
        self.DecryptButton = QtWidgets.QPushButton(self.widget)
        self.DecryptButton.setGeometry(QtCore.QRect(730, 420, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DecryptButton.setFont(font)
        self.DecryptButton.setStyleSheet(
            "QPushButton#DecryptButton{\n"
            "border-style:outset;\n"
            "border-radius: 15px;\n"
            "border-width: 2px;\n"
            "border-color: black;\n"
            "color: rgba(255,255,255,200);\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(61, 124, 120, 150));\n"
            "}\n"
            "QPushButton#DecryptButton:hover{\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(0, 0, 0, 190));\n"
            "}\n"
            "QPushButton#DecryptButton:pressed{\n"
            "paddling-left: 5px;\n"
            "paddling-top: 5px;\n"
            "background-color: rgba(248, 248, 255, 100);\n"
            "}"
        )
        self.DecryptButton.setObjectName("DecryptButton")
        self.DecoderImage = QtWidgets.QLabel(self.widget)
        self.DecoderImage.setGeometry(QtCore.QRect(590, -10, 171, 181))
        self.DecoderImage.setStyleSheet("")
        self.DecoderImage.setText("")
        self.DecoderImage.setPixmap(QtGui.QPixmap("imgs/caesar2.png"))
        self.DecoderImage.setScaledContents(True)
        self.DecoderImage.setOpenExternalLinks(False)
        self.DecoderImage.setObjectName("DecoderImage")
        self.BruteForceButton = QtWidgets.QRadioButton(self.widget)
        self.BruteForceButton.setGeometry(QtCore.QRect(860, 330, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BruteForceButton.setFont(font)
        self.BruteForceButton.setStyleSheet("color: rgba(255,255,255,200)")
        self.BruteForceButton.setObjectName("BruteForceButton")
        self.ClearButton = QtWidgets.QPushButton(self.widget)
        self.ClearButton.setGeometry(QtCore.QRect(630, 650, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ClearButton.setFont(font)
        self.ClearButton.setStyleSheet(
            "QPushButton#ClearButton{\n"
            "border-style:outset;\n"
            "border-radius: 15px;\n"
            "border-width: 2px;\n"
            "border-color: black;\n"
            "color: rgba(255,255,255,200);\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(61, 124, 120, 150));\n"
            "}\n"
            "\n"
            "QPushButton#ClearButton:hover{\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(0, 0, 0, 190));\n"
            "}\n"
            "QPushButton#ClearButton:pressed{\n"
            "paddling-left: 5px;\n"
            "paddling-top: 5px;\n"
            "background-color: rgba(248, 248, 255, 100);\n"
            "}"
        )
        self.ClearButton.setObjectName("ClearButton")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(270, 110, 71, 571))
        self.frame.setStyleSheet("background-color: rgba(0,0,0,255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setGeometry(QtCore.QRect(140, 110, 181, 571))
        self.frame_2.setStyleSheet(
            "background-color: rgba(0,0,0,255);\n" "border-radius: 40px;"
        )
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.GitHubButton = QtWidgets.QPushButton(self.frame_2)
        self.GitHubButton.setGeometry(QtCore.QRect(10, 10, 171, 101))
        self.GitHubButton.setStyleSheet(
            "QPushButton#GitHubButton{\n"
            "background-color: rgba(0,0,0,255);\n"
            "}\n"
            "QPushButton#GitHubButton:pressed{\n"
            "paddling-left: 5px;\n"
            "paddling-top: 5px;\n"
            "background-color: rgba(0, 139, 139, 100);\n"
            "}\n"
            ""
        )
        self.GitHubButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("imgs/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.GitHubButton.setIcon(icon)
        self.GitHubButton.setIconSize(QtCore.QSize(170, 100))
        self.GitHubButton.setDefault(False)
        self.GitHubButton.setObjectName("GitHubButton")
        self.Observacao = QtWidgets.QTextEdit(self.frame_2)
        self.Observacao.setGeometry(QtCore.QRect(10, 130, 141, 161))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Observacao.setFont(font)
        self.Observacao.setStyleSheet("color: rgba(255,255,255,220)")
        self.Observacao.setReadOnly(True)
        self.Observacao.setObjectName("Observacao")
        self.Contato = QtWidgets.QLabel(self.frame_2)
        self.Contato.setGeometry(QtCore.QRect(10, 510, 171, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Contato.setFont(font)
        self.Contato.setStyleSheet("color: rgba(255,255,255,175)")
        self.Contato.setObjectName("Contato")
        self.Observacao.raise_()
        self.Contato.raise_()
        self.GitHubButton.raise_()
        self.CloseButton = QtWidgets.QPushButton(self.widget)
        self.CloseButton.setGeometry(QtCore.QRect(950, 110, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.CloseButton.setFont(font)
        self.CloseButton.setStyleSheet(
            "QPushButton#CloseButton{\n"
            "color: rgba(255, 255, 255, 180);\n"
            "background-color: rgba(255, 255, 255, 0);\n"
            "background-style: outset;\n"
            "image: url(:/newPrefix/closebuttom.png);\n"
            "}\n"
            "QPushButton#CloseButton:hover{\n"
            "color: rgba(255,255,255,255);\n"
            "}\n"
            "QPushButton#CloseButton:pressed{\n"
            "paddling-left: 5px;\n"
            "paddling-top: 5px;\n"
            "color: rgba(220, 20, 60, 230);\n"
            "}"
        )
        self.CloseButton.setObjectName("CloseButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Titulo.setText(_translate("Form", "Cifra de C??sar"))
        self.DecryptText.setPlaceholderText(_translate("Form", "Texto"))
        self.EncryptText.setPlaceholderText(_translate("Form", "Texto"))
        self.EncryptKey.setPlaceholderText(_translate("Form", "Chave"))
        self.DecryptKey.setPlaceholderText(_translate("Form", "Chave"))
        self.EncryptResult.setPlaceholderText(_translate("Form", "Resultado"))
        self.DecryptResult.setPlaceholderText(_translate("Form", "Resultado"))
        self.EncryptButton.setText(_translate("Form", "Encriptar"))
        self.DecryptButton.setText(_translate("Form", "Decriptar"))
        self.BruteForceButton.setText(_translate("Form", "Brute Force"))
        self.ClearButton.setText(_translate("Form", "Limpar"))
        self.Observacao.setHtml(
            _translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt; font-weight:600; text-decoration: underline;">Observa????o:</span></p>\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;"><br /></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt; font-weight:600;">- O bot??o Brute Force s?? funciona para textos em portugu??s.</span></p></body></html>',
            )
        )
        self.Contato.setText(_translate("Form", "Contato: igorstark@usp.br"))
        self.CloseButton.setText(_translate("Form", "X"))
