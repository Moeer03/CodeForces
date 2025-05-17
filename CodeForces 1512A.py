t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Determine the majority element from first three
    if a[0] == a[1] or a[0] == a[2]:
        majority = a[0]
    else:
        majority = a[1]

    # Find and print the 1-based index of the unique element
    for i in range(n):
        if a[i] != majority:
            print(i + 1)
            break
