num = int(open('input.txt', 'rt').read().split('\n')[0])
people = list(map(lambda x : tuple(x.split()), open('input.txt', 'rt').read().split('\n')[1:]))
member = []
for i, (age, name) in enumerate(people):
    member.append((i, int(age), name))
ag = sorted(member, key= lambda x : (x[1], x[0]))
[print(age, name) for (i, age, name) in ag]