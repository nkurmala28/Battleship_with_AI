from Player import Player
from typing import Tuple
import random

class SearchDestroy(Player):

    def __init__(self,n: int,m: int,num: int,shiplist: dict,opponentshiplist: dict) -> None:
        super().__init__(n,m,num,shiplist,opponentshiplist)
        self.name = self.AIname()
        self.emptycoords = []
        for row in range(self.row):
            for col in range(self.column):
                self.emptycoords.append((row,col))
        self.mode = "search"
        self.destroycount = 0
        self.destroylocation = []
        self.destroyrow = 0
        self.destroycol = 0

    def AIname(self) -> str:
        return f"Search Destroy AI {self.number}"

    def shootcoords(self,opponentcontents: list)->(int, int):
        if len(self.destroylocation) != 0:
            self.mode = 'destroy'
        else:
            self.mode = 'search'

        if self.mode == "destroy":
            if self.destroycount == 0:
                self.destroyrow, self.destroycol = self.destroylocation[0]
                self.destroycount = 3
                return self.destroyrow, self.destroycol-1
            elif self.destroycount == 3:
                self.destroycount -= 1
                return self.destroyrow-1, self.destroycol
            elif self.destroycount == 2:
                self.destroycount -= 1
                return self.destroyrow, self.destroycol+1
            elif self.destroycount == 1:
                self.destroycount -= 1
                self.destroylocation.pop(0)
                self.mode = "search"
                return self.destroyrow+1, self.destroycol

        elif self.mode == "search":
            option = random.choice(self.emptycoords)
            row, col = option
            return int(row), int(col)

    def shoot(self,opponentname: str ,opponentshiplist: dict ,opponentcontents: list,playername: str) -> None: # add y,x, self.shiplits
        while True:
            row,col = self.shootcoords(opponentcontents)
            if self.shootplacementcheck(col,row) and self.shootplacementposition(col,row,opponentcontents) :
                if opponentcontents[row][col] != "O" and opponentcontents[row][col] != "X":
                    if opponentcontents[row][col] != "*":
                        self.destroylocation.append((row, col))
                        Player.shootgrid(self, opponentname, opponentshiplist, opponentcontents, playername, row, col)
                        self.emptycoords.remove((row,col))
                        break
                    else:
                        Player.shootgrid(self, opponentname, opponentshiplist, opponentcontents, playername, row, col)
                        self.emptycoords.remove((row, col))
                        break
            else:
                continue


    def shootplacementposition(self,x: int ,y: int ,opponentcontent: list)-> bool: #check for board anad then replace *
        if opponentcontent[y][x] != 'O' and opponentcontent[y][x] != 'X':
            return True
        else:
            return False

    def shootplacementcheck(self,x: int,y: int)-> bool:#check the int and details
        if self.row <= y or y < 0 or x < 0 or self.column <= x:
            return False
        else:
            return True


    def shipplacement(self):
        Player.shipplace(self,self.name)