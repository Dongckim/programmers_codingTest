k, m = list(map(int, open('input.txt', 'rt').read().split(' ')))

def find_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in range(k, m):
    if find_prime(i):
        print(i)

