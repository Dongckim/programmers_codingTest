num = open('input.txt', 'rt').read().split('\n')[0]
nums = open('input.txt', 'rt').read().split('\n')[1].split(' ')

def find_prime(num):
    if num == 1:
            return False
    for i in range(1, num):
        if num % i == 0:
            return False
    return True
print(nums)
print([j for j in nums if find_prime(int(j))])

print(list(map(lambda x : find_prime(int(x)) == True, nums)))
print(len(list(map(lambda x : find_prime(int(x)) == True, nums))))