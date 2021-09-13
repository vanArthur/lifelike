import os
import random
from time import sleep
import LifeLike_color

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

class maze():

    def __init__(self, x, y, level, keyboardLayout):
        self.x = x
        self.y = y
        self.level = level
        self.location = [2,2]
        self.last = "O"
        self.lastMove = ""
        self.keyboardLayout = keyboardLayout

        self.grid = []
        self.path = []
        self.targets = []
        self.score = 0
        self.levelScore = 0

    def generateGrid(self):
        self.location = [2,2]
        self.last = "O"
        self.lastMove = ""

        self.grid = []
        self.path = []
        self.targets = []
        self.levelScore = 0

        for i in range(self.y):
            self.grid.append([])
            self.path.append([])
        for each in range(len(self.grid)):
            for i in range(self.x):
                self.grid[each].append(" ")
                self.path[each].append(" ")
        for i in range(self.level):
            while True:
                tx = random.randint(0,self.x - 1)
                ty = random.randint(0,self.y - 1)
                tco = [tx, ty]
                if tco == [2,2]:
                    if random.randint(0,1) == 0:
                        tco[0] + 1
                    else:
                        tco[1] + 1
                if tco in self.targets:
                    continue
                else:
                    self.targets.append(tco)
                    self.path[tco[1]][tco[0]] = "⦿"
                    self.grid[tco[1]][tco[0]] = "⦿"
                    break
        for i in range(self.level * 2):
            while True:
                ox = random.randint(0,self.x - 1)
                oy = random.randint(0,self.y - 1)
                oco = [ox, oy]
                if oco == [2,2]:
                    if random.randint(0,1) == 0:
                        oco[0] - 1
                    else:
                        oco[1] - 1
                if oco in self.targets:
                    continue
                else:
                    self.targets.append(oco)
                    self.grid[oco[1]][oco[0]] = "█"
                    self.path[oco[1]][oco[0]] = "█"
                    break

    def mazeGame(self):
        while True:
            self.grid[self.location[1]][self.location[0]] = ("╳")

            clear()
            print("┏", end="")
            print('━' * len(self.grid[0]), end="")
            print('┓')
            for cords,row in enumerate(self.grid):
                print("┃", end="")
                for co in row:
                    if co == "╳":
                        print(LifeLike_color.CYAN, co, LifeLike_color.END, end="", sep="")
                    elif co == "⦿":
                        print(LifeLike_color.RED, co, LifeLike_color.END, end="", sep="")
                    else:print(co, end="")
                print("┃", cords)
            print("┗", end="")
            print("━" * len(self.grid[0]), end="")
            print("┛")
            print(" ", end="")
            for i in range(self.x):
                if i % 5 == 0:
                    print("^", "    ", end="", sep="")
            print("")
            print(" ", end="")
            for i in range(self.x):
                if i % 5 == 0:
                    if i > 9:
                        print(i, "   ", end="", sep="")
                    else:
                        print(i, "    ", end="", sep="")
            print("")

            print(self.location)
            print("")
            print("Score: ", self.score)
            print("levelScore: ", self.levelScore)
            p_input = input("Make your move!")
            if p_input in ("stop", "end", "quit", "exit"):
                return
            for each in p_input:
                self.grid[self.location[1]][self.location[0]] = self.last
                self.path[self.location[1]][self.location[0]] = self.last
                if each == self.keyboardLayout[0] and self.location[1] != 0:
                    self.last = "║"
                    self.location[1] -= 1
                elif each == self.keyboardLayout[2] and self.location[1] != len(self.grid) - 1:
                    self.last = "║"
                    self.location[1] += 1
                elif each == self.keyboardLayout[3] and self.location[0] != len(self.grid[0]) - 1:
                    self.last = "═"
                    self.location[0] += 1
                elif each == self.keyboardLayout[1] and self.location[0] != 0:
                    self.last = "═"
                    self.location[0] -= 1
                else:
                    return

                if self.lastMove == "s" and each == "d":
                    self.grid[self.location[1]][(self.location[0] - 1)] = "╚"
                elif self.lastMove == "s" and each == "q":
                    self.grid[self.location[1]][(self.location[0] + 1)] = "╝"
                elif self.lastMove == "z" and each == "d":
                    self.grid[self.location[1]][(self.location[0] - 1)] = "╔"
                elif self.lastMove == "z" and each == "q":
                    self.grid[self.location[1]][(self.location[0] + 1)] = "╗"
                elif self.lastMove == "q" and each == "z":
                    self.grid[(self.location[1] + 1)][(self.location[0])] = "╚"
                elif self.lastMove == "q" and each == "s":
                    self.grid[(self.location[1] - 1)][(self.location[0])] = "╔"
                elif self.lastMove == "d" and each == "z":
                    self.grid[(self.location[1] + 1)][(self.location[0])] = "╝"
                elif self.lastMove == "d" and each == "s":
                    self.grid[(self.location[1] - 1)][(self.location[0])] = "╗"
                self.lastMove = each

                if self.path[(self.location[1])][(self.location[0])] in ("║","═","╚","╝","╔","╗", "█"):
                    for _ in range(10):
                        print("You Died!")
                    sleep(3)
                    clear()
                    return
                if self.path[(self.location[1])][(self.location[0])] == "⦿":
                    self.score += 1
                    self.levelScore += 1

                if self.levelScore == self.level:
                    self.level += 5
                    clear()
                    self.generateGrid()
