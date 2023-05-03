n=int(input(":"))
l1=list(range(1,n+1))
count=0
while len(l1)>1:
    l2=l1[:]
    for i in range(0,len(l2)):
        count+=1
        if count%3==0:
            l1.remove(l2[i])
print(l1[0])