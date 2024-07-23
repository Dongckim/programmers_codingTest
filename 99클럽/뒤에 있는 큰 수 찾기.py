def find_large(lst, num):
    for i in lst:
        if num < i:
            return i



def solution(numbers):
    answer = []
    for idx, num in enumerate(numbers):
        if idx == len(numbers)-1:
            answer.append(-1)
        else:
            if not find_large(numbers[idx+1:], num):
                answer.append(-1)
            else:
                answer.append(find_large(numbers[idx+1:], num))
    return answer


if __name__ == "__main__":
    print(solution([9, 1, 5, 3, 6, 2]))