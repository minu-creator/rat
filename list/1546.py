x = int(input())
a = list(map(int, input().split()))
m= max(a)

hap=0
dap=0
for i in range(x):
    a[i]=a[i]/m*100

print(sum(a)/x)
