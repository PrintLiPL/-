data1=[66,15,12,13,47,56,9,99,66,126541]
f2=filter(lambda x:x>50,data1)
data2=list(f2)
print(data2)

f3=map(lambda x:x+2,data1)
data3=list(f3)
print(data3)
print(data1)
