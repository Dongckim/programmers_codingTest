num = int(open("input.txt", 'rt').read().split('\n')[0])
stack_ls = list(map(int, open("input.txt", 'rt').read().split('\n')[1:]))

origin = [i+1 for i in range(num)]
stack = []
answer = []

for i in range(num):
    if len(stack_ls) == 0:
        pass
    else:
        stack.insert(0, origin[i])
        answer.append('+')
        while True:
            try:
                if stack[0] == stack_ls[0]:
                        stack_ls.pop(0)
                        stack.pop(0)
                        answer.append('-') 
                elif stack[0] > stack_ls[0]:
                    answer.append('NO') 
                    break
                else:
                    break
            except:
                 break
    
if 'NO' in answer:
     print('NO')
else:
    [print(i) for i in answer]