N = int(input())
if N >= 1:
    pascal = [[1]]
    for i in range(N - 1):
        row = pascal[-1]
        newrow = [1]
        for j in range(len(row) - 1):
            newrow.append(row[j] + row[j + 1])
        newrow.append(1)
        pascal.append(newrow)

    for x in pascal:
        print(*x)