num = int(open('input.txt', 'rt').read().split('\n')[0])
for i in range(num):
    k = int(open('input.txt', 'rt').read().split('\n')[i+1])
    n = int(open('input.txt', 'rt').read().split('\n')[i+2])
    people = [i for i in range(1, n+1)]
    for i in range(k):
        total = []
        for j in range(1, n+1):
            total.append(sum(people[:j]))
        people = total[:]
    print(people[-1])