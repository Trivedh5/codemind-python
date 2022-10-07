tc = int(input())
for i in range(tc):
    n = int(input())
    p = 1
    while n > 0:
        p *= n
        n -= 1
    print(p)