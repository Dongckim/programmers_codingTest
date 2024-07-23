def solution(num1, num2):
    answer = num1//num2
    return answer


def solution2(num1,num2):
    answer = num1 / num2
    return int(answer)


def solution3(num1,num2):
    return divmod(num1, num2)[0]

solution = int.__floordiv__


if __name__ == "__main__":
    print(solution(7, 4))
