t = int(input())
a = list(map(int , input().split()))
b = max(a)
s = 0
for i in a:
    s += (b - i)
print(s)
