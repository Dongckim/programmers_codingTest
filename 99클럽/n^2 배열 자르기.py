def solution(n, left, right):
    lst = []
    for i in range(1, n+1):
        for j in range(1,n+1):
            if i >= j:
                lst.append(i)
            else:
                lst.append(j)

        print(lst)

    return lst[left:right+1]


def solution2(n, left, right):
    return [max(i//n, i%n)+1 for i in range(left, right+1)]


if __name__ == "__main__":
    print(solution(4,7,14))
