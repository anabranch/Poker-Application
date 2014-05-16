from card import Card
from collections import Counter
from equalitymixin import CommonEqualityMixin

class CardGroup(CommonEqualityMixin):
    """docstring for CardGroup"""
    def __init__(self, cards=[]):
        super(CardGroup, self).__init__()
        self.cards = cards

    def __str__(self):
        return str(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def get_card(self, number, suit):
        for c in self.cards:
            if c == Card(number, suit):
                return c
        else: # this should return an error
            return False

    def is_flush(self):
        local_cards = self.cards
        suits = [card.suit for card in local_cards]
        s_counter = Counter(suits)
        if max(s_counter.values()) > 4:
            return True
        else:
            return False

    def flush_details(self):
        local_cards = self.cards
        suits = [card.suit for card in local_cards]
        s_counter = Counter(suits)
        fl_suit = None
        for k, v in s_counter.items():
            if v > 4:
                fl_suit = k
        mx = 0
        for x in local_cards:
            if mx <= x.number and x.suit == fl_suit:
                mx = x.number
        return self.get_card(mx, fl_suit)

    def is_straight(self):
        local_cards = self.cards

        successives = 1
        for x in local_cards:
            if x.is_ace:
                local_cards.append(Card(1,x.suit))

        values = sorted([card.as_tuple() for card in local_cards])
        for x in enumerate(values):
            location = x[0]
            num, suit = x[1]
            if location+1 >= len(values):
                break
            n2, s2 = values[location+1]
            if num+1 == n2:
                successives += 1
        if successives == 5:
            return True
        else:
            return False

    def straight_details(self):
        local_cards = self.cards
        mx = 0
        for x in local_cards:
            if x.is_ace:
                local_cards.append(Card(1,x.suit))

        values = sorted([card.as_tuple() for card in local_cards])
        for x in enumerate(values):
            location = x[0]
            num, suit = x[1]
            if location+1 >= len(values):
                break
            n2, s2 = values[location+1]
            if num+1 == n2:
                mx = n2
        return self.get_card(mx, suit)

    def is_straight_flush(self):
        local_cards = self.cards
        
        if not self.is_straight() and not self.is_flush():
            return False
        successives = 1
        print local_cards
        print self.cards
        for x in local_cards:
            if x.is_ace:
                print local_cards
                local_cards.append(Card(1,x.suit))

        print local_cards
        dict_by_suit = {}
        for c in local_cards:
            num, suit = c.as_tuple()
            if suit not in dict_by_suit:
                dict_by_suit[suit] = [num]
            else:
                dict_by_suit[suit].append(num)

        for k, v in dict_by_suit.items():
            if len(sorted(v)) >= 5:
                print k, sorted(v)

        return False

    def straight_flush_details(self):
        local_cards = self.cards
        successives = 1
        mx = 0
        suit = None
        return self.get_card(mx, suit)
            