class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)

        if self.top:            #스택이 비어있지 않다면
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None

        data = self.top.data # 1
        self.top = self.top.next # 2
        self.size -= 1
        return data


    def peek(self):
        if self.size == 0:
            return None
        return self.top.data


    def print(self):
        current = self.top
        string = ""
        while current:
            string += str(current.data)
            if current.next:
                string += "->"
            current = current.next
        print(string)


def original_solution(s):
    stack = Stack()
    for brkt in s:
        if brkt == "(":
            stack.push(brkt)
        if brkt == ")":
            last = stack.pop()
            if last == '(' and brkt == ')':
                continue
            else:
                return False

    if stack.size > 0:
        return False
    else:
        return True

# ----------------------------------------------


def answer_solution(s):
    check = []
    for i in s:
        if i == "(":
            check.append(i)
        else:
            try:
                check.pop()
            except:     #IndexError
                return False
    if len(check) != 0:
        return False
    else:
        return True

# ----------------------------------------------

from functools import reduce
def unique_solution(s):
    return reduce(lambda a, b: a+'\r' if b == '(' else a[:-1], list(s), s) == s


# == 비교의 시간복잡도???

# ----------------------------------------------


if __name__ == "__main__":
    import time
    import datetime

    # 이미 정렬된 리스트
    list1 = [1, 2, 3, 4, 5]
    print('dd',sorted(list1) == list1)  # True

    # 정렬되지 않은 리스트
    list2 = [3, 1, 4, 2, 5]
    print('dd',list2.sort() == list2)  # False


    start = time.time()
    print(original_solution("((((())))((((((((())))((((((())))))(((((("))
    sec = time.time() - start

    times = str(datetime.timedelta(seconds=sec))
    short = times.split('.')[0]
    print(f"{times} sec")
    print(f"{short} sec")


# 스택 활용의 예시 (후입 선출)
# 웹 브라우저 방문 기록
# 역순 문자열 만들기
# 실행취소(undo)
# 후위 표기법 계산
# 수식의 괄호 검사(연산자 우선순위 표현을 위한 괄호 검사)

# 큐의 예시
# 우선순위가 같은 작업 예약 (대기열)
# 은행 업무
# 콜센터 고객 대기시간
# 프로세스 관리
# 너비 우선 탐색
# 캐시(cache) 구현