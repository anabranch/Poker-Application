from collections import Counter
import operator
from random import shuffle

from baseclasses.basecardgroup import BaseCardGroup
from baseclasses.statedobject import StatedObject
from card import Card
from utils import longest_sequence

class ValuedCardGroup(BaseCardGroup):
    """docstring for ValuedCardGroup"""
    def __init__(self, cards=[]):
        super(ValuedCardGroup, self).__init__(cards)

    def best_hand(self): # could be optimized but this is fine for now
        kickers = self._kickers()
        pair = self._pair()
        two_pair = self._two_pair()
        trip = self._trip()
        quad = self._quad()
        straight = self._straight()
        flush = self._flush()
        fh = self._full_house()
        straightflush = self._straight_flush()
        if straightflush:
            return straightflush
        if fh:
            return fh
        if quad:
            return quad
        if flush:
            return flush
        if straight:
            return straight
        if quad:
            return quad
        if trip:
            return trip
        if two_pair:
            return two_pair
        if pair:
            return pair
        return kickers

    def _cards_by_number(self, add_low_ace=False):
        local_cards = self.local_card_copy()
        number_dict = {}
        for card in local_cards:
            if card.number not in number_dict:
                number_dict[card.number] = []
            number_dict[card.number].append(card)
        if add_low_ace:
            if 14 in number_dict:
                number_dict[1] = []
                for val in number_dict[14]:
                    number_dict[1].append(Card(1, val.suit))
        return number_dict

    def _cards_by_suit(self, add_low_ace=False):
        local_cards = self.local_card_copy()
        suit_dict = {}
        for card in local_cards:
            if card.suit not in suit_dict:
                suit_dict[card.suit] = []
            suit_dict[card.suit].append(card)
        if add_low_ace:
            for k, vals in suit_dict.items():
                nums = [card.number for card in vals]
                if 14 in nums:
                    suit_dict[k].append(Card(1,k))
        return suit_dict

    def _kickers(self, remove_cards=[], mx=5):
        if mx > 5:
            mx = 5
        local_cards = self.local_card_copy()
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
        card_num_dict = self._cards_by_number(add_low_ace=True)
        sorted_keys_num_dict = sorted(card_num_dict)
        if len(sorted_keys_num_dict) < 5:
            return {}
        seqcount, sequence = longest_sequence(sorted_keys_num_dict)
        if seqcount < 5:
            return {}
        seqfinal = sorted(sequence, reverse=True)[:5]
        if 1 in seqfinal:
            seqfinal.remove(1)
            seqfinal.append(14)
        vals = [card_num_dict[val][0] for val in seqfinal]
        return {"hand":vals}

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
            vals += dub.values()[0]
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
        card_num_dict = self._cards_by_number()
        doubles = []
        triples = []
        final_combo = []
        for k, v in card_num_dict.items():
            if len(v) >= 3:
                triples.append({k:v[:3]})
            elif len(v) >= 2:
                doubles.append({k:v[:2]})

        if len(triples) == 0 or (len(triples) == 1 and len(doubles) == 0):
            return {}
        if len(triples) == 1:
            final_combo += triples[0].values()[0]
            final_combo += max(doubles).values()[0]
        elif len(triples) == 2:
            sorted_trips = sorted(triples)
            first = sorted_trips.pop()
            second = sorted_trips.pop()
            final_combo += first.values()[:3][0]
            final_combo += second.values()[:2][0]
        return {"hand":final_combo}

    def _straight_flush(self):
        card_suit_dict = self._cards_by_suit(add_low_ace=True)
        suit = None
        numcarddict = {}
        keys = []
        for k, v in card_suit_dict.items():
            if len(v) >= 5:
                suit = k
                for val in v:
                    keys.append(val.number)
                    numcarddict[val.number] = val
                break
        if len(keys) < 5:
            return {}
        seqcount, sequence = longest_sequence(sorted(keys))
        if seqcount < 5:
            return {}
        seqfinal = sorted(sequence, reverse=True)[:5]
        if 1 in seqfinal:
            seqfinal.remove(1)
            seqfinal.append(14)
        vals = [numcarddict[val] for val in seqfinal]
        return {"hand":vals}


class PocketCardGroup(BaseCardGroup):
    """docstring for PocketCardGroup"""
    def __init__(self):
        super(PocketCardGroup, self).__init__([])


class DeckCardGroup(BaseCardGroup, StatedObject):
    """docstring for Deck"""
    def __init__(self):
        super(DeckCardGroup, self).__init__([])
        self.state = "unshuffled"
        suits = ["Diamonds","Clubs","Hearts","Spades"]
        number = range(2,15)
        self.unshuffled_cards = []
        for suit in suits:
            for card in number:
                print suit,card
                self.cards.append(Card(card, suit))

    def shuffle(self):
        if self.state == "unshuffled":
            self.state_change(self.state, "shuffled")
            self.unshuffled_cards = self.local_card_copy()
            shuffle(self.cards)
        else:
            print "cards already shuffled"

    def pop(self):
        if self.state == 'shuffled':
            return self.cards.pop()

class BoardCardGroup(BaseCardGroup, StatedObject):
    def __init__(self):
        super(BoardCardGroup, self).__init__([])
        # preflop, flop, turn, river
        self.state = "preflop"

    def add_flop(self, cards):
        self.cards += cards

    def add_turn(self, card):
        self.cards += card

    def add_river(self, card):
        self.cards += card

class BurnCardGroup(BaseCardGroup, StatedObject):
    def __init__(self):
        super(BurnCardGroup, self).__init__([])
        # preflop, flop, turn, river
        self.state = "preflop"

    def burn(self, card):
        pass