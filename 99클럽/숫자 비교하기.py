def solution(num1, num2):
    return 1 if num1 == num2 else -1

def solution2(num1, num2):
    return ((num1 == num2)-0.5)*2


if __name__ == "__main__":
    print(solution2(2, 3))
