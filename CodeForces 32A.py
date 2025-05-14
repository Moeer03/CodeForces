n = str(input())
i = 0
r = ''
while i < len(n):
    if n[i] == '.':
        r += '0'
        i += 1
    elif (n[i] == '-') and (n[i + 1] =='.'):
        r += '1'
        i += 2
    elif (n[i] == '-') and (n[i + 1] == '-'):
        r += '2'
        i += 2
print(r)
