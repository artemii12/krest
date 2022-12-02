import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.pols = [0, 0, 0,
                     0, 0, 0,
                     0, 0, 0]

    def init_ui(self):
        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle('крест')

        self.comanda = False
        self.winner = False

        self.btn1 = QPushButton('', self)
        self.btn1.resize(50, 50)
        self.btn1.move(20, 20)
        self.btn1.setStyleSheet('QPushButton {background-color: #DBE2EF}')
        self.btn1.setFont(QFont('Arial', 40))
        self.btn1.clicked.connect(self.count1)

        self.btn2 = QPushButton('', self)
        self.btn2.resize(50, 50)
        self.btn2.move(70, 20)
        self.btn2.setStyleSheet('QPushButton {background-color: #DBE2EF}')
        self.btn2.setFont(QFont('Arial', 40))
        self.btn2.clicked.connect(self.count2)

        self.btn3 = QPushButton('', self)
        self.btn3.resize(50, 50)
        self.btn3.move(120, 20)
        self.btn3.setStyleSheet('QPushButton {background-color: #DBE2EF}')
        self.btn3.setFont(QFont('Arial', 40))
        self.btn3.clicked.connect(self.count3)

        self.btn4 = QPushButton('', self)
        self.btn4.resize(50, 50)
        self.btn4.move(20, 70)
        self.btn4.setStyleSheet('QPushButton {background-color: #DBE2EF}')
        self.btn4.setFont(QFont('Arial', 40))
        self.btn4.clicked.connect(self.count4)

        self.btn5 = QPushButton('', self)
        self.btn5.resize(50, 50)
        self.btn5.move(70, 70)
        self.btn5.setStyleSheet('QPushButton {background-color: #DBE2EF}')
        self.btn5.setFont(QFont('Arial', 40))
        self.btn5.clicked.connect(self.count5)

        self.btn6 = QPushButton('', self)
        self.btn6.resize(50, 50)
        self.btn6.move(120, 70)
        self.btn6.setStyleSheet('QPushButton {background-color: #DBE2EF}')
        self.btn6.setFont(QFont('Arial', 40))
        self.btn6.clicked.connect(self.count6)

        self.btn7 = QPushButton('', self)
        self.btn7.resize(50, 50)
        self.btn7.move(20, 120)
        self.btn7.setStyleSheet('QPushButton {background-color: #DBE2EF}')
        self.btn7.setFont(QFont('Arial', 40))
        self.btn7.clicked.connect(self.count7)

        self.btn8 = QPushButton('', self)
        self.btn8.resize(50, 50)
        self.btn8.move(70, 120)
        self.btn8.setStyleSheet('QPushButton {background-color: #DBE2EF}')
        self.btn8.setFont(QFont('Arial', 40))
        self.btn8.clicked.connect(self.count8)

        self.btn9 = QPushButton('', self)
        self.btn9.resize(50, 50)
        self.btn9.move(120, 120)
        self.btn9.setStyleSheet('QPushButton {background-color: #DBE2EF}')
        self.btn9.setFont(QFont('Arial', 40))
        self.btn9.clicked.connect(self.count9)

        self.lbl = QLabel(self)
        self.lbl.setText('ход: ╳')
        self.lbl.move(30, -5)
        self.winb = QLabel(self)
        self.winb.setText('')
        self.winb.setStyleSheet('QPushButton {background-color: #DBE2EF}')
        self.winb.setFont(QFont('Arial', 11))
        self.winb.move(75, -5)

        self.btn = QPushButton('Новая игра', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(60, 170)
        self.btn.clicked.connect(self.newu)

    def newu(self):
        self.pols = [0, 0, 0,
                     0, 0, 0,
                     0, 0, 0]
        self.winb.setText('')
        self.btn1.setText('')
        self.btn2.setText('')
        self.btn3.setText('')
        self.btn4.setText('')
        self.btn5.setText('')
        self.btn6.setText('')
        self.btn7.setText('')
        self.btn8.setText('')
        self.btn9.setText('')

    def update(self):
        print(self.pols)
        if self.pols[0] == 1 and self.pols[1] == 1 and self.pols[2] == 1:
            self.winb.setText('ВЫЙГРАЛ: X')
        elif self.pols[3] == 1 and self.pols[4] == 1 and self.pols[5] == 1:
            self.winb.setText('ВЫЙГРАЛ: X')
        elif self.pols[6] == 1 and self.pols[7] == 1 and self.pols[8] == 1:
            self.winb.setText('ВЫЙГРАЛ: X')
        elif self.pols[0] == 1 and self.pols[3] == 1 and self.pols[6] == 1:
            self.winb.setText('ВЫЙГРАЛ: X')
        elif self.pols[1] == 1 and self.pols[4] == 1 and self.pols[7] == 1:
            self.winb.setText('ВЫЙГРАЛ: X')
        elif self.pols[2] == 1 and self.pols[5] == 1 and self.pols[8] == 1:
            self.winb.setText('ВЫЙГРАЛ: X')
        elif self.pols[0] == 1 and self.pols[4] == 1 and self.pols[8] == 1:
            self.winb.setText('ВЫЙГРАЛ: X')
        elif self.pols[2] == 1 and self.pols[4] == 1 and self.pols[6] == 1:
            self.winb.setText('ВЫЙГРАЛ: X')

        if self.pols[0] == 2 and self.pols[1] == 2 and self.pols[2] == 2:
            self.winb.setText('ВЫЙГРАЛ: ○')
        elif self.pols[3] == 2 and self.pols[4] == 2 and self.pols[5] == 2:
            self.winb.setText('ВЫЙГРАЛ: ○')
        elif self.pols[6] == 2 and self.pols[7] == 2 and self.pols[8] == 2:
            self.winb.setText('ВЫЙГРАЛ: ○')
        elif self.pols[0] == 2 and self.pols[3] == 2 and self.pols[6] == 2:
            self.winb.setText('ВЫЙГРАЛ: ○')
        elif self.pols[1] == 2 and self.pols[4] == 2 and self.pols[7] == 2:
            self.winb.setText('ВЫЙГРАЛ: ○')
        elif self.pols[2] == 2 and self.pols[5] == 2 and self.pols[8] == 2:
            self.winb.setText('ВЫЙГРАЛ: ○')
        elif self.pols[0] == 2 and self.pols[4] == 2 and self.pols[8] == 2:
            self.winb.setText('ВЫЙГРАЛ: ○')
        elif self.pols[2] == 2 and self.pols[4] == 2 and self.pols[6] == 2:
            self.winb.setText('ВЫЙГРАЛ: ○')

        if not self.comanda:
            self.lbl.setText('ход: ○')
        if self.comanda:
            self.lbl.setText('ход: ╳')

    def count1(self):
        if not self.comanda:
            self.pols[0] = 1
            self.btn1.setText('╳')
            self.update()
        else:
            self.pols[0] = 2
            self.btn1.setText('○')
            self.update()
        if self.comanda:
            self.comanda = False
        else:
            self.comanda = True

    def count2(self):
        if not self.comanda:
            self.pols[1] = 1
            self.btn2.setText('╳')
            self.update()
        else:
            self.pols[1] = 2
            self.btn2.setText('○')
            self.update()
        if self.comanda:
            self.comanda = False
        else:
            self.comanda = True

    def count3(self):
        if not self.comanda:
            self.pols[2] = 1
            self.btn3.setText('╳')
            self.update()
        else:
            self.pols[2] = 2
            self.btn3.setText('○')
            self.update()
        if self.comanda:
            self.comanda = False
        else:
            self.comanda = True

    def count4(self):
        if not self.comanda:
            self.pols[3] = 1
            self.btn4.setText('╳')
            self.update()
        else:
            self.pols[3] = 2
            self.btn4.setText('○')
            self.update()
        if self.comanda:
            self.comanda = False
        else:
            self.comanda = True

    def count5(self):
        if not self.comanda:
            self.pols[4] = 1
            self.btn5.setText('╳')
            self.update()
        else:
            self.pols[4] = 2
            self.btn5.setText('○')
            self.update()
        if self.comanda:
            self.comanda = False
        else:
            self.comanda = True

    def count6(self):
        if not self.comanda:
            self.pols[5] = 1
            self.btn6.setText('╳')
            self.update()
        else:
            self.pols[5] = 2
            self.btn6.setText('○')
            self.update()
        if self.comanda:
            self.comanda = False
        else:
            self.comanda = True

    def count7(self):
        if not self.comanda:
            self.pols[6] = 1
            self.btn7.setText('╳')
            self.update()
        else:
            self.pols[6] = 2
            self.btn7.setText('○')
            self.update()
        if self.comanda:
            self.comanda = False
        else:
            self.comanda = True

    def count8(self):
        if not self.comanda:
            self.pols[7] = 1
            self.btn8.setText('╳')
            self.update()
        else:
            self.pols[7] = 2
            self.btn8.setText('○')
            self.update()
        if self.comanda:
            self.comanda = False
        else:
            self.comanda = True

    def count9(self):
        if not self.comanda:
            self.pols[8] = 1
            self.btn9.setText('╳')
            self.update()
        else:
            self.pols[8] = 2
            self.btn9.setText('○')
            self.update()

        if self.comanda:
            self.comanda = False
        else:
            self.comanda = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Example()
    window.show()
    app.exec()
