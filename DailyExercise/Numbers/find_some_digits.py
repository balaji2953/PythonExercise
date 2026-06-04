def sum_of_digits(num):
    num = abs(num)

    total = 0

    while num:
        total += num % 10
        num //= 10

    return total

if __name__ == "__main__":
    print(sum_of_digits(1234))
