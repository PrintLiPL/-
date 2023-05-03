# 1
"""
s='Hi LanCiao'
print(s[-7:0])
"""
# 2
'''
pi=31143.1415926
print(round(pi),round(pi,-2))#round()四舍五入 -前面取整 +小数取整
'''
# 3 a:97 A:65`
'''
p=ord('b')
print(p,chr((p+3)%26+p))
'''
# 4
'''
n=input(':').split(',')
print(max(n))
'''
# 5质因数
'''
n = int(input(':'))
count = 0
while n > 2:
    for i in range(2, n + 1):
        if n % i == 0:
            count += 1
            n = n // i
            break
print(count)
'''
# 6
'''
length=[]
count=0
num='1234567890'
n=input(':')
for i in range(len(n)):
    if n[i] in num:
        count+=1
    if n[i] not in num or i+1>len(n)-1:
        length.append(count)
        count=0
print(max(length))
'''
# 7 中文可以当变量名
'''
n=int(input(":"))
def 质数(num):
    a=0
    for i in range(1,num):
        if num%i==0:
            a+=1
    if a==1 :
        return 1
    else:
        return 0
lst=[]
all=[]
for 变量 in range(1,n):
    if 质数(变量)==1:
        lst.append(变量)
for a in lst:
    for b in lst:
        if a+b==n:
           all.append(abs(a-b))
print(min(all))
'''
# 8
'''
lst=input(":").split(',')
a=0
b=0
for i in lst:
    lst[b]=int(i)
    b+=1
lst.sort()
while True:
    for i in range(len(lst)-2):
        lst[i]+=1
        a+=1
    lst.sort()
    if max(lst)==min(lst):
        print(a)
        break
'''
# 9 翻牌
'''
n=int(input(":"))
lst=[]
all=[]
for i in range(n):
    ca=input(":").split(",")
    lst.append(ca)
def place(lst):#定位每一个A的位置
    x=[]
    y=[]
    cb=0
    ca=0
    for a in lst :
        for b in a:
            if b=="A":
                x.append(cb)
                y.append(ca)
            cb+=1
        cb=0
        ca+=1
    print(x)
    print(y)
    d=dict(zip(x,y))
    return d
print(place(lst))
def countA(lst):
    su=0
    global n
    for a in range(n-1):
        for b in range(n-1):
                if lst[a][b+1]=='A':
                    su+=1
                if lst[a+1][b]=='A':
                    su+=1
    return su
for a in range(n):
    for b in range(n):
        if lst[a][b]=="B":
            lst[a][b]='A'
            all.append(countA(lst))
            for i in range(n):
                print(lst[i])
            print(countA(lst))
            print("-------------------------")
            lst[a][b]="B"
print(max(all))
'''
# 奇怪的平面直角花盆系 对角线：xy坐标的 和 或 差值相等 2,1 3,2 5,2 4,3 3,4 6,5 or 1,1 2,1 3,1 5,1 6,1 9,1 1,2 1,3 6,6
'''
n = input(":").split(' ')
x = []
y = []
a = 0
count1 = 0  # x
count2 = 0  # y
count3 = 0  # 右对
count4 = 0  # 左对

all = []
for i in n:
    b = n[a]
    x.append(b[0])
    y.append(b[2])
    a += 1
x = list(map(int, x))
y = list(map(int, y))
for a in range(0, len(x)):
    print(x[a])
    print(y[a])
    for i in range(0, len(x)):
        if x[a] + y[a] == x[i] + y[i] and x[a] != x[i]:  # 左对
            count4 += 1
        elif x[a] - y[a] == x[i] - y[i] and x[a] != x[i]:  # 右对
            count3 += 1
        elif x[a] == x[i] and y[a] != y[i]:  # y
            count2 += 1
        elif x[a] != x[i] and y[a] == y[i]:  # x
            count1 += 1
    all.append(max(count1+1, count2+1, count3+1, count4+1))
    print(all)
    count1=0
    count2=0
    count3=0
    count4=0
print(max(all))
'''

