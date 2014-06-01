def longest_sequence(ls):
    """
    Params =  a list of numbers
    returns a tuple of the length of the seq. and the longest sequence
    """
    sequences = []
    current_sequence = []
    for location, num in enumerate(sorted(ls)):
        if location +1 >= len(ls):
            break
        next_location = location + 1
        next_num = ls[next_location]
        if num + 1 == next_num:
            if num not in current_sequence:
                current_sequence.append(num)
            if next_num not in current_sequence:
                current_sequence.append(next_num)
        else:
            sequences.append((len(current_sequence), current_sequence))
            current_sequence = []
    if max(sequences)[0] == 0:
        return (len(current_sequence), current_sequence)
    return max(sequences)

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