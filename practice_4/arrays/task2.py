n = 7
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        val = max(0, i + j - (n - 2))
        row.append(val)
    matrix.append(row)

for row in matrix:
    print(" ".join(str(x) for x in row))
