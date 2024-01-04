from itertools import combinations
_, cri = list(map(int, open('input.txt', 'rt').read().split('\n')[0].split(' ')))
nums = list(map(int, open('input.txt', 'rt').read().split('\n')[1].split(' ')))

result = 0
for num in combinations(nums, 3):
    if sum(list(num)) <= cri and result < sum(list(num)):
        result = sum(list(num))
print(result)