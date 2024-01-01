n,m = list(map(int, open('input.txt', 'rt').read().split('\n')[0].split(' ')))
matrix = list(map(list, open('input.txt', 'rt').read().split('\n')[1:]))

answer = []
sample = None
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        sample = [mat[j:j+8]for mat in matrix[i:i+8]]
        for_B , for_W = 0, 0
        for k in range(8):
            for l in range(8):
                if (k+l) % 2 == 0:
                    if sample[k][l] != 'W':
                        for_B += 1
                    if sample[k][l] != 'B':
                        for_W += 1
                else:
                    if sample[k][l] != 'B':
                        for_B += 1
                    if sample[k][l] != 'W':
                        for_W += 1
        answer.append(min(for_B, for_W))  
print(min(answer))