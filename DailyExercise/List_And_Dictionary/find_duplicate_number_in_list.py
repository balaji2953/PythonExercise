def find_duplicates(li):
    
    if not li:
        return []
    
    duplicate = []
    temp = []

    for i in li:
        if i not in temp:
            temp.append(i)
        
        else:
            duplicate.append(i)
    
    return list(set(duplicate))

if __name__ == "__main__":
    print(find_duplicates([1,2,3,1,5,1,2,0]))
