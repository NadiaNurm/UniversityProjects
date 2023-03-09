field = [[' ', ' ', ' '], #создали пустую матрицу
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

def printField():  #печатаем матрицу
    print(field[0])
    print(field[1])
    print(field[2])

def get_input(counter):  #получаем значение ячейки, в которую хотим поставить Х или О, и номер хода
    figure = 'X' # первый ходит Х - нечетный ход
    if counter % 2 == 0: # если ход четный, то ходит О
        figure = 'O'
    try:
        a = int(input("Куда хотите поставить {}? Введите номер строки ".format(figure)))
        b = int(input("Куда хотите поставить {}? Введите номер столбца ".format(figure)))
        while not(0 < a < 4) or not(0 < b < 4):
            print("Нет такой строки или столбца")
            a = int(input("Куда хотите поставить {}? Введите номер строки ".format(figure)))
            b = int(input("Куда хотите поставить {}? Введите номер столбца ".format(figure)))
        return a,b
    except:
        print('Некорректный ввод') # если ввод некорректный, то начинаем вводить заново
        return get_input(counter)

def replaceX(a,b): #заменяем пустое поле на Х
    global field
    if field[a-1][b-1] == ' ':
        field[a-1][b-1] = 'X'
    else:
        print('Поле занято')
        return False
    printField()
    return True # если удалось заменить,то возвращается True

def replaceO(a,b): #заменяем пустое поле на О
    global field
    if field[a-1][b-1] == ' ' :
        field[a-1][b-1] = 'O'
    else:
        print('Поле занято')
        return False
    printField()
    return True # если удалось заменить,то возвращается True

def win():
    Xwin = False
    Owin = False
    field_T = [[],[],[]] # меняем строики и столбцы местами, создаем транспонированную матрицу 
    field_diagonal = [[],[]] # матрица, в которую запишем диагонали
    for row in field: # забираем строку из field, если в строке три О или три Х, то это победа
        i = row.count('X') 
        j = row.count('O')
        if i == 3:
            Xwin = True
        if j == 3:
            Owin = True
        field_T[0].append(row[0]) #транспонируем матрицу и опять считаем количество О или Х
        field_T[1].append(row[1])
        field_T[2].append(row[2])
        for _ in field_T:
            k = _.count('X')
            m = _.count('O')
            if k == 3:
                Xwin = True
            if m == 3:
                Owin = True
    field_diagonal[0].append(field[0][0]) #записываем диагонали в первые две строки и опять считаем количество О или Х
    field_diagonal[0].append(field[1][1])
    field_diagonal[0].append(field[2][2])
    field_diagonal[1].append(field[0][2])
    field_diagonal[1].append(field[1][1])
    field_diagonal[1].append(field[2][0])
    for _ in field_diagonal:
            n = _.count('X')
            o = _.count('O')
            if n == 3:
                Xwin = True
            if o == 3:
                Owin = True
    return Xwin,Owin

def game(): #сама игра
    counter = 1 # для четность/нечетность, чтобы знать, какой фигурой ходим
    printField()
    Xwin = False
    Owin = False
    while Xwin != True and Owin != True: 
        a,b = get_input(counter)
        result = False 
        if counter % 2 != 0:
            result = replaceX(a,b)
        else:
            result = replaceO(a,b)
        if result: # проверяем, сделал ли игрок ход
            counter += 1      
        Xwin, Owin = win()
    if Xwin == True:
        print("X выиграл")
    else:
        print("O выиграл")
game()
