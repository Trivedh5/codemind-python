a = int(input())
b = int(input())
for i in range(a,b+1):
    count = 0
    n = i
    while n > 0:
        r = n % 10
        if r > 0:
            if i % r == 0:
                count += 1
        n = n//10
    if len(str(i)) == count:
        print(i,end =" ")