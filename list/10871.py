x = list(map(int, input().split()))
l = list(map(int, input().split()))
for i in range(len(l)):
    if x[1]>l[i]:
        print(l[i] ,end=" ")