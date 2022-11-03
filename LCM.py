a,b = map(int,input().split())
p = a*b
while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a
if a == 0:
    gcd = b
else:
    gcd = a
print(p//gcd)