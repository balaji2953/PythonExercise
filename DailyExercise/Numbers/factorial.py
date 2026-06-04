def factorial(num):

    if num < 0:
        return -1

    if num == 0 or num == 1:
        return 1
    
    # use recursive 

    return (num * (num-1))

if __name__ == "__main__":
    print(factorial(1))
    print(factorial(-10))
    print(factorial(100))
