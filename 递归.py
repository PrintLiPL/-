'''
def a(n):
    if n<=1 :
        return 1
    b=a(n-1)
    print(b)
print(a(3))#调用自己，传递&回归
'''
#1
'''
def n(lst):
    return lst[0] if len(lst)<=1 else lst[0]+n(lst[1:])
print(n([1,2,3,4,5]))
'''
#2
'''
def change(n,base):
    str_lst='0123456789ABCDEF'
    print(n,'\t',n//base)
    return str_lst[n] if n<base else change(n//base,base) + str_lst[n%base]
print(change(9,8))
'''
#3
'''
import turtle as t
import random
t.speed(5)

def draw(line):
    if line>0:
        t.forward(line)
        t.right(90)
        draw(line-5)
draw(100)
t.done
'''
#4
def rabit(a,b,c):

    a,b=b,a+b
    if c==0:
        return b
    return rabit(a,b,c-1)
c=int(input("c:"))
print(rabit(1,1,c-3))#c-3为项数
def rabit2(n):
    if n==1 or n==2:
        return 1
    else:
        return rabit2(n-1)+rabit2(n-2)
print(rabit2(c))