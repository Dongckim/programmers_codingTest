def solution(arr, intervals):
    answer = []
    [[s1, e1], [s2, e2]] = intervals
    for i in range(s1,e1+1):
        answer.append(arr[i])
    for i in range(s2,e2+1):
        answer.append(arr[i])
    return answer    
            