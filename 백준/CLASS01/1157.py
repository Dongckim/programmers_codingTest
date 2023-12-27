word = open("input.txt", "rt")

char_ls = {}
for char in word.read().upper():
    if char not in char_ls:
        char_ls[char] = 1
    else:
        char_ls[char] += 1

if len(char_ls) == 1:
    print(list(char_ls.keys())[0])

elif  max(char_ls.values()) == sorted(char_ls.values())[::-1][1]:
    print("?")
 
else:
    max_val = max(char_ls.values())
    print([k for k, v in char_ls.items() if v == max_val][0])