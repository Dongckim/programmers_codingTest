num = open('input.txt', 'rt').read().split('\n')[0]
input = open('input.txt', 'rt').read().split('\n')[1:]

for i in range(int(num)):
    oos = input[i].split('X')
    total = 0
    for oo in oos:
        for i, _ in enumerate(oo):
            total += i+1
    print(total)
