rg = int(open('input.txt', 'rt').read().split('\n')[0])
nums = list(map(int, open('input.txt', 'rt').read().split('\n')[1:]))

answer = []

for i in range(rg):
    if nums[i] != 0:
        answer.append(nums[i])
        print(answer)
    else:
        answer.pop()

print(answer)