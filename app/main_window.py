from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QLineEdit, QVBoxLayout, QWidget, QStyle, QHBoxLayout, QPushButton)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Bin2Dec App")
        self.setGeometry(100, 100, 800, 600)

        entry_label = QLabel("Hello, PyQt!", self)
        label_style = "QLabel { color: blue; font-size: 16px; font-weight: bold; }"
        entry_label.setStyleSheet(label_style)
        entry_label.setGeometry(370, 10, 200, 30)

        # widgets

        self.insert_number_label = QLabel("Enter a number", self)
        self.insert_number_input = QLineEdit(self)
        self.display_result_label = QLabel("", self)
        self.update_push_button = QPushButton("Result", self)

        # layout

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setSpacing(1)
        self.vertical_layout.addWidget(self.insert_number_label)
        self.vertical_layout.addWidget(self.insert_number_input)
        self.vertical_layout.addWidget(self.display_result_label)
        self.vertical_layout.addWidget(self.update_push_button)

        container = QWidget()
        container.setLayout(self.vertical_layout)

        self.setCentralWidget(container)

        self.update_push_button.clicked.connect(self.update_display)

    def update_display(self):
        entered_text = self.insert_number_input.text()

        if not self.is_binary_string_valid():
            self.display_result_label.setText("Error!")
            self.display_result_label.setStyleSheet("QLabel { color: red; }")
            self.insert_number_input.setReadOnly(True)
            return
        else:
            decimal_number = int(entered_text, 2)
            self.display_result_label.setText(f"{decimal_number}")

    def is_binary_string_valid(self):
        binary_string = self.insert_number_input.text()
        binary_string.replace("0", "")
        if binary_string == "":
            return True
        elif binary_string.replace("1", "") == "":
            return True
        else:
            return False
