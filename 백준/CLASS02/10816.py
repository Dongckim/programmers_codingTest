num1 = int(open('input.txt', 'rt').read().split('\n')[0])
cards = list(map(int, open('input.txt', 'rt').read().split('\n')[1].split(' ')))
num2 = int(open('input.txt', 'rt').read().split('\n')[2])
card_nums = list(map(int, open('input.txt', 'rt').read().split('\n')[3].split(' ')))

dict = {}

for card in cards:
    if card not in dict:
        dict[card] = 1
    else:
        dict[card] += 1

answer = []
for card in card_nums:
    try:
        answer.append(str(dict[card]))
    except KeyError:
        answer.append('0')

print(' '.join(answer))