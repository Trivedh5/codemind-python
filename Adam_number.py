n = int(input())
a = n * n
rev = 0
rev1 = 0
while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n//10
b = rev * rev
while b > 0:
    c = b % 10
    rev1 = rev1 * 10 + c
    b = b//10
if a == rev1:
    print("True")
else:
    print("False")