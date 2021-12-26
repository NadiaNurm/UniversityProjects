from PyQt5 import QtCore,QtGui,QtWidgets
import design
import sys
from enum import Enum

class State(Enum):
    empty = 0
    cross = 1
    circle = 2



class Main_App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    crossImg = ':/img/cross.png'
    circleImg = ':/img/circle.png'
    emptyImg = ':/img/empty.png'
    crossWinImg = ':/img/cross_win.png'
    circleWinImg = ':/img/circle_win.png'
    counter = 1

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.labelX1Y1.clicked.connect(self.setImage)
        self.labelX2Y1.clicked.connect(self.setImage)
        self.labelX3Y1.clicked.connect(self.setImage)
        self.labelX1Y2.clicked.connect(self.setImage)
        self.labelX2Y2.clicked.connect(self.setImage)
        self.labelX3Y2.clicked.connect(self.setImage)
        self.labelX1Y3.clicked.connect(self.setImage)
        self.labelX2Y3.clicked.connect(self.setImage)
        self.labelX3Y3.clicked.connect(self.setImage)

        self.field = [
                        [self.labelX1Y1,self.labelX2Y1,self.labelX3Y1],
                        [self.labelX1Y2,self.labelX2Y2,self.labelX3Y2],
                        [self.labelX1Y3,self.labelX2Y3,self.labelX3Y3]]
        self.setLabelAttr()

    def setLabelAttr(self):
        for row in self.field:
            for label in row:
                setattr(label,'state', State.empty)

    
    def setImage(self):
        sender = self.sender()
        if sender.state != State.empty:
            return
        if self.counter % 2 != 0:
            sender.setPixmap(QtGui.QPixmap(self.crossImg))
            sender.state = State.cross
        else:
            sender.setPixmap(QtGui.QPixmap(self.circleImg))
            sender.state = State.circle
        self.counter += 1
        self.checkWin()

    def checkWin(self):
        Xwin = False
        Owin = False
        for row in self.field:
            Xwin = True
            for label in row:
                if label.state != State.cross:
                    Xwin = False
                    break
            Owin = True
            for label in row:
                if label.state != State.circle:
                    Owin = False
                    break
            if Xwin:
                for label in row:
                    label.setPixmap(QtGui.QPixmap(self.crossWinImg))
            if Owin:
                for label in row:
                    label.setPixmap(QtGui.QPixmap(self.circleWinImg))
                

    #def win():
    #    Xwin = False
    #    Owin = False
    #    field_T = [[],[],[]] # меняем строики и столбцы местами, создаем транспонированную матрицу 
    #    field_diagonal = [[],[]] # матрица, в которую запишем диагонали
    #    for row in field: # забираем строку из field, если в строке три О или три Х, то это победа
    #        i = row.count('X') 
    #        j = row.count('O')
    #        if i == 3:
    #            Xwin = True
    #        if j == 3:
    #            Owin = True
    #        field_T[0].append(row[0]) #транспонируем матрицу и опять считаем количество О или Х
    #        field_T[1].append(row[1])
    #        field_T[2].append(row[2])
    #        for _ in field_T:
    #            k = _.count('X')
    #            m = _.count('O')
    #            if k == 3:
    #                Xwin = True
    #            if m == 3:
    #                Owin = True
    #    field_diagonal[0].append(field[0][0]) #записываем диагонали в первые две строки и опять считаем количество О или Х
    #    field_diagonal[0].append(field[1][1])
    #    field_diagonal[0].append(field[2][2])
    #    field_diagonal[1].append(field[0][2])
    #    field_diagonal[1].append(field[1][1])
    #    field_diagonal[1].append(field[2][0])
    #    for _ in field_diagonal:
    #            n = _.count('X')
    #            o = _.count('O')
    #            if n == 3:
    #                Xwin = True
    #            if o == 3:
    #                Owin = True
    #    return Xwin,Owin

        
        
 

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main_App()
    window.show()
    return app.exec_()

if __name__ == '__main__':
    main()

