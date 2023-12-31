A, B, V = list(map(int, open("input.txt", "rt").read().split(' ')))

rm = V-B // (A-B)
if rm == int(rm):
    print(rm)
else:
    print(rm+1)
