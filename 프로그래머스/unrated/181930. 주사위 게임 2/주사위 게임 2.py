import math

def solution(a, b, c):
    if a != b and b != c and a!=c:
        return a+b+c
    else:
        if a == b and b == c and a==c:
            return (a+b+c)*(math.pow(a,2)+math.pow(b,2)+math.pow(c,2))*(math.pow(a,3)+math.pow(b,3)+math.pow(c,3))
        else:
            return (a+b+c)*(math.pow(a,2)+math.pow(b,2)+math.pow(c,2))