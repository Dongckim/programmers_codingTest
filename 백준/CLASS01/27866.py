word,  idx = open('input.txt', 'rt').readlines()

word, idx = word.rstrip('\t'), int(idx)
print(word[idx-1])