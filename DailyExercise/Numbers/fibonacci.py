def fibonacci(n):
    if n <= 0:
        return []

    result = []
    a, b = 0, 1

    for _ in range(n):
        result.append(a)
        a, b = b, a + b

    return result

def using_generator_create_fibonacci(num):
    def fibonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    # Get first 100 Fibonacci numbers
    gen = fibonacci()
    for _ in range(num):
        print(next(gen), end=" ")


if __name__ == "__main__":
    print(fibonacci(5))
    using_generator_create_fibonacci(10)
