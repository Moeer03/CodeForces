t = int(input())
for _ in range(t):
    n = list(map(int,input().split()))
    n.sort()
    print(n[1])
