k, m = list(map(int, open('input.txt', 'rt').read().split(' ')))

def find_prime(num):
    if num == 1:
            return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(k, m+1):
    if find_prime(i):
        print(i)
