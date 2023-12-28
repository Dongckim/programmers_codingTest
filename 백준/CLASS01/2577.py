nums = open('input.txt', 'rt').read().split('\n')
total = 1
for num in nums:
    total *= int(num)

total = str(total)
dict = {}
for num in total:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1

num_list = [0,1,2,3,4,5,6,7,8,9]
for num in num_list:
    if str(num) in dict:
        print(dict[str(num)])
    else:
        print(0)
