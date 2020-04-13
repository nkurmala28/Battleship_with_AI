class Ships(object):

    @staticmethod
    def shipshot(character: str, opponentname: str, opponentshiplist: dict):
        for ship in opponentshiplist:
            if ship[0].upper() == character.upper():
                opponentshiplist[ship] -= 1
                if opponentshiplist[ship] == 0:
                    print(f"You hit {opponentname}'s {ship}!")
                    print(f"You destroyed {opponentname}'s {ship}")
                    break
                else:
                    print(f"You hit {opponentname}'s {ship}!")
                    break
        else:
            print("Miss")


    @staticmethod
    def allshipsdown(playerlist: dict)-> bool:
        for value in playerlist.values():
            if int(value) != 0:
                return False
        return True

        #function that ends game and prints winner after this nonosense
        pass
