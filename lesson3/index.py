def GTLN(a, b, c, d):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    if d > max:
        max = d
    return max

a= GTLN(2, 5, 7, 3)
print(a)