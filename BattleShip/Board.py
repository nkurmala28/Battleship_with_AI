class Board(object):
    def __init__(self, m: int, n: int):
        self.rows = n
        self.columns = m
        self.contents = [['*' for x in range(n)] for y in range(m)]

    def __iter__(self):
        return iter(self.contents)

    def __getitem__(self, index: int):
        return self.contents[index]

    @staticmethod
    def printgrid(content: list,row: int,column: int):
        print(" ", end=" ")  # first sep character
        for columnnumber in range(column):
            print(columnnumber, end=' ')  # first line
        print(end="\n")  # to create new line after the first line

        # the following rows below the first row
        for rownumber in range(row):
            print(rownumber, end=" ")
            for gridvalue in content[rownumber]:
                print(gridvalue, end=" ")
            print(end='\n')

    @staticmethod
    def printscanninggrid(content: list,row: int,column: int,name: str):
        print(f"{name}'s Placement Board")
        print(" ", end=" ")  # first sep character
        for columnnumber in range(column):
            print(columnnumber, end=' ')  # first line
        print(end="\n")  # to create new line after the first line

        # the following rows below the first row
        for rownumber in range(row):
            print(rownumber, end=" ")
            for gridvalue in content[rownumber]:
                print(gridvalue, end=" ")
            print(end='\n')

    @staticmethod
    def oppview(opponentcontent: list,rows: int,columns: int):
        #xnums = range(rows)
        #ynums = range(columns)
        print(" ", end=" ")  # first sep character
        for columnnumber in range(columns):
            print(columnnumber, end=' ')  # first line
        print(end="\n")  # to create new line after the first line

        # the following rows below the first row
        for rownumber in range(rows):
            print(rownumber, end=" ")
            for gridvalue in opponentcontent[rownumber]:
                if gridvalue == "X" or gridvalue == "O" or gridvalue == "*":
                    print(gridvalue, end=" ")
                else:
                    print("*", end=" ")
            print(end='\n')
