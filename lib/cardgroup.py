from copy import copy
from collections import Counter
import operator

from equalitymixin import CommonEqualityMixin
from card import Card

class CardGroup(CommonEqualityMixin):
    """docstring for CardGroup"""
    def __init__(self, cards=[]):
        super(CardGroup, self).__init__()
        self.cards = cards

    def __str__(self):
        return str(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def _local_card_copy(self):
        return [copy(card) for card in self.cards]

    def _cards_by_number(self):
        local_cards = self._local_card_copy()
        number_dict = {}
        for card in local_cards:
            if card.number not in number_dict:
                number_dict[card.number] = []
            number_dict[card.number].append(card)
        return number_dict

    def _cards_by_suit(self):
        local_cards = self._local_card_copy()
        suit_dict = {}
        for card in local_cards:
            if card.suit not in suit_dict:
                suit_dict[card.suit] = []
            suit_dict[card.suit].append(card)
        return suit_dict

    def _kickers(self, remove_cards=[], mx=5):
        if mx > 5:
            mx = 5
        local_cards = self._local_card_copy()
        for card in remove_cards:
            local_cards.pop(local_cards.index(card))
        # need to get this to return cards not a tuple
        return sorted([card for card in local_cards], reverse=True, key=operator.attrgetter('number'))[:mx]

    def _pair(self):
        pair = []
        pair_value = 0
        card_num_dict = self._cards_by_number()
        for card_num, cards in card_num_dict.items():
            if len(cards) <= 1:
                del(card_num_dict[card_num])
        for k, v in card_num_dict.items():
            if k > pair_value:
                pair_value = k
                pair = v[:2]
        if pair:
            return {"hand": pair, "kickers":self._kickers(pair,3)}
        return {}

    def _trip(self):
        trips = []
        trip_value = 0
        card_num_dict = self._cards_by_number()
        for card_num, cards in card_num_dict.items():
            if len(cards) <= 2:
                del(card_num_dict[card_num])
        for k, v in card_num_dict.items():
            if k > trip_value:
                trip_value = k
                trips = v[:3]
        if trips:
            return {"hand": trips, "kickers":self._kickers(trips,2)}
        return {}

    def _quad(self):
        quads = []
        quad_value = 0
        card_num_dict = self._cards_by_number()
        for card_num, cards in card_num_dict.items():
            if len(cards) <= 3:
                del(card_num_dict[card_num])
        for k, v in card_num_dict.items():
            if k > quad_value:
                quad_value = k
                quads = v[:4]
        if quads:
            return {"hand": quads, "kickers":self._kickers(quads,1)}
        return {}

    def _straight(self):
        card_num_dict = self._cards_by_number()
        successive = []
        sorted_num_tuple = sorted(zip(card_num_dict.keys(), card_num_dict.values()))
        for location, val in enumerate(sorted_num_tuple):
            num, card = val
            if location + 1 >= len(card_num_dict):
                break # I bet there's a better way to do this...
            num2, card2 = sorted_num_tuple[location + 1]
            if num+1 == num2:
                successive.append(card2[0])
                if card[0] not in successive:
                    successive.append(card[0])
            else:
                successive = []
        if len(successive) >= 5:
            return {"hand":successive}
        return {}

    def _two_pair(self):
        card_num_dict = self._cards_by_number()
        doubles = []
        for k, v in card_num_dict.items():
            if len(v) >= 2:
                doubles.append({k:v[:2]})
        if len(doubles) < 2:
            return {}

        doubles = sorted(doubles, reverse=True)
        vals = []
        for dub in doubles:
            print dub.values()
            vals += dub.values()[0]
        print vals
        return {"hand":vals, "kickers":self._kickers(vals,1)}

    def _flush(self):
        card_suit_dict = self._cards_by_suit()
        suit = None
        vals = None
        for k, v in card_suit_dict.items():
            if len(v) >= 5:
                suit = k
                vals = list(reversed(list(reversed(sorted(v, key=operator.attrgetter('number'))))[:5]))
        if suit:
            return {"hand":vals}
        return {}

    def _full_house(self):
        # card_num_dict = self._cards_by_number()
        # doubles = []
        # for k, v in card_num_dict.items():
        #     if len(v) >= 2:
        #         doubles.append({k:v[:2]})
        # if len(doubles) < 2:
        #     return {}

        # doubles = sorted(doubles, reverse=True)
        # vals = []
        # for dub in doubles:
        #     print dub.values()
        #     vals += dub.values()[0]
        # print vals
        # return {"hand":vals, "kickers":self._kickers(vals,1)}
        return {}

    def _straight_flush(self):
        card_suit_dict = self._cards_by_suit()
        successive = []
        suit = None
        vals = []
        for k, v in card_suit_dict.items():
            if len(v) >= 5:
                suit = k
                vals = sorted(v, key=operator.attrgetter('number'))
        print vals
        for location, val in enumerate(vals):
            num, card, suit_rank = val.as_tuple()
            if location + 1 >= len(vals):
                break # I bet there's a better way to do this...
            val2 = vals[location + 1]
            num2, card2, suit_rank2 = vals[location + 1].as_tuple()
            if num+1 == num2:
                successive.append(val2)
                if val not in successive:
                    successive.append(val)
            else:
                successive = []
        if len(successive) >= 5:
            return {"hand":successive}
        return {}

class PocketCardGroup(CardGroup):
    """docstring for PocketCardGroup"""
    def __init__(self, cards=[]):
        super(PocketCardGroup, self).__init__(cards)

if __name__ == '__main__':
    x = PocketCardGroup([
            Card(14,"Diamonds"), 
            Card(14,"Spades"), 
            Card(13,"Diamonds"), 
            Card(13,"Clubs"), 
            Card(13, "Hearts")
        ])
    x.add_card(Card(2,"Diamonds"))
    print x.cards
    # print "High Cards"
    # print x.kickers()
    print "Full House"
    print x.two_pair()
    # print "pairs"
    # print x.pairs()
    # print "trips"
    # print x.trips()
    # print "quads"
    # print x.quads()
    # print "straight"
    # print x.straight()
    # print "flush"
    # print x.flush()
    # print "straight flush"
    # print x.straight_flush()
        