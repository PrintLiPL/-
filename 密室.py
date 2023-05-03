n=input(":").split(',')
x=int(n[0])
y=int(n[1])
m=int(n[2])
s=1
count=0
'''for i in range(1,m+1):
   if s+1!=x and s+2!=x and s+1!=y and s+2!=y:
       count+=2
       s+=1
   if s+1==x or s+1==y :
        s+=2
   if s+1==m:
       count+=1
       print(count)
       break
   if s==m:
       print(count)
       break
'''
#正解
def M(x,y,n):
    if n<=-0:
        return 0
    elif n==1:
        return 1
    elif n==x:#多种情况的判断
        return 0
    else:
        return M(x,y,n-1)+M(x,y,n-2)#递归
print(M(x,y,m))



