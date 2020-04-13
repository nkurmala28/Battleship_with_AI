from Board import Board
from typing import Tuple
from Ships import Ships
import random

#only for inteheriting by those not human

class Player(object): #fix issue of same name being printed
    def __init__(self,m: int, n: int, num: int,shiplist: dict,opponentshiplist: dict):
        self.row = m
        self.column = n
        self.number = num
        self.contents = [['*' for x in range(n)] for y in range(m)]
        self.shiplist = shiplist
        self.opponentshiplist = opponentshiplist


#for ship placement
    def shipplace(self,playername: str) -> None:
        Board.printscanninggrid(self.contents, self.row, self.column,playername)
        for ship in self.shiplist:
            shipname = ship
            marker = shipname[0].upper()
            length = int(self.shiplist[shipname])
            while True:
                y,x,orientation = self.shipinputcheck(ship,length,self.shiplist)
                if orientation[0].upper() == 'H':
                    for i in range(length):
                        self.contents[y][x+i] = marker
                    break
                elif orientation[0].upper() == 'V':
                    for i in range(length):
                        self.contents[y+i][x] = marker
                    break
            Board.printscanninggrid(self.contents, self.row, self.column,playername)

    def shipinputcheck(self, shipname: str, length: int, playershiplist: dict) -> Tuple[int, int, str]:
        while True:
            y,x,orientation = self.get_ship_start_coords(length)
            if self.overlapcheck(x, y, shipname, length, orientation, playershiplist):
                return y, x, orientation

    def get_ship_start_coords(self,length:int) -> Tuple[int,int,str]:
        orientation = random.choice(["Horizontal","Vertical"])
        if orientation == "Horizontal":
            row = random.randint(0, self.row - 1)
            col = random.randint(0, self.column - length)
            return row, col, orientation

        elif orientation == "Vertical":
            row = random.randint(0, self.row-length)
            col = random.randint(0, self.column - 1)
            return row, col, orientation

    def overlapcheck(self, x: int, y: int, shipname: str, length: int, orientation: str, playershiplist: dict) -> bool:
        if orientation[0].upper() == 'H':
            for i in range(length):
                if self.contents[y][x + i] != "*":
                    character = self.contents[y][x + i]
                    overlapshipname = self.namefinder(character, playershiplist)
                    return False
        elif orientation[0].upper() == 'V':
            for i in range(length):
                if self.contents[y + i][x] != "*":
                    character = self.contents[y + i][x]
                    overlapshipname = self.namefinder(character, playershiplist)
                    return False
        return True

    def namefinder(self, char: str, playershiplist: dict) -> str:
        for name in playershiplist:
            if name[0].upper() == char.upper():
                return f"['{char.upper()}']"


#########for shooting###########################################################################################################

    def shootgrid(self,opponentname: str ,opponentshiplist: dict ,opponentcontents: list,playername: str,y: int,x: int) -> None:
        while True:
            print(f"{playername}'s Scanning Board")
            Board.oppview(opponentcontents,self.row,self.column)
            print(f"\n{playername}'s Board")
            Board.printgrid(self.contents,self.row,self.column)
            char = opponentcontents[y][x]
            Ships.shipshot(char,opponentname,opponentshiplist)
            if opponentcontents[y][x] == "*":
                opponentcontents[y][x] = "O"
            else:
                opponentcontents[y][x] = "X"
            print(f"{playername}'s Scanning Board")
            Board.oppview(opponentcontents, self.row, self.column) #check for this spacing
            print(f"\n{playername}'s Board")
            Board.printgrid(self.contents, self.row, self.column)
            break



