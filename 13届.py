"""
d={"lan":1,"qiao":2,"qing":3,"shao":4}
print(max(d.keys()))
print(d.pop(max(d.keys()),0))
print(d)
"""
# 1 给定一个正整数n，输出各位数字乘积*6的值
'''
n=input(":")
count=1
for i in n:
    count*=int(i)
print(count*6)
'''
# 2 被看到了
'''
n=input(":").split(",")
count0=0
count1=0
count2=0
a=0
for i in n:
    if a+2>len(n)-1:
        break
    elif n[a]==n[a+2]:
        count1+=1
    elif n[a]!=n[a+2] and n[a]=='q' :
        count0+=1
    elif n[a]!=n[a+2] and n[a]=='p':
        count2+=1
    a+=1
if n[0]==n[1] and n[0]=='p':
    count0+=1
else:
    count1+=1
if n[-1]==n[-2] and n[-1]=='q':
    count0+=1
else:
    count1+=1
print(count0,'\t',count1,'\t',count2)
'''
# 3 男生女生转圈圈
'''
x=int(input("x:"))
y=int(input("y:"))
k=int(input("k:"))
lst=[a for a in range(1,x+y+1)]
seat=0
go=0
lsg=[]
count=0
while len(lst)-go!=x:
    if seat>len(lst)-1:
        seat=1
        count+=1
        continue
    if count==k and lst[seat] not in lsg:
        go+=1
        lsg.append(lst[seat-1])
        count=0
        pass
        continue
    seat+=1
    count+=1
    print(count,'\t',seat)
inde=[]
print(lst)
print(lsg)
print(go)
for i in range(len(lst)):
    if lst[i] not in lsg:
       inde.append(lst[i])
print(inde,sep=',')
'''
# 4 可顺序列表再倒叙 or 判断相邻
'''
num=input(":")
n=input(":").split(',')
d=0
count=0
ha=[1 for i in range(len(n))]
for i in n :
    n[d]=int(i)
    d+=1
a=0
def check(n):
    global ha
    for i in range(len(n)-1):
        if n[i]<n[i+1]:
            while ha[i+1]<=ha[i]:
                ha[i+1]+=1
        elif n[i]>n[i+1]:
            while ha[i]<=ha[i+1]:
                ha[i]+=1
check(n)
a=len(n)
def changelst(lst):
    lsta=[]
    for c in range(1,len(lst)+1):
        lsta.append(lst[-c])
    return lsta
n=changelst(n)
ha=changelst(ha)
check(n)
print(n)
print(sum(ha))
'''
# 5 1,2,3,4,5,6,7,8,9,10
'''
n = list(map(int, input(":").split(",")))
n.sort()
print(max(n))
def m(n):
    nl = []
    for i in range(len(n) - 1):
        n.sort()
        if len(n) == 0:
            break
        nl.append(max(n))
        del n[-1]
        if len(n) == 0:
            break
        nl.insert(0, max(n))
        del n[-1]
    return nl


n = m(n)
cou = []
for i in range(len(n)):
    cou.append(n[i] * n[i + 1] * n[i + 2])
    if i + 2 == len(n) - 1:
        break
print(sum(cou))
'''
# 6 排小球
b=list(map(int,input(":").split(",")))
w=list(map(int,input(":").split(",")))
k=int(input(":"))
all=[]
su=0
for i in range(k):
    x=max(b)
    y=max(w)
    if len(all)>=3:
        break
    if x>y :
        all.append(x)
        a=0
        while b[a]!=x:
            del b[0]
        del b[0]
    elif y>x:
        all.append(y)
        for i in w:
            if i!=y:
                del w[0]
            else:
                while w[a] != y:
                    del w[0]
                del w[0]
    else:
        all.append(x)
        for i in b:
            if i!=y:
                del b[0]
            else:
                del b[0]
                break
        for i in w:
            if i!=x:
                del w[0]
            else:
                del w[0]
                break
    print(b)
    print(w)
for i in range(0,len(all)):
    print(all[i],end='')