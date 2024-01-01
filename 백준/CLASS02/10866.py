num = int(open('input.txt', 'rt').read().split('\n')[0])
commands = open('input.txt', 'rt').read().split('\n')[1:]

arr = []
for com in commands:
    print(com.split(' '))
    if len(com.split(' ')) == 2:
        cmd, i = com.split(' ')
        i = int(i)
        if cmd == 'push_back':
            arr.append(i)
        elif cmd == 'push_front':
            arr.insert(0, i)
    else:
        cmd = com
        if cmd == 'pop_front':
            if len(arr) == 0:
                print(-1)
            else:
                print(arr.pop(0))
        elif cmd == 'pop_back':
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
                print(arr[0])
        elif cmd == 'back':
            if len(arr) == 0:
                print(-1)
            else:
                print(arr[-1])
