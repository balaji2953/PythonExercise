v = int(input())
s = int(input())

if 1 <= v <= 30:
    vertex = []
    
    # Generate all pair sums from 1 to v
    for i in range(1, v):
        for j in range(i + 1, v + 1):
            vertex.append(i + j)
    
    output_count = 0

    # 1. Check for unique pairs in 'vertex' that sum up to 's'
    seen = set()
    pairs_found = set()

    for num in vertex:
        target = s - num
        if target in seen:
            pair = tuple(sorted((num, target)))
            pairs_found.add(pair)
        seen.add(num)

    output_count += len(pairs_found)

    # 2. Count how many times 's' itself appears in the vertex list
    # (Replaces your original single-element checking logic safely)
    output_count += vertex.count(s)

    print(output_count)

else:
    print("Invalid Input")
