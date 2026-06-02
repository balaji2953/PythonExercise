str = "programming"

def find_non_repeating_index_approach_1(str):
    rep ={}
    for ch in str:
        rep[ch] = rep.get(ch, 0) + 1
    
    index = 0
    for ch in str:
        if rep[ch] == 1:
            return index
        index += 1

    return -1

def find_non_repeating_index_approach_2(s):
    
    for index, ch in enumerate(s, start=0):
        count = 0
        count = s.count(ch)

        if count == 1:
            return index

    return -1

print(f"First Non-repeating Character Index: {find_non_repeating_index_approach_1(str)}")
