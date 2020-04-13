from Player import Player
from typing import List, Tuple

class CheatingAi(Player):

    def __init__(self,n: int,m: int,num: int,shiplist: dict,opponentshiplist: dict):
        super().__init__(n,m,num,shiplist,opponentshiplist)
        self.name = self.AIname()

    def AIname(self):
        return f"Cheating Ai {self.number}"

    def opponentcoords(self,opponentcontents: list) -> List[Tuple[int, int]]:
        availcoords = []
        for row in range(self.row):
            for col in range(self.column):
                if opponentcontents[row][col] != "O" and opponentcontents[row][col] != "*" and opponentcontents[row][col] != "X":
                    availcoords.append((row,col))
        return availcoords

    def shootcoords(self,opponentcontents: list) -> Tuple[int,int]:
        availcoords = self.opponentcoords(opponentcontents)
        y,x = availcoords.pop(0)
        return y,x

    def shoot(self,opponentname: str ,opponentshiplist: dict ,opponentcontents: list,playername: str): # add y,x, self.shiplits
        y,x = self.shootcoords(opponentcontents)
        Player.shootgrid(self,opponentname,opponentshiplist,opponentcontents,playername,y,x)

    def shipplacement(self):
        Player.shipplace(self,self.name)