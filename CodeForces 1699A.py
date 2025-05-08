n = int(input())
for i in range(n):
    a = int(input())
    if a < 1400:
        print('Division 4')
    elif 1400 <= a <= 1599:
        print('Division 3')
    elif 1600 <= a <= 1899:
        print('Division 2')
    else:
        print('Division 1')
