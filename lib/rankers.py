from collections import Counter
from card import Card
from cardgroup import CardGroup
from deck import Deck

if __name__ == '__main__':
    d = Deck()
    d.gen_cards()
    test = CardGroup([d.cards[c] for c in range(0,4)])
    test.add_card(Card(14,"Diamonds"))
    # printCard(number, suit)
    print test
    print ""
    print test.is_straight()
    print test.straight_details()