from Board import Board
from Ships import Ships
from typing import Tuple

class HumanPlayer(object):
    def __init__(self,m: int, n: int, num: int,shiplist: dict,opponentshiplist: dict):
        self.row = m
        self.column = n
        self.number = num
        self.contents = [['*' for x in range(n)] for y in range(m)]
        self.name = self.get_name()
        self.playershiplist = shiplist
        self.opponentshiplist = opponentshiplist


    def get_name(self) -> str:
        self.name = input(f"Player {self.number} please enter your name: ")
        return self.name

    #THE SHOOT FUNCTION
    def shoot(self,opponentname: str ,opponentshiplist: dict ,opponentcontents: list,player2name: str) -> None:
        while True:
            print(f"{self.name}'s Scanning Board")
            Board.oppview(opponentcontents,self.row,self.column)
            print(f"\n{self.name}'s Board")
            Board.printgrid(self.contents,self.row,self.column)

            x,y = self.shootinputcheck(opponentcontents)
            shotcharac = opponentcontents[y][x]
            Ships.shipshot(shotcharac,opponentname,opponentshiplist)

            if opponentcontents[y][x] == "*":
                opponentcontents[y][x] = "O"
            else:
                opponentcontents[y][x] = "X"
            print(f"{self.name}'s Scanning Board")
            Board.oppview(opponentcontents, self.row, self.column) #check for this spacing
            print(f"\n{self.name}'s Board")
            Board.printgrid(self.contents, self.row, self.column)
            break

    # Supporting functions
    def shootinputcheck(self,opponentcontent: list) -> Tuple[int,int]:
        while True:
            coord = input(f"\n{self.name}, enter the location you want to fire at in the form row, column: ")
            if self.shootformatcheck(coord):
                y, x = coord.split(",")
                x = int(x.strip())
                y = int(y.strip())
                if self.shootplacementcheck(x,y) and self.shootplacementposition(x,y,opponentcontent):
                    return x,y


    def shootformatcheck(self,coord: str) -> bool:
        if len(coord.split(",")) > 2:
            print(f'{coord} is not a valid location.\nEnter the firing location in the form row, column')
            return False
        elif "," in coord:
            y, x = coord.split(",")
            if '-' in x or '-' in y:
                print(f"{coord} is not in bounds of our {self.row} X {self.column} board.")
                return False
            elif (x.strip()).isdigit() and (y.strip()).isdigit():
                return True
            elif not (y.strip()).isdigit():
                print(f"Row should be an integer. {y} is NOT an integer.")
                return False
            elif not (x.strip()).isdigit():
                print(f"Column should be an integer. {x} is NOT an integer.")
                return False
        else:
            print(f"{coord} is not a valid location.\nEnter the firing location in the form row, column")
            return False

    def shootplacementposition(self,x: int ,y: int ,opponentcontent: list)-> bool: #check for board anad then replace *
        if opponentcontent[y][x]  ==  'O' or opponentcontent[y][x]=='X':
            print(f"You have already fired at {y}, {x}.")
            return False
        else:
            return True

    def shootplacementcheck(self,x: int,y: int)-> bool:#check the int and details
        if self.row <= y or self.column <= x:
            print(f"{y}, {x} is not in bounds of our {self.row} X {self.column} board.")
            return False
        else:
            return True


    #THE PLACEMENT FUNCTION
    def shipplacement(self) -> None:
        Board.printscanninggrid(self.contents, self.row, self.column,self.name)
        for ship in self.playershiplist:
            shipname = ship
            marker = shipname[0].upper()
            length = int(self.playershiplist[shipname])
            while True:
                x,y,orientation = self.shipinputcheck(shipname,length,self.playershiplist)
                if orientation[0].upper() == 'H':
                    for i in range(length):
                        self.contents[y][x+i] = marker
                    break
                elif orientation[0].upper() == 'V':
                    for i in range(length):
                        self.contents[y+i][x] = marker
                    break
            Board.printscanninggrid(self.contents, self.row, self.column,self.name)


    # supporting functions
    def orientation(self,shipname: str,length: int) -> str:
        while True:
            orientation = input(f"{self.name} enter horizontal or vertical for the orientation of {shipname} which is {length} long: ")
            if (orientation.strip()).upper() == 'H' or (orientation.strip()).upper() == 'HORIZONTAL' or (orientation.strip()).upper() == "VERTICAL" or (orientation.strip()).upper() == "V":
                return orientation
            else:
                print(f"{orientation} does not represent an Orientation")


    def shipinputcheck(self, shipname: str, length: int ,playershiplist: dict) -> Tuple[int,int,str]:
        while True:
            orientation = self.orientation(shipname, length)
            coord = input(f"{self.name}, enter the starting position for your {shipname} ship ,which is {length} long, in the form row, column: ")
            if self.formatcheck(coord,shipname,orientation):
                y,x = coord.split(",")
                x = int(x.strip())
                y = int(y.strip())
                if self.outofbounds(x,y,shipname,length,orientation) and self.rangecheck(x, y, shipname, length, orientation) and self.overlapcheck(x, y, shipname, length, orientation,playershiplist):
                    return x,y,orientation

    def formatcheck(self,coord: str,shipname: str,orientation: str)-> bool:
        if len(coord.split(",")) > 2:
            print(f'{coord} is not in the form x,y')
            return False
        elif "," in coord:
            y,x = coord.split(",")
            if '-' in x or '-' in y:
                if orientation[0].upper() == "V":
                    print(f"Cannot place {shipname} vertically at {coord} because it would be out of bounds.")
                else:
                    print(f"Cannot place {shipname} horizontally at {coord} because it would be out of bounds.")
                return False
            elif (x.strip()).isdigit() and (y.strip()).isdigit():
                return True
            elif not (y.strip()).isdigit():
                print(f"{y} is not a valid value for row.\n It should be an integer between 0 and {self.row - 1}")
                return False
            elif not (x.strip()).isdigit():
                print(f"{x} is not a valid value for column.\n It should be an integer between 0 and {self.column - 1}")
                return False
        else:
            print(f"{coord} is not in the form x,y")
            return False

    def outofbounds(self,x: int,y: int,shipname: str,length: int,orientation: str)-> bool:
        if self.column-1 < x or self.row-1 < y:
            if orientation[0].upper() == "H":
                print(f"Cannot place {shipname} horizontally at {y}, {x} because it would be out of bounds.")
                return False
            elif orientation[0].upper() == "V":
                print(f"Cannot place {shipname} vertically at {y}, {x} because it would be out of bounds.")
                return False
        else:
            return True


    def rangecheck(self, x: int, y: int, shipname: str, length: int, orientation: str)-> bool:
        if orientation[0].upper() == "H":
            if self.column > x+length-1 and x >= 0 and self.row > y >= 0:
                return True
            else:
                print(f"Cannot place {shipname} horizontally at {y}, {x} because it would end up out of bounds.")
                return False
        elif orientation[0].upper() == "V":
            if self.row > y+length-1 and y >= 0 and self.column > x >= 0:
                return True
            else:
                print(f"Cannot place {shipname} vertically at {y}, {x} because it would end up out of bounds.")
                return False

    def overlapcheck(self, x: int, y: int, shipname: str, length: int, orientation: str,playershiplist: dict)-> bool:
        if orientation[0].upper() == 'H':
            for i in range(length):
                if self.contents[y][x + i] != "*":
                    character = self.contents[y][x + i]
                    overlapshipname = self.namefinder(character,playershiplist)
                    print(f"Cannot place {shipname} horizontally at {y}, {x} because it would overlap with {overlapshipname}")
                    return False
        elif orientation[0].upper() == 'V':
            for i in range(length):
                if self.contents[y+i][x] != "*":
                    character = self.contents[y+i][x]
                    overlapshipname = self.namefinder(character,playershiplist)
                    print(f"Cannot place {shipname} vertically at {y}, {x} because it would overlap with {overlapshipname}")
                    return False
        return True

    def namefinder(self,char: str,playershiplist: dict)-> str:
        for name in playershiplist:
            if name[0].upper() == char.upper():
                return f"['{char.upper()}']"



