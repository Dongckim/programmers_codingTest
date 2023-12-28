num_lst = map(int, open('input.txt', 'rt').read().split('\n'))
total = []
for num in num_lst:
    if num % 42 not in total:
        total.append(0)

print(len(total))