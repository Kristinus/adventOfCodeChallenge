import sys
import numpy as np

class Board:
    def __init__(self, board):
        self.board = board
        self.marked = [[False] * 5] * 5
    
    def mark(self, num):
        for row in range(5):
            for col in range(5):
                if self.board[row][col] == num:
                    self.marked[row][col] = True
                    return self.isBingo(row, col)

    def isBingo(self, row, col):
        if all(self.marked[row]):
            return True
        if all(zip(*self.marked)[col]):
            return True
        return False
        

def part1(arr):
    boards = []
    nums = arr[0]
    
    return

def part2(arr):
    return

if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        arr = f.read().splitlines()

        print(part1(arr))
        print(part2(arr))
