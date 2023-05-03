lst=input(":").split(",")
n=0
for i in lst:
    lst[n]=int(i)
    n+=1
lst.sort()
#print(lst)
for a in lst:
    '''
    if a+1!=lst[lst.index(a)+1]:
        print(a+1)
        break
    '''
    if a+1 not in lst:
        print(a+1)
        break