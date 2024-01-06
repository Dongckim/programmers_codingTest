'''
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
'''
n = int(open('input.txt', 'rt').read().split('\n')[0])
nums = list(map(int, open('input.txt', 'rt').read().split('\n')[1:]))
print(round(sum(nums)/len(nums)))

dic = {}
for num in nums:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

nums = sorted(nums)
print(nums[n//2])

max_v = max(dic.values())
candidate = sorted([k for k, v in dic.items() if v == max_v])
print(candidate[0] if len(candidate) == 1 else candidate[1])

print(nums[-1]-nums[0])