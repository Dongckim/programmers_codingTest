num = open('input.txt', 'rt').read()
for i in range(int(num)-1,-1,-1):
    print(i*" " + (int(num)-i)*'*')