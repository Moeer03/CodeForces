a = list(map(int , input().split()))
a.sort()
a[1] = a[1] - a[0]
print(a[0] , a[1] // 2)
