a, b = map(int, input().split(' '))
c = int(input())
if b+c>=60:
    a=a+((b+c)//60)
    if a>=24:
        a=a-24
    b=(b+c)%60
else:
    b=b+c
print(a,b)

