def count_vowels(string):

    if not string:
        return []
    
    vowels = []
    
    for ch in string:
        if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        # if ch.lower() in 'aeiou':
            vowels.append(ch)

    return vowels

if __name__ == "__main__":
    print(count_vowels("python"))
