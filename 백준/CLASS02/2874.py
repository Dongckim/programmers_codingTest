num = int(open("input.txt", 'rt').read().split('\n')[0])
stack_ls = list(map(int, open("input.txt", 'rt').read().split('\n')[1:]))

origin = [i+1 for i in range(num)]
stack = []
answer = []

for i in range(num):
    if len(stack) == 0:
        pass
    if stack_ls[i] != origin[i]: #오리진이랑 다르면
        stack.insert(0, stack_ls[i])
        
    else:   #오리진이랑 같으면, 
        if len(stack) != 0:
            answer.append(stack.pop(0))
print(stack_ls)