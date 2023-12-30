num = open('input.txt', 'rt').read().split('\n')[0]
words = open('input.txt', 'rt').read().split('\n')[1:]

print(sorted(list(set(words)), key = lambda x : (len(x), x)))
