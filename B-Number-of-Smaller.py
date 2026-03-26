n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
p1,p2=0,0
res=[]
for num in b:
    if(p1==n):
        res.append(n)
    else:
        while(p1<n and a[p1]<num):
            p1+=1
        res.append(p1)
print(*res)
