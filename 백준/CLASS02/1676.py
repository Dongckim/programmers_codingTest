def factorial(x):
    a = 1
    for i in range(1, x+1):
        a*=i
    return a

n = list(str(factorial(int(open('input.txt', 'rt').read()))))

answer= []
for i in range(len(n)-1,-1,-1):
    if n[i] == '0':
        answer.append(0)
    else:
        print(len(answer))
        break