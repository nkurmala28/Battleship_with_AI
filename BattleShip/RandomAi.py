from Player import Player
from typing import Tuple
import random

class RandomAi(Player):

    def __init__(self,n: int,m: int,num: int,shiplist: dict,opponentshiplist: dict):
        super().__init__(n,m,num,shiplist,opponentshiplist)
        self.name = self.AIname()

        self.emptycoords = []
        for row in range(self.row):
            for col in range(self.column):
                self.emptycoords.append((row,col))

    def AIname(self) -> str:
        return f"Random Ai {self.number}"

    def shootcoords(self,opponentcontents: list) -> Tuple[int,int]:
        option = random.choice(self.emptycoords)
        row,col = option
        self.emptycoords.remove(option)
        return int(row),int(col)

    def shoot(self,opponentname: str ,opponentshiplist: dict ,opponentcontents: list,playername: str):
        y,x = self.shootcoords(opponentcontents)
        Player.shootgrid(self,opponentname,opponentshiplist,opponentcontents,playername,y,x)

    def shipplacement(self):
        Player.shipplace(self,self.name)



