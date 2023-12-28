num_list = list(map(int, open('input.txt', 'rt').read().split(' ')))
for i in range(7):
    if abs(num_list[i] - num_list[i+1]) != 1:
        print('mixed')
        break
    if i == 6:
        if num_list[i] > num_list[i + 1]:
            print('descending')
            break
        else:
            print('ascending')
            break