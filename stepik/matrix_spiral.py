s = input().split()
m, n = int(s[0]), int(s[1])

top = left = 0
bottom = m - 1
right = n - 1
k = 1

mat = [[0 for x in range(n)] for y in range(m)]

while True:
    if left > right:
        break

    for i in range(left, right + 1):
        mat[top][i] = k
        k += 1
    top = top + 1

    if top > bottom:
        break

    for i in range(top, bottom + 1):
        mat[i][right] = k
        k += 1
    right = right - 1

    if left > right:
        break

    for i in range(right, left - 1, -1):
        mat[bottom][i] = k
        k += 1
    bottom = bottom - 1

    if top > bottom:
        break

    for i in range(bottom, top - 1, -1):
        mat[i][left] = k
        k += 1
    left = left + 1

for i in range(m):
    for j in range(n):
        print(str(mat[i][j]).ljust(3), end = '')
    print()