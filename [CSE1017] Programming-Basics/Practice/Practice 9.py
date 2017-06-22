# Sliding Puzzle
import random

class Reader :
    @staticmethod
    def get_number(size) :
        num = input("Type the number you want to move (Type 0 to quit): ")
        while not (num.isdigit() and 0 <= int(num) <= size * size - 1) :
            num = input("Type the number you want to move (Type 0 to quit): ")
        return int(num)

class SlidingBoard :
    def __init__(self, size) :
        self.__board = SlidingBoard.create_board(SlidingBoard.create_init_board(size))
        self.__empty = self.find_position(0)

    @property
    def board(self) :
        return self.__board

    @staticmethod
    def create_board(numbers) :
        board = []
        for r in range(4) :
            k = r * 4
            row = numbers[k:k+4]
            board.append(numbers[k:k+4])
        return board

    @staticmethod
    def create_init_board(size) :
        numbers = [n for n in range(size * size)]
        random.shuffle(numbers)
        return numbers

    @staticmethod
    def create_goal_board(size) :
        numbers = [n for n in range(size * size)]
        numbers[-1] = 0
        return numbers

    def find_position(self, num) :
        for i in range(len(self.__board)) :
            for j in range(len(self.__board)) :
                if num == self.__board[i][j] :
                    return(i, j)

    def move(self, pos) :
        (x,y) = pos
        if self.__empty in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)) :
            self.__board[self.__empty[0]][self.__empty[1]] = self.__board[x][y]
            self.__board[x][y] = 0
            self.__empty = pos
        else:
            print("Can't move! Try again.")

    def print_board(self) :
        print("S |  0  1  2  3")
        print("- + -----------")
        i = 0
        for row in self.__board :
            print(i, "|", end = ' ')
            for item in row :
                if item == 0:
                    print("  ", end = " ")
                elif 10 <= item <= 15 :
                    print(item,end = " ")
                else :
                    print(str(item).rjust(2),end=" ")
            print()
            i += 1

class SlidingPuzzleController() :
    def __init__(self, size) :
        self.__slider = SlidingBoard(size)
        self.__goal = SlidingBoard.create_board(SlidingBoard.create_goal_board(size))
        self.__size = size

    def play(self) :
        while True:
            self.__slider.print_board()
            if self.__slider.board == self.__goal :
                print("Congratulations!")
                break
            num = Reader.get_number(self.__size) # get number between 0 and 15
            if num == 0 :
                break
            pos = self.__slider.find_position(num)
            self.__slider.move(pos)
        print("Please come again.")

def main() :
    import sys
    size = sys.argv[1]
    if size.isdigit() and int(size) > 1 :
        SlidingPuzzleController(int(size)).play()
    else :
        print("Not aproper system argument.")

main()