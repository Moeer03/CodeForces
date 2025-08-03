t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    max_blank = 0
    current_blank = 0

    for num in a:
        if num == 0:
            current_blank += 1
            max_blank = max(max_blank, current_blank)
        else:
            current_blank = 0

    print(max_blank)
