a, b, c = map(int, input().split(' '))
if a==b==c:
    print (10000+a*1000)
elif a==b!=c:
    print (1000+b*100)
elif a==c!=b:
    print (1000+a*100)
elif c==b!=a:
    print (1000+c*100)
elif a!=b!=c:
    if(a <c and b <c):
        print(c*100)
    elif(a <b and c <b):
        print(b*100)
    elif(c <a and b <a):
        print(a*100)



