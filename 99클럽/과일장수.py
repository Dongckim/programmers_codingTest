def solution(k, m, score):
    result = 0
    score.sort(reverse = True)
    for i in range(m - 1, len(score), m):
        result += score[i] * m

    return result


if __name__ == "__main__":
    import time
    import datetime
    start = time.time()
    print(solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
    sec = time.time() - start

    times = str(datetime.timedelta(seconds=sec))
    short = times.split('.')[0]
    print(f"{times} sec")
    print(f"{short} sec")