l = int(input())
n = int(input())
for i in range(n):
    w,h = map(int,input().split())
    if l == w and l == h:
        print("ACCEPTED")
    elif w > l and h > l and w != h:
        print("CROP IT")
    elif w > l and h == l:
        print("CROP IT")
    elif h > l and w == l:
        print("CROP IT")
    elif w > l and h > l and w == h:
        print("ACCEPTED")
    else:
        print("UPLOAD ANOTHER")