from card import Card
from copy import copy
from collections import Counter
from equalitymixin import CommonEqualityMixin

class CardGroup(CommonEqualityMixin):
    """docstring for CardGroup"""
    def __init__(self, cards=[]):
        super(CardGroup, self).__init__()
        self._cards = [copy(card) for card in cards]

    def __str__(self):
        return str(self._cards)

    def cards(self):
        return [copy(card) for card in self._cards]

    def add_card(self, card):
        cards = self.cards()
        cards.append(copy(card))
        self._cards = cards

    def get_card(self, number, suit):
        for c in self._cards:
            if c == Card(number, suit):
                return c
        else: # this should return an error
            return False

    def is_straight(self):
        local_cards = self.cards()
        successives = 1
        for x in local_cards:
            if x.is_ace:
                local_cards.append(Card(1,x.suit))

        tuples = sorted([card.as_tuple() for card in local_cards])
        for x in enumerate(tuples):
            location = x[0]
            num, suit = x[1]
            if location + 1 >= len(tuples):
                break
            next_num, next_suit = tuples[location+1]
            if num + 1 == next_num:
                successives += 1
        if successives < 5:
            return False
        return True

    def straight_details(self):
        local_cards = self.cards()
        straight_cards = []
        mx_num = 0
        mx_suit = None
        for x in local_cards:
            if x.is_ace:
                local_cards.append(Card(1,x.suit))

        tuples = sorted([card.as_tuple() for card in local_cards])
        for x in enumerate(tuples):
            location = x[0]
            num, suit = x[1]
            if location + 1 >= len(tuples):
                break
            next_num, next_suit = tuples[location+1]
            if num + 1 == next_num:
                if mx_num == 0:
                    straight_cards.append(Card(num, suit))
                mx_num = next_num
                mx_suit = next_suit
                straight_cards.append(Card(mx_num, mx_suit))
        print set(straight_cards)
        return straight_cards

    def is_flush(self):
        local_cards = self.cards()
        suits = Counter([card.suit for card in local_cards])
        if max(suits.values()) > 4:
            return True
        else:
            return False

    def flush_details(self):
        local_cards = self.cards()
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

    def is_straight_flush(self):
        local_cards = self.cards()
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
        local_cards = self.cards()
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
            