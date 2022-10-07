a,b = map(int,input().split())
x = max(a,b)
i = 1
while i > 0:
    m = x * i
    if m % a == 0 and m % b == 0:
        print(m)
        break
    i += 1