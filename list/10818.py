x = int(input())
l = list(map(int, input().split()))
max=-1000000000000000
min=10000000000000
for i in range(len(l)):
    if l[i]<min:
        min=l[i]
    if l[i]>max:
        max=l[i]
print(min,max ,end=" ")