
def k(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum
ma=int(input("M:"))
na=int(input("N:"))
for f in range(ma,na+1):
    if f==k(f):
        print(f)
'''lst=[]
for i in range(m,n+1):
    lst.append(i)
def yinzi(aaa):
    ad=[]
    for x in range(1,aaa+1):
        if aaa%x==0 and aaa!=x:
            ad.append(x)
    if sum(ad)==aaa:
        return aaa
data1=filter(yinzi,lst)
for i in list(data1):
    print(i)
'''