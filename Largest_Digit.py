n = int(input())
l = 0
for i in str(n):
    r = int(i) %10
    if r > l:
        l = r
print(l)