import time 
import math
from player import Human, Computer 

class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print ('|  ' + ' | '.join(row) + ' |')


    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|  ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, position in enumerate(self.board) if position == ' ']
            #alternative method 
            #moves = []
            #for (i, position) in enumerate(self.board):
                # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
                #if position == ' ':
                    #moves.append(i)
                #return moves
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True 
        return False

    def winner( self, square, letter):
        row_index = square // 3
        row = self.board[row_index + 1 : (row_index + 1) *3]
        if all([position == letter for position in row]):
            return True

        column_index = square %3
        column = [self.board[column_index+i*3] for i in range (3)]
        if all([position == letter for position in column]):
            return True 

        if square %2 == 0:
            diag1 = [self.board[i] for i in [0,4,8]]
            if all ([position == letter for position in diag1]):
                return True
            diag2 = [self.board[i] for i in [2,4,6]]
            if all([position == letter for position in diag2]):
                return True

        return False


def play(game, playerx, playero, print_game=True):
    if print_game:
        game.print_board_nums()
    letter = 'X' #declaring starting player

    while game.empty_squares():
        if letter == 'O':
            square = playero.get_move(game)
        else: 
            square = playerx.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f'makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print (letter + ' won!')
                return letter

            letter = 'O' if letter == 'X' else 'X'
        
        time.sleep(1.0)

    if print_game:
        print( "It's a tie!")

if __name__ == '__main__':
    playerx = Human('X')
    playero = Computer('O')
    t = TicTacToe()
    play(t, playerx, playero, print_game=True)



##########################

