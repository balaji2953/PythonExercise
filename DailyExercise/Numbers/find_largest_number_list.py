def find_largest_num(arr):
    if not arr:
        return None

    largest = arr[0]

    for num in arr[1:]:
        if num > largest:
            largest = num

    return largest


def find_second_largest(arr):
    if len(arr) < 2:
        return None

    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num

    return second_largest

if __name__ == "__main__":
    print(find_largest_num([4,2,7,1,9]))
    print(find_second_largest([4,2,7,1,9]))
