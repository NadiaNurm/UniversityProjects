import random

field = [[' ', ' ', ' ', ' '], #создали пустую матрицу
         [' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ']]


def printField():  #печатаем матрицу
    for row in field:
        output_string = '|'
        for cell in row:
            output_string += cell.zfill(2) + '|' # мы выводим поле с рамкой и разделителями, а также добавляем 0 для выравнивания
        print(output_string)

def check_cell(cell): # когда мы записываем рандомные цифры в поле, мы должны проверить, чтобы они не повторялись
    for row in field:
        if str(cell) in row:
            return True
    return False

def field_random(): # заполняем ячейки цифрами от 1 до 16
    global field
    for i,row in enumerate(field): # добавляем счетчик к итерации, берем строку
        for j in range(len(row)): # проходим по всем элементам в строке
            cell = random.randint(1,16)
            while check_cell(cell):
                cell = random.randint(1,16)
            field[i][j] = str(cell)
    for i,row in enumerate(field):
        for j,cell in enumerate(row):
            if cell == '16': # т.к. у нас есть еще элемент 16, его надо заменить на пустое место
                field[i][j] = '  '
                return

def find_cell(input_cell): # ищем номер нужной нам ячейки по введенному числу, которое хотим передвинуть
    for i,row in enumerate(field):
        for j,cell in enumerate(row):
            if cell == input_cell:
                return i,j
    return

def check_win(): # проверяем выигрыш
    win_string = '123456789101112131415  ' # мы выиграем, если у нас будет набор чисел последовательно от 0 до 15
    current_string = ''
    for row in field:
        for cell in row:
            current_string += cell # заполняем переменную значениями из матрицы, которые у нас есть в текущий момент
    if current_string == win_string: # сравниваем их с нужной для выигрыша строкой
        return True
    else:
        return False


# поскольку играть в игру долго, создаем поле просто для проверки, корректно ли программа определяет момент выигрыша. 
def field_debug():
    global field
    field2 = [['1', '2', '3', '4'], #создали матрицу, для которой нужно сделать лишь несколько шагов
         ['5', '6', '7', '8'],
         ['9', '10', '15', '11'],
         ['13', '14', '  ', '12']]
    field = field2


def game():
    #field_debug()
    field_random()
    printField()
    win = check_win()
    while not(win):
        number = input('Какое число хотите передвинуть? ')
        direction = input('Куда хотите передвинуть? \n влево - A, вправо - D, вверх - W, вниз - S ')
        try:
            i,j = find_cell(number) # нашли номер ячейки, в которой находится число, которое мы ввели в консоли
        except:
            print('Неправильно введен номер')
            continue
        target_i = i
        target_j = j
        if direction in ['A','a','ф','Ф']: # если мы хотим сдвинуть влево, то строка остается неизменной, а столбец меняем на предыдущий
            target_j -= 1
        elif direction in ['W','w','ц','Ц']: # если мы хотим сдвинуть вверх, то столбец остается неизменным, а строку меняем на предыдущую
            target_i -= 1
        elif direction in ['S','s','Ы','ы']: # если мы хотим сдвинуть вниз, то столбец остается неизменным, а строку меняем на следующую
            target_i += 1
        elif direction in ['D','d','В','в']: # если мы хотим сдвинуть вправо, то строка остается неизменной, а столбец меняем на следующий
            target_j += 1
        else:
            print('Неправильно выбрано направление')
            continue
        try:
            if field[target_i][target_j] == '  ': # проверяем, чтобы в ячейке, куда мы хотим сдвинуть число, было пустое поле
                field[target_i][target_j] = field[i][j] # меняем местами пустое поле и число
                field[i][j] = '  '
                printField()
                win = check_win()
            else:
                print('Можно переводить только в пустое поле')
                continue
        except:
            print('Нельзя выходить за границы поля')
    print('Вы выиграли!')


game()

            