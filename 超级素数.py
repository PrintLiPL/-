n=int(input(":"))
cc=0
if n<10 or n>1e+8:
    print("不符合题意")
    exit()
def su(a):
    a=int(a)
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return a
    else:
        return 0
for i in range(1,n+1):
    ipl=su(i)
    if ipl!=0:
        for x in range(len(str(ipl))-1):
            ipl/=10
            ipl=su(ipl)
    else:
        continue
    if ipl!=0:
        cc+=1
        print(i)
print(cc)