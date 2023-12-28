num = int(open('input.txt', 'rt').read().split('\n')[0])
lst = open('input.txt', 'rt').read().split('\n')[1:]

for i in range(num):
    a, b = lst[i].split(' ')
    new_word = ''
    for j, char in enumerate(b):
        new_word += char*int(a)
    print(new_word)