def is_composite(x):
    if x <= 3:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return True
    return False

n = int(input())
for a in range(4, n):
    b = n - a
    if is_composite(a) and is_composite(b):
        print(a, b)
        break
