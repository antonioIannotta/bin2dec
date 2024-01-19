from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Bin2Dec App")
        self.setGeometry(100, 100, 800, 600)

        label = QLabel("Hello, PyQt!", self)
        label.setGeometry(10, 10, 200, 30)

        # widgets

        self.label = QLabel("Enter a number", self)
        self.number_input = QLineEdit(self)
        self.display_label = QLabel("", self)

        #layout

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.number_input)
        layout.addWidget(self.display_label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.number_input.textChanged.connect(self.update_display)

    def update_display(self):
        entered_text = self.number_input.text()
        if "c" in entered_text:
            self.display_label.setText("Error!")
            self.number_input.setReadOnly(True)
            return

        self.display_label.setText(f"{entered_text}")


