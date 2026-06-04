import math

def check_is_prime_number(num):
    
    if num <= 1:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True

def is_prime_without_sqrt(n):
    
    if n <= 1:
        return False

    i = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True
    
if __name__ == "__main__":
    print("isPrime" if check_is_prime_number(10) else "isNotPrime")
    print("isPrime" if is_prime_without_sqrt(7) else "isNotPrime")
