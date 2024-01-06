input = open('input.txt', 'rt').read().split('\n')

for sentence in input:
    new_s =[]
    for word in sentence:
        new_s += list(word)
    if new_s == ['.']:
        break
    else:
        dict = {'(' : [], ')':[], '[' : [], ']' : []}
        for i, char in enumerate(new_s):
            if char == '(':
                dict['('].append(i)
            elif char == ')':
                dict[')'].append(i)
            elif char == '[':
                dict['['].append(i)
            elif char == ']':
                dict[']'].append(i)

        if (len(dict['(']) == len(dict[')'])) and (len(dict['[']) == len(dict[']'])):
            for j in range(len(dict['('])):
                for k in range(len(dict['['])):
                    if dict['('][j] < dict[')'][j] and dict['['][k] < dict[']'][k]:
                        pass
                    elif dict[')'][j] > dict['['][k]:
                        print('no')
                        break
                    else:
                        print('no')
                        break
            print('yes')
        
        else:
            print('no')
