nums = list(map(int, open('input.txt', 'rt').read().split('\n')[1].split(' ')))
max_v = max(nums)
new = sum([num/max_v*100 for num in nums])
print(new/len(nums))