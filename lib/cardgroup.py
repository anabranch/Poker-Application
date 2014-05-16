from card import Card
from copy import copy
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
        local_cards = copy(self.cards)
        suits = [card.suit for card in local_cards]
        s_counter = Counter(suits)
        print s_counter
        print local_cards
        if max(s_counter.values()) > 4:
            return True
        else:
            return False

    def flush_details(self):
        local_cards = copy(self.cards)
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
        local_cards = copy(self.cards)

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
        local_cards = copy(self.cards)
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
        print mx
        print suit
        return self.get_card(mx, suit)

    def is_straight_flush(self):
        local_cards = copy(self.cards)
        print local_cards
        mx = 0
        successives = 1
        for x in local_cards:
            if x.is_ace:
                local_cards.append(Card(1,x.suit))
        grouped_by_suit = {}
        for x in local_cards:
            num, suit = x.as_tuple()
            if suit not in grouped_by_suit:
                grouped_by_suit[suit] = [num]
            else:
                grouped_by_suit[suit].append(num)

        suited = None
        suit = None
        for k,v in grouped_by_suit.items():
            if len(v) >= 5:
                suit = k
                suited = sorted(grouped_by_suit[k])

        for location, num in enumerate(suited):
            if location+1 >= len(suited):
                break
            n2 = suited[location+1]
            if num+1 == n2:
                successives += 1
                mx = n2        
        if successives >= 5:
            return True
        return False

    def straight_flush_details(self):
        local_cards = copy(self.cards)
        print local_cards
        mx = 0
        for x in local_cards:
            if x.is_ace:
                local_cards.append(Card(1,x.suit))
        grouped_by_suit = {}
        for x in local_cards:
            num, suit = x.as_tuple()
            if suit not in grouped_by_suit:
                grouped_by_suit[suit] = [num]
            else:
                grouped_by_suit[suit].append(num)

        suited = None
        suit = None
        for k,v in grouped_by_suit.items():
            if len(v) >= 5:
                suit = k
                suited = sorted(grouped_by_suit[k])

        for location, num in enumerate(suited):
            if location+1 >= len(suited):
                break
            n2 = suited[location+1]
            if num+1 == n2:
                mx = n2
        return self.get_card(mx,suit)
            