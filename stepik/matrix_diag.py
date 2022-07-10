s = input().split()
n, m = int(s[0]), int(s[1])
k, l = 1, [[0] * m for _ in range(n)]

for i in range(0, n + m - 1):
    #print('l_range=', max(0, i - min(n, m) + 1), 'h_range=',  min(i + 1, max(n, m)))
    if n > m:
        l_range = max(0, i - min(n, m) + 1)
        h_range = min(i + 1, max(n, m))
    if n < m:
        l_range = max(0, i - max(n, m) + 1)
        h_range = min(i + 1, min(n, m))
    if n == m:
        l_range = max(0, i - max(n, m) + 1)
        h_range = min(i + 1, min(n, m))
    for j in range(l_range, h_range):
        #print('i=', i, 'j=', j)
        l[j][i-j] = k
        k += 1
for i in range(n):
    for j in range(m):
        print(str(l[i][j]).ljust(3), end = '')
    print()