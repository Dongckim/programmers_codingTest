lst = list(map(lambda x: list(map(int, x.split())), open('input.txt', 'rt').read().split('\n')))
for l in lst:
    st = sorted(l)
    if 0 in st:
        break
    elif st[0]**2 + st[1]**2 == st[2]**2:
        print('right')
    else:
        print('wrong')