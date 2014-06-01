from collections import Counter
import operator
from utils import longest_sequence, pretty

from baseclasses.generics import Card

def hand_val_gen(**kwargs):
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

def group_by_suit(cards):
    suit_dictionary = {}
    for card in cards:
        if card.suit not in suit_dictionary:
            suit_dictionary[card.suit] = []
        suit_dictionary[card.suit].append(card)
    return suit_dictionary

def get_no_hand(cards):
    cards = sorted([card for card in cards], key=operator.attrgetter('number'))[-5:]
    resp = hand_val_gen(hand_rank=0,name="High Card", \
    all_cards=cards, ordered_kickers=cards)
    return resp

def get_kickers(cards, exclude_cards=[], mx=5):
    cs = []
    if mx > 5:
        mx = 5
    for card in cards:
        if card not in exclude_cards:
            cs.append(card)
    return sorted(cs, key=operator.attrgetter('number'))[-mx:]

def get_two_kind(cards):
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
    high_card = 0
    straight = []

    c_by_num = group_by_num(cards,add_low_ace=True)
    nums = c_by_num.keys()
    if len(nums) < 5:
        return {}
    seqcount, sequence = longest_sequence(nums)
    if seqcount < 5:
        return {}
    high_card = c_by_num[max(sequence)][0]
    for c in sequence:
        straight.append(c_by_num[c][0])

    resp = hand_val_gen(hand_rank=4,name='Straight',s_or_sf_high_card=high_card.number)
    resp['all_cards'] = straight[-5:]
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
    if not three_kind_info or not two_two_kind_info:
        return {}

    fh = []
    for card in three_kind_info['all_cards']:
        if card not in three_kind_info['ordered_kickers']:
            fh.append(card)
    full_of_value = 0
    print two_two_kind_info
    if three_kind_info['three_kind_value'] != two_two_kind_info['two_kind_value']:
        full_of_value = two_two_kind_info['two_kind_value']

    elif three_kind_info['three_kind_value'] != two_two_kind_info['two_kind_value_2'] and full_of_value == 0:
        full_of_value = two_two_kind_info['two_kind_value_2']
    else:
        return {}

    for card in two_two_kind_info['all_cards']:
        if card not in two_two_kind_info['ordered_kickers'] and card.number == full_of_value:
            fh.append(card)
    resp = hand_val_gen(hand_rank=6,name="Full House", \
        three_kind_value=three_kind_info['three_kind_value'], two_kind_value=full_of_value)
    resp['all_cards'] = fh
    return resp

def get_straight_flush(cards):
    suit = None
    suited_cards = []
    c_by_suit = group_by_suit(cards)
    for s, cs in c_by_suit.items():
        if len(cs) >= 5:
            suit = s
            suited_cards = get_straight(cs)
    if not suited_cards:
        return {}
    resp = hand_val_gen(hand_rank=8, name='Straight Flush', \
            s_or_sf_high_card=suited_cards['s_or_sf_high_card'], \
            suit=suit)
    resp['all_cards'] = suited_cards['all_cards']
    return resp

def get_best_hand(cards):
    sf = get_straight_flush(cards)
    if sf:
        return sf

    fk = get_four_kind(cards)
    if fk:
        return fk

    fh = get_full_house(cards)
    if fh:
        return fh

    flush = get_flush(cards)
    if flush:
        return flush

    straight = get_straight(cards)
    if straight:
        return straight

    tk = get_three_kind(cards)
    if tk:
        return tk

    tk = get_three_kind(cards)
    if tk:
        return tk

    ttk = get_two_two_kind(cards)
    if ttk:
        return ttk

    two = get_two_kind(cards)
    if two:
        return two

    nh = get_no_hand(cards)
    if nh:
        return nh

# def rank_pairs()

def rank_hands(hands):
    ranked = dict((count, []) for count in range(0,9))
    final_rank = []

    for seat, hand in hands.items():
        bh = get_best_hand(hand)
        ranked[bh['hand_rank']].append({
            "seat": seat,
            "original": hand,
            "ranked": bh
            })
    for x in reversed(range(0,9)):
        if len(ranked[x]) == 1:
            final_rank.append(ranked[x][0])
        if len(ranked[x]) > 1:
            print "**"*20
            pretty(ranked[x])
    print "-"*50
    pretty(final_rank)
    # ranked = sorted(ranked, key=operator.attrgetter('ranked.hand_rank'))
    

