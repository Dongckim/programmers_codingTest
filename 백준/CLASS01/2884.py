input = open('input.txt', 'rt').read().split()
h, m = map(int, input)
if m - 45 < 0:
    m = 60 + (m -45)
    h -= 1
    if h < 0:
        h += 24
else:
    m -= 45
    
print(h,m)