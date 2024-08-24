# from collections import deque
#
#
# def calculate_distances(N, connections):
#     # 각 파이프의 연결 정보를 저장할 인접 리스트
#     adj = [[] for _ in range(N + 1)]
#
#     # 주어진 연결 정보에 따라 인접 리스트를 채움
#     for E, B1, B2 in connections:
#         adj[E].append(B1)
#         adj[E].append(B2)
#         adj[B1].append(E)
#         adj[B2].append(E)
#
#     print(adj)
#     # 거리를 저장할 배열 (거리 초기값은 -1로 설정)
#     distance = [-1] * (N + 1)
#     distance[1] = 1  # 파이프 1번의 거리는 1로 설정
#
#     # BFS 사용
#     queue = deque([1])
#
#     while queue:
#         current = queue.popleft()
#         current_distance = distance[current]
#
#         for neighbor in adj[current]:
#             if distance[neighbor] == -1:  # 아직 방문하지 않은 파이프
#                 distance[neighbor] = current_distance + 1
#                 queue.append(neighbor)
#
#     return distance
#
#
# # 테스트 입력
# N = 5
# connections = [
#     (1, 2, 3),
#     (3, 4, 5)
# ]
#
# distances = calculate_distances(N, connections)
#
# # 파이프 번호 1~N에 대한 거리를 출력
# for i in range(1, N + 1):
#     print(f"Pipe {i} is distance {distances[i]} from the barn.")

import sys
from collections import deque


def bfs(tree, n):
    # 1번 노드에서 각 노드까지의 거리를 저장할 배열
    distances = [-1] * (n + 1)  # 왜 0이 아닌 -1인기? : 0으로하면 미방문 내역은 확인하기 힘드니깐
    distances[1] = 1  # 1번 노드는 루트이므로 거리 1

    queue = deque([1])  # BFS 탐색을 위한 큐, 루트부터 시작

    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if distances[neighbor] == -1:  # 방문하지 않은 노드만 처리
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    return distances[1:]


def main():
    n, c = map(int, input().split())
    tree = [[] for _ in range(n + 1)]

    for _ in range(c):
        e, b1, b2 = map(int, input().split())
        tree[e].append(b1)
        tree[e].append(b2)
        tree[b1].append(e)
        tree[b2].append(e)

    result = bfs(tree, n)

    for distance in result:
        print(distance)


if __name__ == "__main__":
    main()

# import sys
#
# N, C = map(int, sys.stdin.readline().split())
#
# array = [0] * (N + 1)
# for _ in range(C):
#     root, left, right = map(int, sys.stdin.readline().split())
#     array[left] = root
#     array[right] = root
#
#
# def dfs(p, cnt):
#     if p == 1: return cnt
#     return dfs(array[p], cnt + 1)
#
#
# for i in range(1, N + 1):
#     print(dfs(i, 1))
