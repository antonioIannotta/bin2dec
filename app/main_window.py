from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My PyQt App")
        self.setGeometry(100, 100, 800, 600)

        label = QLabel("Hello, PyQt!", self)
        label.setGeometry(10, 10, 200, 30)
