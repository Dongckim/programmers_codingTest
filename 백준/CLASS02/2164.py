from collections import deque

num = int(open('input.txt', 'rt').read())
dq = deque([i+1 for i in range(num)])
while len(dq) != 1:
    dq.popleft()
    dq.append(dq[0])
    dq.popleft()
print(dq[0])