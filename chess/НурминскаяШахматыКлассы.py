from enum import Enum
import colorama
from colorama import Fore,Back,Style
colorama.init()

field = [[' ', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', ' ', ' ', ], #создали пустую матрицу
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],     
         ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ], #i - строка, j - столбец      
         ['7', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '7', ],
         ['6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '6', ],
         ['5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '5', ],
         ['4', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '4', ],
         ['3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '3', ],
         ['2', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '2', ],
         ['1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
         [' ', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', ' ', ' ' ]]

board = [[None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None],]      

class Color(Enum):
    Black = 1
    White = -1
    Empty = 0



dict_field = {
    'a1': (9, 2), 'b1': (9, 3), 'c1': (9, 4), 'd1': (9, 5), 'e1': (9, 6), 'f1': (9, 7), 'g1': (9, 8), 'h1': (9, 9),'a2': (8, 2), 'b2': (8, 3), 'c2': (8, 4), 
    'd2': (8, 5), 'e2': (8, 6), 'f2': (8, 7), 'g2': (8, 8), 'h2': (8, 9), 'a3': (7, 2), 'b3': (7, 3), 'c3': (7, 4),'d3': (7, 5), 'e3': (7, 6), 'f3': (7, 7),
    'g3': (7, 8), 'h3': (7, 9), 'a4': (6, 2), 'b4': (6, 3), 'c4': (6, 4), 'd4': (6, 5), 'e4': (6, 6), 'f4': (6, 7),'g4': (6, 8), 'h4': (6, 9), 'a5': (5, 2), 
    'b5': (5, 3), 'c5': (5, 4), 'd5': (5, 5), 'e5': (5, 6), 'f5': (5, 7), 'g5': (5, 8), 'h5': (5, 9), 'a6': (4, 2),'b6': (4, 3), 'c6': (4, 4), 'd6': (4, 5),
    'e6': (4, 6), 'f6': (4, 7), 'g6': (4, 8), 'h6': (4, 9), 'a7': (3, 2), 'b7': (3, 3), 'c7': (3, 4), 'd7': (3, 5),'e7': (3, 6), 'f7': (3, 7), 'g7': (3, 8),
    'h7': (3, 9), 'a8': (2, 2), 'b8': (2, 3), 'c8': (2, 4), 'd8': (2, 5), 'e8': (2, 6), 'f8': (2, 7), 'g8': (2, 8),'h8': (2, 9)
    }



class Figure:
    def __init__(self, color, current_i, current_j):
        self.owner_color  = color 
        self.owner_current_i = current_i
        self.owner_current_j = current_j

    def get_color(self):
        return self.owner_color

class Black_Pawn(Figure):
    def check_moves(self, i, j):
        if board[i][j] == None and (self.owner_current_j == j):
            if (i - self.owner_current_i == 2):
                if (self.owner_current_i == 1) and board[i-1][j] == None:
                    return True
                    #field[i][j] = '♙'
            elif i - self.owner_current_i == 1:
                    return True
        else:
            return False

    def check_attack(self, i, j):
        if board[i][j] == None:
            return False
        if board[i][j].get_color() != self.get_color():
            if self.owner_current_j == j:
                return False
            if (i == self.owner_current_i + 1) and (j == self.owner_current_j + 1 or j == self.owner_current_j - 1):
                return True
        else:
            return False
         
class White_Pawn(Figure):        
    def check_moves(self, i, j):
        if board[i][j] == None and (self.owner_current_j == j):
            if (i - self.owner_current_i == -2):
                if (self.owner_current_i == 6) and board[i-1][j] == None:
                    return True
                    #field[i][j] = '♙'
            elif i - self.owner_current_i == -1:
                    return True
        else:
            return False

    def check_attack(self, i, j):
        if board[i][j] == None:
            return False
        if board[i][j].get_color() != self.get_color():
            if self.owner_current_j == j:
                return False
            if (i == self.owner_current_i - 1) and (j == self.owner_current_j + 1 or j == self.owner_current_j - 1):
                return True
        else:
            return False
    
                
#Rook - ладья
class Rook(Figure):
    def check_way(self,i,j):    
        if i == self.owner_current_i: #ходим вправо или влево
            if self.owner_current_j < j:
                for col in (self.owner_current_j + 1, j):
                    if board[i][col] != None:
                        return False
                return True
            elif self.owner_current_j > j:
                for col in (j, self.owner_current_j - 1):
                    if board[i][col] != None :
                        return False
                return True
        elif j == self.owner_current_j: #ходим вниз или вверх
            if self.owner_current_i < i:
                for row in (self.owner_current_i + 1, i):
                    if board[row][j] != None:
                        return False
                return True
            elif self.owner_current_i > i:
                for row in (i, self.owner_current_i - 1):
                    if board[row][j] != None :
                        return False
                return True
    
    def check_moves(self,i,j):
        if board[i][j] != None:
            return False
        elif self.check_way(i,j):
            return True
        else:
            return False
    
    def check_attack(self,i,j):
        if board[i][j] == None:
            return False
        if board[i][j].get_color() != self.get_color() and self.check_way(i,j):
            return True
        return False


# Knight - конь
class Knight(Figure):
    def check_moves(self, i, j):
        d_row = abs(self.owner_current_i - i)
        d_col = abs(self.owner_current_j - j)
        if ((d_row == 1 and d_col == 2) or (d_row == 2 and d_col == 1)) and board[i][j] == None:
            return True
        return False

    def check_attack(self, i, j):
        if board[i][j] == None:
            return False
        d_row = abs(self.owner_current_i - i)
        d_col = abs(self.owner_current_j - j)
        if (d_row == 1 and d_col == 2) or (d_row == 2 and d_col == 1):
            if board[i][j].get_color() != self.get_color():
                return True  
        return False  

# Bishop - слон
class Bishop(Figure):
    def check_way(self,i,j):
        def go_up(num):
            return num + 1
        def go_down(num):
            return num - 1    
        d_row = abs(self.owner_current_i - i)
        d_col = abs(self.owner_current_j - j)
        if d_row != d_col:
            return False
        if i > self.owner_current_i:
            i_mod = go_up
        else:
            i_mod = go_down
        if j > self.owner_current_j:
            j_mod = go_up
        else:
            j_mod = go_down  
        target_i = self.owner_current_i
        target_j = self.owner_current_j      
        for m in range(d_row-1):
            target_i = i_mod(target_i)
            target_j = j_mod(target_j)
            if board[target_i][target_j] != None:
                return False
        return True
    
    def check_moves(self,i,j):
        if board[i][j] != None:
            return False
        elif self.check_way(i,j):
            return True
        else:
            return False
    
    def check_attack(self,i,j):
        if board[i][j] == None:
            return False
        if board[i][j].get_color() != self.get_color() and self.check_way(i,j):
            return True
        return False


# Queen - Ферзь 
class Queen(Figure):
    def check_way(self,i,j):
        if Rook.check_way(self,i,j) or Bishop.check_way(self,i,j):
            return True
        return False  

    def check_moves(self,i,j):
        if board[i][j] != None:
            return False
        elif self.check_way(i,j):
            return True
        else:
            return False

    def check_attack(self,i,j):
        if board[i][j] == None:
            return False
        if board[i][j].get_color() != self.get_color() and self.check_way(i,j):
            return True
        return False


                
# King-король
class King(Figure):
    def check_way(self,i,j):
        if abs(self.owner_current_i - i) > 1 and abs(self.owner_current_j - j) > 1:
            return False
        if Rook.check_way(self,i,j) or Bishop.check_way(self,i,j):
            return True
        return False  

    def check_moves(self,i,j):
        if board[i][j] != None:
            return False
        elif self.check_way(i,j):
            return True
        else:
            return False

    def check_attack(self,i,j):
        if board[i][j] == None:
            return False
        if board[i][j].get_color() != self.get_color() and self.check_way(i,j):
            return True
        return False

#пешка ходит только по диагонали
class Catapult(Figure):
    def check_way(self,i,j):
        if abs(self.owner_current_i - i) == 1 and abs(self.owner_current_j - j) == 1:
            return True
        return False

    def check_moves(self,i,j):
        if board[i][j] != None:
            return False
        elif self.check_way(i,j):
            return True
        else:
            return False
    
    def check_attack(self,i,j):
        if board[i][j] == None:
            return False
        if board[i][j].get_color() != self.get_color() and self.check_way(i,j):
            return True
        return False


#Может ходить на любую точку, но бьет только по диагонали на одну клетку
class Spy(Figure):
    def check_way(self,i,j):
        if abs(self.owner_current_i - i) == 1 and abs(self.owner_current_j - j) == 1:
            return True
        return False

    def check_moves(self,i,j):
        if board[i][j] != None:
            return False
        return True
    
    def check_attack(self,i,j):
        if board[i][j] == None:
            return False
        if board[i][j].get_color() != self.get_color() and self.check_way(i,j):
            return True
        return False

#Фигура,расположенная в центре доски, может только атаковать противника, как конь 
class Trebuchet(Figure):
    def check_moves(self, i, j):
        return False

    def check_attack(self, i, j):
        if board[i][j] == None:
            return False
        d_row = abs(self.owner_current_i - i)
        d_col = abs(self.owner_current_j - j)
        if (d_row == 1 and d_col == 2) or (d_row == 2 and d_col == 1):
            if board[i][j].get_color() != self.get_color():
                return True  
        return False  



def board_to_field():
    global field, board
    for cell in dict_field.keys():
        i_field = dict_field[cell][0]
        j_field = dict_field[cell][1]
        i_board = i_field - 2
        j_board = j_field - 2
        if board[i_board][j_board] == None:
            field[i_field][j_field] = '.'
        elif isinstance(board[i_board][j_board], Black_Pawn):
            field[i_field][j_field] = 'p'
        elif isinstance(board[i_board][j_board], White_Pawn):
            field[i_field][j_field] = 'P'  
        elif isinstance(board[i_board][j_board], Rook) and board[i_board][j_board].get_color() == Color.Black:
            field[i_field][j_field] = 'r'   
        elif isinstance(board[i_board][j_board], Rook) and board[i_board][j_board].get_color() == Color.White:
            field[i_field][j_field] = 'R' 
        elif isinstance(board[i_board][j_board], Bishop) and board[i_board][j_board].get_color() == Color.Black:
            field[i_field][j_field] = 'b'   
        elif isinstance(board[i_board][j_board], Bishop) and board[i_board][j_board].get_color() == Color.White:
            field[i_field][j_field] = 'B'
        elif isinstance(board[i_board][j_board], Knight) and board[i_board][j_board].get_color() == Color.Black:
            field[i_field][j_field] = 'n'   
        elif isinstance(board[i_board][j_board], Knight) and board[i_board][j_board].get_color() == Color.White:
            field[i_field][j_field] = 'N'
        elif isinstance(board[i_board][j_board], Queen) and board[i_board][j_board].get_color() == Color.Black:
            field[i_field][j_field] = 'q'   
        elif isinstance(board[i_board][j_board], Queen) and board[i_board][j_board].get_color() == Color.White:
            field[i_field][j_field] = 'Q'
        elif isinstance(board[i_board][j_board], King) and board[i_board][j_board].get_color() == Color.Black:
            field[i_field][j_field] = 'k'   
        elif isinstance(board[i_board][j_board], King) and board[i_board][j_board].get_color() == Color.White:
            field[i_field][j_field] = 'K'
        elif isinstance(board[i_board][j_board], Catapult) and board[i_board][j_board].get_color() == Color.Black:
            field[i_field][j_field] = 'c'   
        elif isinstance(board[i_board][j_board], Catapult) and board[i_board][j_board].get_color() == Color.White:
            field[i_field][j_field] = 'C'    
        elif isinstance(board[i_board][j_board], Spy) and board[i_board][j_board].get_color() == Color.Black:
            field[i_field][j_field] = 's'   
        elif isinstance(board[i_board][j_board], Spy) and board[i_board][j_board].get_color() == Color.White:
            field[i_field][j_field] = 'S'
        elif isinstance(board[i_board][j_board], Trebuchet) and board[i_board][j_board].get_color() == Color.Black:
            field[i_field][j_field] = 't'   
        elif isinstance(board[i_board][j_board], Trebuchet) and board[i_board][j_board].get_color() == Color.White:
            field[i_field][j_field] = 'T'    
#
def create_board():
    global board
    i = 1
    for j in range(0,8,2):
        board[i][j] = Black_Pawn(Color.Black,i,j)
        board[i][j+1] = Catapult(Color.Black,i,j)
    i = 6
    for j in range(0,8,2):
        board[i][j] = White_Pawn(Color.White,i,j)
        board[i][j+1] = Catapult(Color.White,i,j)
    board[0][0] = Rook(Color.Black, 0, 0)
    board[0][7] = Rook(Color.Black, 0, 7)
    board[7][0] = Rook(Color.White, 7, 0)
    board[0][7] = Spy(Color.Black, 0, 7)
    board[7][0] = Spy(Color.White, 7, 0)
    board[7][7] = Rook(Color.White, 7, 7)
    board[0][1] = Knight(Color.Black, 0, 1)
    board[0][6] = Knight(Color.Black, 0, 6)
    board[7][1] = Knight(Color.White, 7, 1)
    board[7][6] = Knight(Color.White, 7, 6)
    board[0][2] = Bishop(Color.Black, 0, 2)
    board[0][5] = Bishop(Color.Black, 0, 5)
    board[7][2] = Bishop(Color.White, 7, 2)
    board[7][5] = Bishop(Color.White, 7, 5)
    board[0][3] = Queen(Color.Black, 0, 3)
    board[0][4] = King(Color.Black, 0, 4)
    board[7][3] = Queen(Color.White, 7, 3)
    board[7][4] = King(Color.White, 7, 4)
    board[4][7] = Trebuchet(Color.White, 4, 7)
    board[3][0] = Trebuchet(Color.Black, 3, 0)




def print_field():
    board_to_field()
    for i in range(12):
        print (' '.join(field[i]))

def move(coord1,coord2,color):
    current_i = dict_field[coord1][0] - 2
    current_j = dict_field[coord1][1] - 2
    i = dict_field[coord2][0] - 2
    j = dict_field[coord2][1] - 2
    if board[current_i][current_j] == None:
        print("На этом месте нет фигуры")
        return False
    if board[current_i][current_j].get_color() != color:
        print('Вы ходите вражеской фигурой')
        return False
    if board[current_i][current_j].check_moves(i,j) or board[current_i][current_j].check_attack(i,j):
        board[i][j] = board[current_i][current_j]
        board[current_i][current_j] = None
        board[i][j].owner_current_i = i
        board[i][j].owner_current_j = j
        return True
    else:
        print('Ход невозможен')
        return False

def figure_color(counter):
    color = ''
    if (counter % 2 != 0):
        color = 'белых' 
    else:
        color = 'черных'
    return color

def find_king(color):
    king_i = 0
    king_j = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if isinstance(board[i][j], King) and board[i][j].get_color() == color:
                king_i = i
                king_j = j
    return king_i,king_j

def check(color,x=None,y=None):
    if x is None or y is None:        
        king_i,king_j = find_king(color)
    else:
        king_i = x
        king_j = y
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == None:
                continue
            if board[i][j].get_color() != color and board[i][j].check_attack(king_i,king_j):
                return True,i,j
    return False, i, j

def coord_generator(king_i,king_j, attack_i,attack_j):
    if attack_i == king_i: #ходим вправо или влево
        if king_j < attack_j:
            for col in range(king_j + 1, attack_j):
                yield attack_i,col
        elif king_j > attack_j:
            for col in range(attack_j, king_j - 1):
                yield attack_i,col
    elif attack_j == king_j: #ходим вниз или вверх
        if king_i < attack_i:
            for row in range(king_i + 1, attack_i):
                yield row,attack_j
        elif king_i > attack_i:
            for row in range(attack_i, king_i - 1):
                yield row,attack_j
    else:
        def go_up(num):
            return num + 1
        def go_down(num):
            return num - 1    
        d_row = abs(king_i - attack_i)
        if king_i > attack_i:
            i_mod = go_up
        else:
            i_mod = go_down
        if king_j > attack_j:
            j_mod = go_up
        else:
            j_mod = go_down        
        target_i = attack_i
        target_j = attack_j
        for m in range(d_row-1):
            target_i = i_mod(target_i)
            target_j = j_mod(target_j)
            yield target_i,target_j



def mate(color,attack_i,attack_j):
    king_i,king_j = find_king(color)
    move = False
    for i in range(len(board)):
        for j in range(len(board)):
            king_move = board[king_i][king_j].check_moves(i,j)
            if king_move:
                board[i][j]=board[king_i][king_j]
                board[king_i][king_j] = None
                king_check = check(color,i,j)[0]
                if not king_check:
                    move = True
                board[king_i][king_j]=board[i][j]
                board[i][j] = None
    cover = False
    if not isinstance(board[attack_i][attack_j],Knight):
        for x,y in coord_generator(king_i,king_j, attack_i,attack_j):
            for i in range(len(board)):
                for j in range(len(board)):
                    if i ==1 and j==6:
                        print()
                    if board[i][j] == None:
                        continue
                    if board[i][j].get_color() == color and board[i][j].check_moves(x,y):
                        board[x][y] = board[i][j]
                        board[i][j] = None
                        if not check(color,king_i,king_j)[0]:
                            cover = True    
                        board[i][j]=board[x][y]
                        board[x][y] = None

    cont_attack = False
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == None:
                    continue
            if board[i][j].get_color() == color and board[i][j].check_attack(attack_i,attack_j):
                    attacker = board[attack_i][attack_j]
                    board[attack_i][attack_j] = board[i][j]
                    if not check(color,king_i,king_j)[0]:
                        cont_attack = True    
                    board[i][j] = board[attack_i][attack_j]
                    board[attack_i][attack_j] = attacker
    if move or cover or cont_attack:
        return False
    return True            

def help(x_coord,y_coord):
    board_to_field()
    figure = board[x_coord][y_coord]
    for i in range(12):
        for j in range(12):
            if i == x_coord+2 and j == y_coord+2:
                print(Fore.GREEN + field[i][j]+Style.RESET_ALL, end = ' ')
                continue
            if (i<2) or (i>9) or (j<2) or (j>9):
                print(field[i][j], end = ' ')
                continue
            if figure.check_attack(i-2,j-2) or figure.check_moves(i-2,j-2):
                print(Back.GREEN + field[i][j]+Style.RESET_ALL, end = ' ')
                continue           
            print(field[i][j], end = ' ')
        print()


def game():
    def black_or_white_color(counter):
        if counter % 2 != 0:
            return Color.White
        else:
            return Color.Black 
    def black_or_white_str(counter):
        if counter % 2 != 0:
            return 'белых'
        else:
            return 'черных'
    counter = 1  
    create_board()
    print_field()
    win = False
    while not win:
        coord = []
        coord.append(input(f'Введите координаты фигуры {black_or_white_str(counter)}: ').lower())
        if coord[0] in dict_field:
            x_coord = dict_field[coord[0]][0] - 2
            y_coord = dict_field[coord[0]][1] - 2
            if board[x_coord][y_coord] is not None:
                if board[x_coord][y_coord].get_color() == black_or_white_color(counter):
                    help(x_coord,y_coord)
                else:
                    print('Неверно выбрана фигура')
                    continue
            else:
                print('Неверно выбрана фигура')
                continue
        else:
            print('Нет такой координаты')
            continue
        coord.append(input('Введите ход: ').lower())
        if move(coord[0],coord[1],black_or_white_color(counter)):
            print_field()
            counter += 1
            is_checked, attack_i, attack_j = check(black_or_white_color(counter))
            if is_checked:
                print(f'Королю {black_or_white_str(counter)} поставлен шах')    
                if board[attack_i][attack_j] != black_or_white_color(counter) and mate(black_or_white_color(counter),attack_i,attack_j):           
                    print(f'Королю {black_or_white_str(counter)} поставлен мат')
                    print('Игра закончена')
                    win = True
                     
        #print('Такой клетки не существует')    


#for i,x in coord_generator(0,4,3,7):
    #print(i,x)       
game()
#coord_generator(0,0,8,8)   
#create_board()
#print_field()
#move('e2', 'e4')
#print_field()
#move('d7','d5')
#print_field()
#move('e4','d5')
#print_field()