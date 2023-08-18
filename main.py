from PyQt6.QtWidgets import QMainWindow, QDial, QLabel, QPushButton, QApplication, QVBoxLayout, QWidget, QHBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QTimer

class AudioCompressorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 400)
        self.setWindowTitle("Audio Compressor")
        self.setStyleSheet("background: #34495E;")
        self.createUI()
        self.changeButtonColor()

    def createUI(self):
        main_layout = QVBoxLayout()

        button_layout = QHBoxLayout()
        button_data = [
            ('Limiter'),
            ('Stereo'),
            ('Filter'),
            ('Left'),
            ('Mute'),
            ('Side Chain'),
            ('Mono'),
            ('Auto'),
            ('Right'),
        ]

        self.buttons = {}
        for text in button_data:
            button = QPushButton(text, self)
            button.setCheckable(True)
            button.clicked.connect(self.changeButtonColor)
            self.buttons[text] = button
            button_layout.addWidget(button)
        
        main_layout.addLayout(button_layout)

        dial_layout = QHBoxLayout()
        self.dials = []
        self.dials_label = []
        self.dial_labels = ['Threshold', 'Attack', 'Release', 'Output']  # Store dial labels in a class variable

        for i in range(4):
            dial_label = QLabel(self.dial_labels[i], self)
            dial_label.setFont(QFont('Arial', 10))
            dial_label.setStyleSheet("color: #ECF0F1;")
            dial_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            dial_label.setFixedHeight(20)
            self.dials_label.append(dial_label)

            dial = QDial(self)
            dial.setMinimum(0)
            dial.setMaximum(99)
            dial.setValue(50)
            dial.valueChanged.connect(self.updateDialLabel)
            dial.sliderReleased.connect(self.showDialLabels)
            dial.setFixedSize(140, 140)
            self.dials.append(dial)

            dial_widget = QWidget(self)
            dial_widget_layout = QVBoxLayout()
            dial_widget_layout.addWidget(dial, alignment=Qt.AlignmentFlag.AlignHCenter)
            dial_widget_layout.addWidget(dial_label, alignment=Qt.AlignmentFlag.AlignHCenter)
            dial_widget.setLayout(dial_widget_layout)
            dial_layout.addWidget(dial_widget)

        main_layout.addLayout(dial_layout)

        self.updatedialslabel = QLabel(self)
        self.updatedialslabel.setFont(QFont('Arial', 12))
        self.updatedialslabel.setStyleSheet("color: #ECF0F1;")
        self.updatedialslabel.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        main_layout.addWidget(self.updatedialslabel)
        self.updatedialslabel.hide()

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.label_timer = QTimer(self)
        self.label_timer.timeout.connect(self.hideDialLabels)
        self.label_timer.setSingleShot(True)

    def changeButtonColor(self):
        for button in self.buttons.values():
            if button.text() == 'Mute' and button.isChecked():
                button.setStyleSheet("background-color: #E74C3C; color: white; font-weight: bold;")
            else:
                button.setStyleSheet("background-color: #3498DB; color: white; font-weight: bold;")


    def updateDialLabel(self, value):
        dial = self.sender()
        index = self.dials.index(dial)
        dial_label = self.dials_label[index]
        dial_label.setText(f'{self.dial_labels[index]}: {value}')  # Update dial label text
        dial_label.adjustSize()

    def showDialLabels(self):
        self.updatedialslabel.hide()
        for label in self.dials_label:
            label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            label.show()

    def hideDialLabels(self):
        for label in self.dials_label:
            label.hide()
        self.updatedialslabel.show()

def main():
    app = QApplication([])
    window = AudioCompressorApp()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
