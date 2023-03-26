a = int(input())
b = int(input())
h=0
for i in range (0,b):
    c, d = map(int, input().split(' '))
    h=h+c*d
if h==a:
    print('Yes')
else:
    print("No")
