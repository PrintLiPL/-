import math

d = 0
n = input(":").split(",")
print(n)
for i in n:
    n[d] = int(i)
    d += 1
c = sorted(n, reverse=True)
# print(*c,sep=",")
# s=[str(i) for i in c]
'''s=map(str,c)
print(",".join(s))'''
# 列表推导式
lst = [e * e for e in range(10) if e % 2 != 0]
print(lst)
lst1 = [(x, y) for x in range(10) for y in range(4)]
print(lst1)
r = list(map(math.sqrt, c))
print(c)
print(r)
