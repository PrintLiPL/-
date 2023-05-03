m=int(input("m:"))
n=int(input("n:"))
j=0
if n>m:
   j=m
   m,n=n,j
a=n
lst=[]
for i in range(m-n+1):
    if a % 7 == 0 and a % 5 != 0 :
        lst.append(a)
    a+=1
for i in range(len(lst)):
    if i==len(lst)-1:
        print(lst[i],end='')
        break
    print(lst[i],end=',')
s=''
for i in range(n,m+1):
    if i%7==0 and i%5!=0:
        s+='{},'.format(i)
print()
print(s[:-1])#1
s=[]
for i in range(n,m+1):
    if i%7==0 and i%5!=0:
        s.append(str(i))
print(",".join(s))#2
print(*s,sep=',')#3
#join
sting='python'
print('| |'.join(sting))
