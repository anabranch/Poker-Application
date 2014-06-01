def card_value_dict(**kwargs):
    dic = {
        "hand_type": None,
        "rank": None,
        "suit": None,
        "cards": [],
        "trip_number": None,
        "quad_number": None,
        "pair_number": None,
        "pair_number_2": None,
        "kicker_1": None,
        "kicker_2": None,
        "kicker_3": None,
        "kicker_4": None,
        "kicker_0": None
    }
    for name, val in kwargs.items():
        dic[name] = val
    return dic

# def pair(cards):
