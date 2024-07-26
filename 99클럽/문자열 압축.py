

def solution(data):
    n = 1   #2개씩 짤라보기
    boool = True
    dic_lst = []
    while boool:
        word = ''
        temp = ''
        temp2 = ''
        count_dic = dict()
        for i in range(0, len(data), n):
            temp = data[i:i + n]
            temp2 = data[i+n: i+n+n]
            if temp == temp2:
                if temp not in count_dic:
                    count_dic[temp] = 1
                else:
                    count_dic[temp] += 1
            else:
                word += temp
                print(word)
        break

        if count_dic != {}:
            dic_lst.append(count_dic)

        if len(data) == n:
            boool = False
        n += 1

    return dic_lst


if __name__ == "__main__":
    import time
    import datetime


    start = time.time()
    print(solution("abcabcabcabcdededededede"))
    sec = time.time() - start

    times = str(datetime.timedelta(seconds=sec))
    short = times.split('.')[0]
    print(f"{times} sec")
    print(f"{short} sec")