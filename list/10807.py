input()
l = list(map(int, input().split()))
x = int(input())

c = 0
for i in range(len(l)):
    if l[i] == x:
        c += 1
        
print(c)