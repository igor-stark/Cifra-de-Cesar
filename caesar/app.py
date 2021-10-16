from PyQt5.QtCore import QUrl
from caesarcipher import *
import caesarscript
from PyQt5.Qt import QDesktopServices
import sys


class App(Ui_Form):
    def __init__(self, window):
        self.setupUi(window)
        self.EncryptButton.clicked.connect(self.clickEncrypt)
        self.DecryptButton.clicked.connect(self.clickDecrypt)
        self.ClearButton.clicked.connect(self.clear)
        self.GitHubButton.clicked.connect(self.open_link)
        self.CloseButton.clicked.connect(self.closeApp)

    def clickEncrypt(self):
        msg = str(self.EncryptText.text())
        key = self.EncryptKey.text()
        try:
            result = caesarscript.caesar(msg, key)
            return self.EncryptResult.setText(result)
        except TypeError:
            self.EncryptResult.setText("Coloque uma chave válida")
        except ValueError:
            self.EncryptResult.setText("Coloque uma chave válida")

    def clickDecrypt(self):
        if self.BruteForceButton.isChecked():
            msg = self.DecryptText.text()
            result = caesarscript.brute_force(msg)
            return self.DecryptResult.setText(result)
        else:
            msg = self.DecryptText.text()
            key = self.DecryptKey.text()
            try:
                result = caesarscript.caesar_decrypt(msg, key)
                return self.DecryptResult.setText(result)
            except TypeError:
                self.DecryptResult.setText("Coloque uma chave válida")
            except ValueError:
                self.DecryptResult.setText("Coloque uma chave válida")

    def clear(self):
        self.EncryptText.setText("")
        self.DecryptText.setText("")
        self.EncryptKey.setText("")
        self.DecryptKey.setText("")
        self.EncryptResult.setText("")
        self.DecryptResult.setText("")
        return print("Tudo limpo!")

    def open_link(self):  # funcionando
        url = QUrl("https://github.com/igor-stark")
        QDesktopServices.openUrl(url)

    def closeApp(self):
        app.quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = App(MainWindow)
    MainWindow.show()
    app.exec_()
