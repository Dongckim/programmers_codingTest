def factorial(x):
    fact = 1
    for i in range(x):
        fact*=(i+1)
    return fact

a, b = list(map(int, open('input.txt', 'rt').read().split(' ')))
print(factorial(a)/factorial(a-b)/factorial(b))