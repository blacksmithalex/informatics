l = []
for i in range(65, 91):
    l.append(chr(i))

word = list(input())
k = int(input())

for i in range(len(word)):
    pos = l.index(word[i]) - k
    word[i] = l[pos]

print(''.join(word))
