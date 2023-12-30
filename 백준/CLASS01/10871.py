# _, i = list(map(int, input().split(' ')))
# num_ls = list(map(int, input().split(' ')))
_, i = list(map(int, open('input.txt', 'rt').read().split('\n')[0].split(' ')))
num_ls = list(map(int, open('input.txt', 'rt').read().split('\n')[1].split(' ')))

answer = []
for num in num_ls:
    if num < i:
        answer.append(num)
        answer.append(' ')
print(''.join(answer))

## 형변환, 출력형식