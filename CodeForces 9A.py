from math import gcd

y, w = map(int, input().split())
max_val = max(y, w)
favorable_outcomes = 6 - max_val + 1
common_divisor = gcd(favorable_outcomes, 6)
print(f"{favorable_outcomes // common_divisor}/{6 // common_divisor}")
