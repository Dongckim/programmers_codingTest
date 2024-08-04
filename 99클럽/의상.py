from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([kind for _, kind in clothes])
    return reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1


def solution(c):
    return reduce(lambda x,y : x*(y+1), [a for a in Counter([x[1] for x in c]).values()])-1



def solution(clothes):
    clothes_type = {}

    for _, kind in clothes:
        if kind not in clothes_type:
            clothes_type[kind] = 2
        else:
            clothes_type[kind] += 1

    count = 1
    for num in clothes_type.values():
        count *= num

    return count - 1



if __name__ == "__main__":
    import time
    import datetime
    start = time.time()


    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))


    sec = time.time() - start
    times = str(datetime.timedelta(seconds=sec))
    short = times.split('.')[0]
    print(f"{times} sec")
    print(f"{short} sec")
