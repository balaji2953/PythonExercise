def count_upper_and_lower_case(string):
    if not string:
        return 0, 0

    upper, lower = 0, 0

    for ch in string:

        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    return upper, lower 

def count_upper_and_lower_case_combination_of_multi_values(string):
    if not string:
        return 0, 0

    upper, lower = 0, 0

    for ch in string:
        if ch.isalpha():
            if ch.isupper():
                upper += 1
            elif ch.islower():
                lower += 1

    return upper, lower


if __name__ == "__main__":
    # u , l = count_upper_and_lower_case("pyTHon")
    u , l = count_upper_and_lower_case_combination_of_multi_values("pyTon1231")

    print(f"Upper: {u}")
    print(f"Lower: {l}")
