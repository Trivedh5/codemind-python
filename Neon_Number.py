n = int(input())
a = n * n
s = 0
while a > 0:
    r = a % 10
    s += r
    a = a//10
if n == s:
    print("Neon Number")
else:
    print("Not Neon Number")