n = int(input())
a = list(map(int,input().split()))
 
has_odd = False
has_even = False
 
for num in a:
    if num % 2:
        has_odd = True
    else:
        has_even = True
if has_even and has_odd:
    a.sort()
print(*a)