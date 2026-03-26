n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
p1, p2 = 0, 0
while p1 < n and p2 < m:
    if a[p1] < b[p2]:
        print(a[p1], end=' ')
        p1 += 1
    elif a[p1] > b[p2]:
        print(b[p2],end=' ')
        p2 += 1
    else:
        print(a[p1], end=' ')
        print(b[p2], end=' ')
        p1 += 1
        p2 += 1
for i in range(p1,n):
    print(a[i],end=' ')
for i in range(p2,m):
    print(b[i],end=' ')
