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
        self.buttonNewGame.clicked.connect(self.resetField)
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
        Xwin, Owin = self.checkWin()
        if Xwin or Owin:
            for row in self.field:
                for label in row:
                    label.setEnabled(False)
            
            self.showMessage(Xwin,Owin)

    def checkWin(self):
        def check_field(field_list):
            for row in field_list:
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
                    return True,False
                if Owin:
                    for label in row:
                        label.setPixmap(QtGui.QPixmap(self.circleWinImg))
                    return False,True
            return False,False      
        
        Xwin, Owin = check_field(self.field) 
        if Xwin or Owin:
            return Xwin,Owin
        
        field_T = [[],[],[]]
        for i in range(3):
            for j in range(3):
                field_T[i].append(self.field[j][i])   

        Xwin, Owin = check_field(field_T) 
        if Xwin or Owin:
            return Xwin,Owin

        field_diagonal = [[],[]]
        field_diagonal[0].append(self.field[0][0]) #записываем диагонали в первые две строки и опять считаем количество О или Х
        field_diagonal[0].append(self.field[1][1])
        field_diagonal[0].append(self.field[2][2])
        field_diagonal[1].append(self.field[0][2])
        field_diagonal[1].append(self.field[1][1])
        field_diagonal[1].append(self.field[2][0])
        
        Xwin, Owin = check_field(field_diagonal) 
        if Xwin or Owin:
            return Xwin,Owin 
        
        return False,False

    def resetField(self):
        for row in self.field:
            for label in row:
                label.setEnabled(True)
                label.setPixmap(QtGui.QPixmap(self.emptyImg))
                label.state = State.empty
        self.counter = 1



    def showMessage(self,Xwin,Owin):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Победа!")
        message = 'Нолики'
        if Xwin:
            message = 'Крестики'
        msgBox.setText(f'Игра окончена! {message} победили!!!')
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        x = msgBox.exec_()
        
 

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main_App()
    window.show()
    return app.exec_()

if __name__ == '__main__':
    main()

