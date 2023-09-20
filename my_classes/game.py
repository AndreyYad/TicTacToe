from my_classes.image import TicTacToeImage
from os import system

class TicTacToe(object):

    PLAYERS = ['O', 'X']

    def __init__(self):
        self.gameboard = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.message = ''
        self.image = ''
        self.turn_text = 'Ходит X'
        self.turn = True
        self.win = False


    def play(self):
        while True:
            system('cls')
            print(self.get_image())
            self.num_reception(input('Ввод: '))
    
    def get_image(self):
        return TicTacToeImage(
            self.gameboard,
            self.message,
            self.turn_text
        )
    
    def num_reception(self, num: str):

        if num == 'e':
            quit()
        elif num == 'r':
            self.__init__()
            return
        elif self.win:
            return

        try:
            num = int(num)-1
        except ValueError:
            self.message = "Ввод должен быть в виде целого числа от 1 до 9!"
            return
        if not(0 <= num <= 8):
            self.message = "Ввод должен быть в виде целого числа от 1 до 9!"
        elif self.gameboard[num // 3][num % 3] != ' ':
            self.message = "Указаная Вами ячейка - занята!"
        else:
            self.gameboard[num // 3][num % 3] = self.PLAYERS[self.turn]
            if self.check_win():
                self.win = True
                self.message = f'{self.PLAYERS[self.turn]} победил!!! (e - выход, r - заново)'
                self.turn_text = ''
            else:
                self.turn = not self.turn
                self.turn_text = f'Ходит {self.PLAYERS[self.turn]}'
        
    def check_win(self):
        combinations_win = [
            [0, 4, 8],
            [2, 4, 6],
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6], 
            [1, 4, 7],
            [2, 5, 8]
        ]
        for combination in combinations_win:
            line = []
            for index in range(3):
                num = combination[index]
                line.append(self.gameboard[num // 3][num % 3])
            if sum([line.count(player) == 3 for player in ['X', 'O']]):
                return True
        return False