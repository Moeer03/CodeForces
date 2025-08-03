t = int(input())
for _ in range(t):
    n = int(input())
    a = str(input())
    
    # Calculate the sum of the array
    s1 = 0
    i = 0
    while i < n:
        j = 0
        s = 0
        if a[i] == '0':
            s += 1
            while (i + j < n):
                if a[j] == '0':
                    s += 1
                    j += 1
                else:
                    i = j
                    break
            if s > s1:
                s1 = s
    print(s1)
