from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindowEx import MainWindowEx
app=QApplication([])
myWindow= MainWindowEx()
myWindow.setupUi(QMainWindow())
Window.show()
app.exec()
