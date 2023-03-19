h, m = map(int, input().split(' '))
if 0 > m-45:
    m = 60+m-45
    h = h-1
elif m-45 == 0:
    m = 0
elif 0 < m-45:
    m = m-45
if 0 > h:
    h = 24+h
print(h, m)
