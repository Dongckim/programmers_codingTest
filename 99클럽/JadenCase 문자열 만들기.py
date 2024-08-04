def solution(s):                 # s.title() 안됨. 왜 안될까 고민해보기
    answer = list(s.title())
    i = 0
    while i != len(answer):
        if answer[i].isdigit():
            answer[i+1] = answer[i+1].lower()
            i += 1
        i+=1
    return ''.join(answer)


def solution1(s):                # capitalize()
    return ' '.join([word.capitalize() for word in s.split(" ")])


def solution2(s):
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = s[i][0].upper() + s[i][1:].lower()
    return " ".join(s)


def solution3(s):                 # map() + upper() + lower()
    return " ".join(map(lambda x: x[0].upper() + x[1:].lower() if x else "", s.split(" ")))


def solution4(s):                 # map() + capitalize()
    return " ".join(map(lambda x: x.capitalize() if x else "", s.split(" ")))


# upper() + lower()과 Capitalize() 무슨 차이가 있을까 고민해보기


if __name__ == "__main__":
    import time
    import datetime


    start = time.time()
    print(solution3("3people unFollowed me"))
    sec = time.time() - start

    times = str(datetime.timedelta(seconds=sec))
    short = times.split('.')[0]
    print(f"{times} sec")
    print(f"{short} sec")