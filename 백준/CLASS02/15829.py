n = int(open('input.txt', 'rt').read().split('\n')[0])
word = list(open('input.txt', 'rt').read().split('\n')[1])
hash = list('abcdefghijklmnopqrstuvwxyz')
dict = {}
for i, v in enumerate(hash):
    dict.setdefault(v, i+1)

default_hash = 0
for i, char in enumerate(word):
    default_hash += dict[char]*pow(31, i)%1234567891
print(default_hash)