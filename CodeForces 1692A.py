n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    c = 0
    for i in a:
        if i > a[0]:
            c += 1
    print(c)
