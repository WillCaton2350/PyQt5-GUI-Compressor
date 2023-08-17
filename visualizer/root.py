from PyQt6.QtWidgets import QMainWindow,QDial
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QFont

class main(QMainWindow):
    def __init__(self):
        super(main,self).__init__()
        self.setGeometry(
        1600,1000,500,800)
        self.setFixedSize(
            500,800)
        self.setWindowTitle(
            "Compressor")
        self.setStyleSheet(
            "background: #141414;")
        self.Ui()
        self.changeColor()
    def Ui(self):
        self.labelQ = QLabel(self)
        self.labelQ.move(
            325,147)
        self.labelQ.setGeometry(
            QtCore.QRect(
            325,145,
            180,30
            ))
        self.labelQ.setFont(
            QFont(
            'Times', 50))
        self.labelQ.setStyleSheet(
            "color:#fff;")
        self.labelQ.setStyleSheet(
            "Background-color:darkblack;")
        self.labelQ2 = QLabel(self)
        self.labelQ2.move(
            325,197)
        self.labelQ2.setGeometry(
            QtCore.QRect(
            325,195,
            180,30))
        self.labelQ2.setFont(
            QFont(
            'Times', 50))
        self.labelQ2.setStyleSheet(
            "color:#fff;")
        self.labelQ2.setStyleSheet(
            "Background-color:darkblack;")
        self.labelQ3 = QLabel(self)
        self.labelQ3.move(
            325,247)
        self.labelQ3.setGeometry(
            QtCore.QRect(
            325,245,180,30))
        self.labelQ3.setFont(QFont(
            'Times', 50))
        self.labelQ3.setStyleSheet(
            "color:#fff;")
        self.labelQ3.setStyleSheet(
            "Background-color:darkblack;")
        self.labelQ4 = QLabel(self)
        self.labelQ4.move(325,97)
        self.labelQ4.setGeometry(
            QtCore.QRect(
            325,95,180,30
            ))
        self.labelQ4.setFont(
            QFont(
            'Times', 50
            ))
        self.labelQ4.setStyleSheet(
            "color:#fff;")
        self.labelQ4.setStyleSheet(
            "Background-color:darkblack;")
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText(
            "Bypass")
        self.btn.move(
            10,100)
        self.btn.setCheckable(True)
        self.btn.clicked.connect(
            self.changeColor)
        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText(
            "Stereo")
        self.btn2.move(
            10,
            150)
        self.btn2.setCheckable(
            True)
        self.btn2.clicked.connect(
            self.changeColor)
        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.setText(
            "Warm")
        self.btn3.move(
            10,
            200)
        self.btn3.setCheckable(
            True)
        self.btn3.clicked.connect(
            self.changeColor)
        self.btn4 = QtWidgets.QPushButton(
            self)
        self.btn4.setText(
            "Left")
        self.btn4.move(10,250)
        self.btn4.setCheckable(True)
        self.btn4.clicked.connect(
            self.changeColor)
        self.btn5 = QtWidgets.QPushButton(self)
        self.btn5.setStyleSheet(
            "color:grey;")
        self.btn5.setText(
            "Side Chain")
        self.btn5.move(135,100)
        self.btn5.setCheckable(True)
        self.btn5.clicked.connect(
            self.changeColor)
        self.btn6 = QtWidgets.QPushButton(self)
        self.btn6.setText(
            "Mono")
        self.btn6.move(135,150)
        self.btn6.setCheckable(True)
        self.btn6.clicked.connect(
            self.changeColor)
        self.btn7 = QtWidgets.QPushButton(self)
        self.btn7.setText("Auto")
        self.btn7.move(
            135,
            200)
        self.btn7.setCheckable(True)
        self.btn7.clicked.connect(
            self.changeColor)
        self.btn8 = QtWidgets.QPushButton(self)
        self.btn8.setStyleSheet(
            "color:#141414;")
        self.btn8.setText("Right")
        self.btn8.move(
            135,250)
        self.btn8.setCheckable(True)
        self.btn8.clicked.connect(
            self.changeColor)
        self.btn9 = QtWidgets.QPushButton(self)
        self.btn9.setText(
            "Mute")
        self.btn9.move(
            360,36)
        self.btn9.setCheckable(True)
        self.btn9.clicked.connect(
            self.changeColor)
        self.dial = QDial(self)
        self.dial.setGeometry(
            QtCore.QRect(
            190, 105, 
            160, 260))
        self.dial.setMinimum(0)
        self.dial.setMaximum(99)
        self.dial.valueChanged.connect(self.dialer)
        self.dial.move(25,300)
        self.dial2 = QDial(self)
        self.dial2.setGeometry(QtCore.QRect(
            190, 105, 
            160, 260))
        self.dial2.setMinimum(0)
        self.dial2.setMaximum(99)
        self.dial2.valueChanged.connect(
            self.dialer)
        self.dial2.move(
            100,
            500)
        self.dial3 = QDial(self)
        self.dial3.setGeometry(
            QtCore.QRect(
            190, 105, 
            160, 260))
        self.dial3.setMinimum(0)
        self.dial3.setMaximum(99)
        self.dial3.valueChanged.connect(
            self.dialer)
        self.dial3.move(
            225,300)
        self.dial4 = QDial(self)
        self.dial4.setGeometry(
            QtCore.QRect(
            190, 105, 
            160, 260))
        self.dial4.setMinimum(0)
        self.dial4.setMaximum(99)
        self.dial4.valueChanged.connect(self.dialer)
        self.dial4.move(
            300,500)
        self.knob1 = QLabel('Threshold', self)
        self.knob1.move(
            60,
            510)
        self.knob1.setFont(
            QFont(
            'Times',
            10))
        self.knob1.setStyleSheet(
            "color:grey;")

        self.knob2 = QLabel(
            'Attack', 
            self)
        self.knob2.move(
            280,
            510)
        self.knob2.setFont(
            QFont(
            'Times', 
            10))
        self.knob2.setStyleSheet(
            "color:grey;")

        self.knob3 = QLabel(
            'Release', 
            self)
        self.knob3.move(143,
                        710)
        self.knob3.setFont(
            QFont(
            'Times', 
            10))
        self.knob3.setStyleSheet(
            "color:grey;")
        self.knob4 = QLabel(
            'Output', 
            self)
        self.knob4.move(
            350,710)
        self.knob4.setFont(
            QFont(
            'Times', 
            10))
        self.knob4.setStyleSheet(
            "color:grey;")
        self.titleLabel = QLabel(
            'Compressor', self)
        self.titleLabel.move(230,770)
        self.titleLabel.setFont(
            QFont(
            'Times', 8))
        self.titleLabel.setStyleSheet("color:grey;")
        self.dial_label = QtWidgets.QLabel(self)
        self.dial_label.setGeometry(
            QtCore.QRect(
            110,100,20,20))
        self.dial_label.setStyleSheet(
            "color:#fff;")
        self.dial_label2 = QtWidgets.QLabel(self)
        self.dial_label2.setGeometry(
            QtCore.QRect(
            110,100,20,20))
        self.dial_label2.setStyleSheet(
            "color:#fff;")
        self.dial_label3 = QtWidgets.QLabel(self)
        self.dial_label3.setGeometry(
            QtCore.QRect(
            110,100,20,20))
        self.dial_label3.setStyleSheet(
            "color:#fff;")
        self.dial_label4 = QtWidgets.QLabel(self)
        self.dial_label4.setGeometry(
            QtCore.QRect(
            110,100,20,20))
        self.dial_label4.setStyleSheet(
            "color:#fff;")
    def changeColor(self):
        button_dict = {
            'btn': self.btn,
            'btn2': self.btn2,
            'btn3': self.btn3,
            'btn4': self.btn4,
            'btn5': self.btn5,
            'btn6': self.btn6,
            'btn7': self.btn7,
            'btn8': self.btn8}
        btn = {
            'btn9':self.btn9}
        any_button_checked = any(
            button.isChecked(
            ) for button in button_dict.values(
            ))
        color = "#c31432" if any_button_checked else "#c31432"
        color2 = '#304352'
        for button in button_dict.values():
            if button.isChecked(
            ) and button == self.btn9:
                button.setStyleSheet(
                    "background-color: darkred;")
            else:
                button.setStyleSheet(
                    f"background-color: {color2};")
                # for mute button
        for button in btn.values():
            if button.isChecked(
            ) and button == self.btn9:
                button.setStyleSheet(
                    "background-color: darkred;")
            else:
                button.setStyleSheet(
                    f"background-color: {color};")
    def dialer(self):
        value = self.dial.value()
        self.dial.setRange(
            -50,0)
        self.dial_label.setText(
            f'dB: {value}')
        self.dial_label.move(
            330,100)
        self.dial_label.adjustSize()
        value2 = self.dial2.value()
        self.dial2.setRange(
            0,500)
        self.dial_label2.setText(
            f'ms: {str(value2)}')
        self.dial_label2.move(
            330,150)
        self.dial_label2.adjustSize()
        value3 = self.dial3.value()
        self.dial3.setRange(
            0,200)
        self.dial_label3.setText(
            f'ms: {str(value3)}')
        self.dial_label3.move(
            330,200)
        self.dial_label3.adjustSize()
        value4 = self.dial4.value()
        self.dial4.setRange(0,100)
        self.dial_label4.setText(
            f'dB: {str(value4)}')
        self.dial_label4.move(
            330,250)
        self.dial_label4.adjustSize()
def clickedBtn():
    print("Clicked")
