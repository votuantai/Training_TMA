from Deck import Deck
from Customer import Customer
from House import House

if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    deck.show()

    Bod = Customer("Bod")
    Bod.print_player()
    Bod.draw(deck)
    Bod.showhand()


    house = House()
    house.print_house()
    house.draw(deck)
    house.showhand()