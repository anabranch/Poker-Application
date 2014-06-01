from collections import Counter
import operator
from utils import longest_sequence

from baseclasses.generics import Card

def hand_val_gen(**kwargs):
    """
    Generates a card_value_dictionary to
    to easily give hand rank information
    """
    dic = {
        "name": None,
        "hand_rank": None,
        "suit": None,
        "all_cards": [],
        "s_or_sf_high_card": None,
        "three_kind_value": None,
        "four_kind_value": None,
        "two_kind_value": None,
        "two_kind_value_2": None,
        "ordered_kickers": []
    }
    for name, val in kwargs.items():
        dic[name] = val
    return dic

def group_by_num(cards, add_low_ace=False):
    card_dictionary = {}
    for card in cards:
        if card.number not in card_dictionary:
            card_dictionary[card.number] = []
        card_dictionary[card.number].append(card)
    if add_low_ace:
        if 14 in card_dictionary:
            card_dictionary[1] = []
            for val in card_dictionary[14]:
                card_dictionary[1].append(val)
    return card_dictionary

def group_by_suit(cards, add_low_ace=False):
    suit_dictionary = {}
    for card in cards:
        if card.suit not in suit_dictionary:
            suit_dictionary[card.suit] = []
        suit_dictionary[card.suit].append(card)
    if add_low_ace:
        for k, vals in suit_dictionary.items():
            nums = [card.number for card in vals]
            if 14 in nums:
                suit_dictionary[k].append(Card(1,k))
    return suit_dictionary

def get_no_hand(cards):
    """
    Takes in a list of cards and a max return count
    and returns a hand val generated dictionary
    """
    cards = sorted([card for card in cards], reverse=True, key=operator.attrgetter('number'))[:5]
    resp = hand_val_gen(hand_rank=0,name="High Card", \
    all_cards=cards, ordered_kickers=cards)
    return resp

def get_kickers(cards, exclude_cards=[], mx=5):
    """
    Takes in a list of cards and a max return count
    and returns an ordered list of kickers
    """
    cs = []
    if mx > 5:
        mx = 5
    for card in cards:
        if card not in exclude_cards:
            cs.append(card)
    return sorted(cs, key=operator.attrgetter('number'))[-mx:]

def get_two_kind(cards):
    """
    Gets the highest two_kind in a list of cards
    and returns a hand val generated dictionary
    """
    two_kind_val = 0
    two_kind = []
    c_by_num = group_by_num(cards)

    for number, card_list in c_by_num.items():
        if len(card_list) >= 2:
            if number > two_kind_val:
                two_kind_val = number

    if not two_kind_val:
        return {}

    two_kind = c_by_num[two_kind_val][:2]
    kickers = get_kickers(cards, two_kind, 3)
    resp = hand_val_gen(hand_rank=1,name='Pair',two_kind_value=two_kind_val)
    resp['all_cards'] = two_kind + kickers
    resp['ordered_kickers'] = kickers
    return resp

def get_two_two_kind(cards):
    doubles = []
    c_by_num = group_by_num(cards)
    for number, card_list in c_by_num.items():
        if len(card_list) >= 2:
            doubles.append((number, card_list[:2]))
    if len(doubles) < 2:
        return {}
    doubles = sorted(doubles)
    tpv, tp = doubles.pop()
    bpv, bp = doubles.pop()
    kicker = get_kickers(cards, tp+bp, 1)
    resp = hand_val_gen(hand_rank=2,name="Two Pair", \
        two_kind_value=tpv, two_kind_value_2=bpv)
    resp['all_cards'] = tp + bp + kicker
    resp['ordered_kickers'] = kicker
    return resp

def get_three_kind(cards):
    """
    Gets the highest set of 3 of a kind in a list of cards
    and returns a hand val generated dictionary
    """
    three_kind_val = 0
    three_kind = []
    c_by_num = group_by_num(cards)

    for number, card_list in c_by_num.items():
        if len(card_list) >= 3:
            if number > three_kind_val:
                three_kind_val = number

    if not three_kind_val:
        return {}
    three_kind = c_by_num[three_kind_val][:3]
    kickers = get_kickers(cards, three_kind, 2)
    resp = hand_val_gen(hand_rank=3,name='Three of a Kind',three_kind_value=three_kind_val)
    resp['all_cards'] = three_kind + kickers
    resp['ordered_kickers'] = kickers
    return resp

def get_four_kind(cards):
    """
    Gets the highest set of 4 of a kind in a list of cards
    and returns a hand val generated dictionary
    """
    four_kind_val = 0
    four_kind = []
    c_by_num = group_by_num(cards)

    for number, card_list in c_by_num.items():
        if len(card_list) >= 4:
            if number > four_kind_val:
                four_kind_val = number

    if not four_kind_val:
        return {}
    four_kind = c_by_num[four_kind_val][:4]
    kickers = get_kickers(cards, four_kind, 1)
    resp = hand_val_gen(hand_rank=7,name='Four of a Kind',four_kind_value=four_kind_val)
    resp['all_cards'] = four_kind + kickers
    resp['ordered_kickers'] = kickers
    return resp

def get_straight(cards):
    """
    Gets the highest straight in a list of cards
    and returns a hand val generated dictionary
    """
    high_card = 0
    straight = []

    c_by_num = group_by_num(cards,add_low_ace=True)
    print c_by_num
    nums = c_by_num.keys()
    if len(nums) < 5:
        return {}
    seqcount, sequence = longest_sequence(nums)
    if seqcount < 5:
        return {}
    high_card = c_by_num[max(sequence)][0]
    for c in sequence:
        straight.append(c_by_num[c][0])

    resp = hand_val_gen(hand_rank=4,name='Straight',s_or_sf_high_card=high_card)
    resp['all_cards'] = straight
    return resp

def get_flush(cards):
    suit = None
    suited_cards = []
    c_by_suit = group_by_suit(cards)
    for s, cs in c_by_suit.items():
        if len(cs) >= 5:
            suit = s
            suited_cards = get_kickers(cs,[],5)
    if not suit:
        return {}
    resp = hand_val_gen(hand_rank=5,name="Flush", suit=suit)
    resp['all_cards'] = suited_cards
    resp['ordered_kickers'] = suited_cards
    return resp

def get_full_house(cards):
    three_kind_info = get_three_kind(cards)
    two_two_kind_info = get_two_two_kind(cards)
    if not three_kind_info and not two_two_kind_info:
        return {}

    fh = []
    for card in three_kind_info['all_cards']:
        if card not in three_kind_info['ordered_kickers']:
            fh.append(card)
    full_of_value = 0

    if three_kind_info['three_kind_value'] != two_two_kind_info['two_kind_value']:
        full_of_value = two_two_kind_info['two_kind_value']

    elif three_kind_info['three_kind_value'] != two_two_kind_info['two_kind_value_2'] and full_of_value == 0:
        full_of_value = two_two_kind_info['two_kind_value_2']
    else:
        print {}

    for card in two_two_kind_info['all_cards']:
        if card not in two_two_kind_info['ordered_kickers'] and card.number == full_of_value:
            fh.append(card)
    print fh
    resp = hand_val_gen(hand_rank=6,name="Full House", \
        three_kind_value=three_kind_info['three_kind_value'], two_kind_value=full_of_value)
    resp['all_cards'] = fh
    return resp

def get_straight_flush(cards):
    pass



    

