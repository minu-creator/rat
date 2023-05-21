p = [0] * 42
a=0
for i in range(10):
    num = int(input())
    p[num%42] = 1
for i in range(42):
    if p[i]==1:
        a=a+1
print(a)
