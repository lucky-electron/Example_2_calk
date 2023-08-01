from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication([])

win = QMainWindow()
button = QPushButton('My Button')
win.setCentralWidget(button)
win.show()

app.exec()