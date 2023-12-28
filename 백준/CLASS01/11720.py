a, b = open('input.txt', 'rt').readlines()
a, b = int(a.rstrip('\t')), b

sum = 0
for i in range(a):
    sum += int(b[i])


print(sum)