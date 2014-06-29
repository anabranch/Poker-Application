def longest_sequence(ls):
    """
    Params =  a list of numbers
    returns a tuple of the length of the seq. and the longest sequence
    """
    sequences = []
    current_sequence = []
    for location, num in enumerate(sorted(ls)):
        if location + 1 >= len(ls):
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
    sequences.append((len(current_sequence), current_sequence))
    if max(sequences)[0] == 0:
        return (len(current_sequence), current_sequence)
    return max(sequences)

def pretty(d, indent=1):
    """Prints a dictionary in JSON like format"""
    if isinstance(d, dict):
        for key, value in d.iteritems():
            print '\t' * indent + str(key)
            if isinstance(value, dict):
                pretty(value, indent+1)
            else:
                print '\t' * (indent+1) + str(value)
    elif isinstance(d, list):
        for val in d:
            pretty(val)
    else:
        print '\t' * (indent+1) + str(d)
