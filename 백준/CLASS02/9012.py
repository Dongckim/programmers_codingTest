num = int(open('input.txt', 'rt').read().split('\n')[0])
ps = open('input.txt', 'rt').read().split('\n')[1:]

for p in ps:
    f_ps = []
    b_ps = []
    for i, val in enumerate(p):
        if val == '(':
            f_ps.append((i, val))
        else:
            b_ps.append((i, val))
    if len(f_ps) != len(b_ps):
        print('NO')
        continue
    else:
        for i in range(len(f_ps)):
            if f_ps[i][0] > b_ps[i][0]:
                print('NO')
                break
            elif i == len(f_ps)-1:
                print(f_ps)
                print('YES')
                break