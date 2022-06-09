from Match import Match
from Customer import Customer
from House import House
if __name__ == '__main__':
    ## Player
    player = Customer('Bod')
    player.print_player()
    ## House
    house = House()
    house.print_house()
    ## Match
    match = Match(player, house)
    match.play()