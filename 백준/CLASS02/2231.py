n = int(open('input.txt', 'rt').read())
for i in range(1, n+1):
    num = sum(list(map(int, str(i))))
    result = num + i
    if i == n:
        print(0)
    if result == n:
        print(i)
        break
