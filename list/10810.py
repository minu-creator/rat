a,b = map(int, input().split())
l = [0] * a
for i in range(b):
    f,e,num = map(int, input().split())
    for j in range(f,e+1):
        l[j-1] = num
    
print(*l)