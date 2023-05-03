f=lambda a,b,c,d:(a**b)*(c**d)
print(f(1,2,3,4))
e=lambda *c : sum(c)
a=[1,2,3,4,5,6,7,8,9,10]
b=[1,2,3,4,5,6,7,8,9,10]
print(e(1,2,3,4,5,6,7,8,9,10))
mp=list(map(lambda *c : sum(c),a))
print(mp)
print(list(map(lambda x,y:(x+y)*(x+2*y),a,b)))