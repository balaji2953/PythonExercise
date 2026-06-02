def reverse_string(string):
    print(string[::-1])

def reverser_string_using_for_loop(string):
    for i in range(len(string)-1,-1,-1):
        print(string[i], end="")

if __name__ == "__main__":
    reverse_string("python")
    reverser_string_using_for_loop("programming")
