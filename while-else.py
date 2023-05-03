i=0
while i*i<1000:
    i+=1
    print(str(i)+'*'+str(i)+'=',i*i)
    if i == 3:
        break
else:
    print("while over")
for i in range(10):
    if i==3:
        break
    print(i,end="")
else:
    print("For Over!")
print(1,"\\")
print(r"hello\n world")#原始字符串
text='AB CD EF GH IJ'
text.replace(' ','|',3)
print(text.replace(' ','|',3))
print(text.split(' '))