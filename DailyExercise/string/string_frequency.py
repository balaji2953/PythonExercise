def string_frequency(string):
    
    if not string:
        return {}
    
    freq={}

    for ch in string:
        c = ch.lower()
        freq[c]= freq.get(c, 0) + 1
    
    return freq

if __name__ == "__main__":
    print(string_frequency("programming"))
    print(string_frequency("Programming"))
