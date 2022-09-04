i,r,k = map(int,input().split())
count = 0
while i <= r:
    if i % k == 0:
        count += 1
    i += 1
print(count)
