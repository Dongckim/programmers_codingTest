class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue(object):
    def __init__(self):
        self.top = None
        self.last = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)

        if self.top is None:
            self.top = node
            self.last = node
        else:
            self.last.next = node
            self.last = self.last.next
        self.size += 1

    def dequeue(self):
        if self.top is None:
            self.last = None
            return None

        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    # 출력
    def print(self):
        current = self.top
        string = ""
        while current:
            string += str(current.data)
            if current.next:
                string += "->"
            current = current.next
        print(string)

    def peek(self):
        if self.size == 0:
            return None
        return self.top.data


def complete_work_data(prog, rate):
    rem = 100 - prog
    return math.ceil(rem / rate)


def solution(progresses, speeds):
    days = Queue()
    answer = []

    for i in range(len(progresses)):
        days.enqueue(complete_work_data(progresses[i], speeds[i]))

    while days.size:
        current_day = days.peek()
        count = 0

        while days.size and days.peek() <= current_day:
            days.dequeue()
            count += 1
        answer.append(count)
    return answer

# ------------------------------------------------------------
# class ListQueue(object):
#     def __init__(self):
#         self.queue = []
#
#     def dequeue(self):
#         if len(self.queue) == 0:
#             return -1
#         return self.queue.pop(0)
#
#     def enqueue(self, n):
#         self.queue.append(n)
#         pass
#
#     def printQueue(self):
#         print(self.queue)


# ------------------------------------------------------------


import math


def complete_work_data(prog, rate):
    rem = 100 - prog
    return math.ceil(rem / rate)


def logic_dividing_solution(progresses, speeds):
    answer = []
    days = []

    for i in range(len(progresses)):
        days.append(complete_work_data(progresses[i], speeds[i]))


    while days:
        current_day = days[0]
        count = 0
        while days and days[0] <= current_day:
            days.pop(0)
            count += 1
        answer.append(count)

    return answer

# ------------------------------------------------------------

from math import ceil


def using_map_solution(progresses, speeds):
    days = list(map(lambda x: (ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
    count = 1
    answer = []

    while days:
        current_day = days[0]
        count = 0
        while days and days[0] <= current_day:
            days.pop(0)
            count += 1
        answer.append(count)

    return answer

# ------------------------------------------------------------

if __name__ == "__main__":
    import time
    import datetime
    start = time.time()


    print(solution([93, 30, 55], [1, 30, 5]))


    sec = time.time() - start
    times = str(datetime.timedelta(seconds=sec))
    short = times.split('.')[0]
    print(f"{times} sec")
    print(f"{short} sec")
