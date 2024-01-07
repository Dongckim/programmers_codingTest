import math 

n = int(open('input.txt', 'rt').read())

div = [1]
for i in range(1, n+1):
    num = i*6 + div[-1]
    if n <= div[-1]:
        print(len(div))
        break
    else:
        div.append(num)
        if i == (math.ceil(n/6)+1):
            print(len(div))
            break


# answer, ans = [], []
# for i in range(1, n+1):
#     if i not in div:
#         ans.append(i)
#         if i == n:
#             answer.append(ans)
#         else:
#             continue
#     if i in div:
#         ans.append(i)
#         answer.append(ans)
#         ans = []
#         continue

# print(len(answer))