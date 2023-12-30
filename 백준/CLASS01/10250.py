num = int(open("input.txt", 'rt').read().split('\n')[0])
tests = open("input.txt", 'rt').read().split('\n')[1:]

for i in range(num):
    test = list(map(int, tests[i].split(' ')))
    H, W, client = test[0], test[1], test[2]
    floor, room_num = 0, 0

    if client%H == 0:
        floor = str(H)
        room_num  = str(client//H).split()
    else:
        floor = str(client%H)
        room_num = str(client//H+1).split()

    if len(room_num[0]) != 2:
        room_num.insert(0, '0')
        print(floor + ''.join(room_num))
    else:
        print(floor + ''.join(room_num))