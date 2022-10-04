a,b = map(int,input().split())
if (a-b) == 1 or (a-b) == -1:
    print("Yes")
elif (a-b) == 9 or (a-b) == -9:
    print("Yes")
else:
    print("No")