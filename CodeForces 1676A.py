n = int(input())
for i in range(n):
    m = str(input())
    i = 0
    a , b = 0 , 0
    while i < 3:
        a += int(m[i])
        b += int(m[i + 3])
        i += 1
    if a == b:
        print('YES')
    else:
        print('NO')
