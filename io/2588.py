# a = int(input())
# b,c,d = map(int, input())
# e= 0
# print(a*d)
# e=e+a*d
# print(a*c)
# e=e+a*c*10
# print(a*b)
# e=e+a*b*100
# print(e)

A = int(input())
B = int(input())

print(A * (B%10))
print(A * ((B // 10) % 10))
print(A * (B // 100))
