def solution(n):
    return list(map(int, reversed(str(n))))


def solution2(n):
    arr = list(str(n))[::-1]
    return list(map(int, arr))


if __name__ == "__main__":
    print(solution2(23))
