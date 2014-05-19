def longest_sequence(ls):
    sequences = []
    current_sequence = []
    for location, num in enumerate(ls):
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




# if __name__ == '__main__':
#     print longest_sequence([
#         1,
#         2,
#         3,
#         4,
#         5,
#         8,
#         9,
#         12])