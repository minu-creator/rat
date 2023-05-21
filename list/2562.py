l = list()
for i in range(9):
     l.append(int(input()))
m=-10000000000
num=0
for i in range(len(l)):
    if l[i]>m:
        m=l[i]
        num=i+1
print(m)
print(num)
