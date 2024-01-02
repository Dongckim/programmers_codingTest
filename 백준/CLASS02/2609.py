a, b = list(map(int, open('input.txt', 'rt').read().split(' ')))
if a > b:
    a, b = b, a

for i in range(a, -1, -1):
    if a%i == 0 and b%i ==0:
        print(i)
        break
    
i = 1
while True:
    if a*i%b == 0:
        print(a*i)
        break
    else:
        i+=1   