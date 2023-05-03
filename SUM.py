
#1
"""a=[]
for i in range(1,n+1):
    a.append(i)
print(sum(a))
"""
#2
"""print((n+1)*n/2)"""
#3
def he(x):
    if x>=1:
        return x+he(x-1)
    else:
        return 0
n=int(input(":"))
print(he(n))