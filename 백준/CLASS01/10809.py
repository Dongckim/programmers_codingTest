word = open('input.txt', 'rt').read()
alphabet = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
answer = ''
for i, char in enumerate(alphabet):
    if char in word:
        answer += str(word.index(char))
        answer += ' '
    else:
        answer += '-1'
        answer += ' '

print(answer)