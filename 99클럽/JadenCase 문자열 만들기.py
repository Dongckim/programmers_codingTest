def solution(s):                 # s.title() 안됨.
    answer = list(s.title())
    i = 0
    while i != len(answer):
        if answer[i].isdigit():
            answer[i+1] = answer[i+1].lower()
            i += 1
        i+=1
    return ''.join(answer)



def solution5(s):                # capitalize()
    return ' '.join([word.capitalize() for word in s.split(" ")])


def jaden_case(s):
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = s[i][0].upper() + s[i][1:].lower()
        print(s[i])
    return " ".join(s)

# def solution0(s):
#     lst = map((lambda x : str(x[0].upper()) + str(x[1:].lower())), s.split(" "))
#     answer = " ".join(lst)
#     return answer



if __name__ == "__main__":
    import time
    import datetime


    start = time.time()
    print(solution("3people unFollowed me"))
    sec = time.time() - start

    times = str(datetime.timedelta(seconds=sec))
    short = times.split('.')[0]
    print(f"{times} sec")
    print(f"{short} sec")