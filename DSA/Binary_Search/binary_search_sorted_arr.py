arr = [-7,-5,-4,-3,-1,0,1,2,4,6,8,9]

target = 6

def find_index(arr, target):

    n = len(arr)
    
    if n==0:
        return -1
    
    left = 0
    right = n-1

    while left <= right:
        middle = left + ((right-left)//2)

        if arr[middle] == target:
            return middle
        
        elif arr[middle] < target:
            left = middle + 1
        
        else:
            right = middle - 1
        
    return -1

result = find_index(arr, target)
print(result)
