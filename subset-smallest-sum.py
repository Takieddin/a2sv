n, s = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
res = 0
left = 0
curr = 0
 
for right in range(len(arr)):
    num = arr[right]
    curr += num
    while curr > s:
        curr -= arr[left]
        left += 1
    res = max(res, right - left + 1)
print(res)
