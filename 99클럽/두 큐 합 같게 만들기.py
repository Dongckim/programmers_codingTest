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



def solution(lst1, lst2):
    answer = 0
    q1, q2 = Queue(), Queue()
    [q1.enqueue(i) for i in lst1]
    [q2.enqueue(i) for i in lst1]

    sum1 = sum(lst1)
    sum2 = sum(lst2)

    # 홀수인 경우
    if (sum1 + sum2) % 2 != 0:
        return -1

    while True:
        if answer == 4 * q1.size:
            return -1

        if sum1 > sum2:
            value = q1.dequeue()
            q2.enqueue(value)
            sum1 -= value
            sum2 += value
        elif sum1 < sum2:
            value = q2.dequeue()
            q1.enqueue(value)
            sum1 += value
            sum2 -= value
        else:
            return answer
        answer += 1


if __name__ == "__main__":
    import time
    import datetime
    start = time.time()


    print(solution([3, 2, 7, 2], [4, 6, 5, 1]))


    sec = time.time() - start
    times = str(datetime.timedelta(seconds=sec))
    short = times.split('.')[0]
    print(f"{times} sec")
    print(f"{short} sec")