def remove_duplicates(li):

    if not li:
        return []
    
    new_li=[i for i in li if i not in new_li]

    return new_li

if __name__ == "__main__":
    remove_duplicates([1,2,3,1,5,1,2,0])
        