k, m = list(map(int, open('input.txt', 'rt').read().split('\n')[0].split(' ')))
lines = list(map(int, open('input.txt', 'rt').read().split('\n')[1:]))

answer = []
def find_length(start, end):
    while (start <= end):
        mid = (start + end) // 2
        total = 0
        for num in lines:
            total += num//mid

        if total >= m:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(find_length(1, max(lines)))





# k, n = map(int, sys.stdin.readline().split())
# arr = []

# for i in range(k):
#     arr.append(int(input()))

# start = 1
# end = max(arr)

# while (start <= end):
#     mid = (start + end) // 2
#     cnt = 0
#     for i in range(k):
#         cnt += arr[i] // mid
#     if cnt >= n:
#         start = mid + 1
#     else:
#         end = mid - 1
# print(end)