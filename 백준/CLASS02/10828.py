num = int(open('input.txt', 'rt').read().split('\n')[0])
commands = open('input.txt', 'rt').read().split('\n')[1:]

arr = []
for com in commands:
    if len(com.split(' ')) == 2:
        cmd, i = com.split(' ')
        if cmd == 'push':
            arr.insert(0, i)
    else:
        cmd = com
        if cmd == 'pop':
            if len(arr) == 0:
                print(-1)
            else:
                print(arr.pop())
        elif cmd == 'size':
            print(len(arr))
        elif cmd == 'empty':
            if len(arr) == 0:
                print(1)
            else:
                print(0)
        elif cmd == 'front':
            if len(arr) == 0:
                print(-1)
            else:
                print(arr[-1])
        elif cmd == 'back':
            if len(arr) == 0:
                print(-1)
            else:
                print(arr[0])