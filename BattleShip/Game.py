# game player board ships missiles
from HumanPlayer import HumanPlayer
from Ships import Ships
import sys
import random
from RandomAi import RandomAi
from CheatingAi import CheatingAi
from SearchDestroy import SearchDestroy

class Game(object):

    def __init__(self):
        configfile = open(sys.argv[1])
        seed = int(sys.argv[2])
        random.seed(seed)
        dimensions = str(configfile.readline())
        dimensions = dimensions.rstrip('\n')
        dimensions = dimensions.split(" ")
        self.rows = int(dimensions[0])
        self.columns = int(dimensions[1])
        self.player1shiplist = {}
        self.player2shiplist = {}

        for line in configfile:
            line = line.strip('\n')
            line = line.split(' ')
            self.player1shiplist[line[0]] = int(line[1])
            self.player2shiplist[line[0]] = int(line[1])

    def GamePlay(self):
        options = {"Human":HumanPlayer,"CheatingAi":CheatingAi,"SearchDestroyAi":SearchDestroy,"RandomAi":RandomAi}

        playertype1 = (input("Enter one of ['Human', 'CheatingAi', 'SearchDestroyAi', 'RandomAi'] for Player 1's type: ")).lower().replace(" ","")
        for i in options:
            if (i.lower()).startswith(playertype1):
                playertype1 = i
                break
        type1 = options[playertype1]
        player1 = type1(self.rows,self.columns,1,self.player1shiplist,self.player2shiplist)
        player1.shipplacement()

        playertype2 = (input("Enter one of ['Human', 'CheatingAi', 'SearchDestroyAi', 'RandomAi'] for Player 2's type: ")).lower().replace(" ","")
        for i in options:
            if (i.lower()).startswith(playertype2):
                playertype2 = i
                break
        type2 = options[playertype2]
        player2 = type2(self.rows,self.columns,2,self.player2shiplist,self.player1shiplist)
        player2.shipplacement()

        while True:
            player1.shoot(player2.name,self.player2shiplist,player2.contents,player1.name)
            if Ships.allshipsdown(self.player2shiplist):
                print(f"\n{player1.name} won the game!")
                break
            player2.shoot(player1.name,self.player1shiplist,player1.contents,player2.name)  #best way to return the coordinates since the method to get them coordinates are different
            if Ships.allshipsdown(self.player1shiplist):
                print(f"\n{player2.name} won the game!")
                break

#check the shit when shit been shot down twice and have to be redone ffs

#PROPbably a problem during the swtich from destroy to search