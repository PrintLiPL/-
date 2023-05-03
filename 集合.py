a={1,32,4,65,'aa',1,1,1,1,32,32,65}
print(set("hello"))
print(a)
a.add(9)#添加元素，不报错
print(a,"add")
a.discard(9)#删除元素，不报错
print(a,"discard")
a.remove('aa')#删除元素，会报错
print(a,"remove")
#pop随机删除最后一个
string={'a','b','c','d','e','f','g','h'}
for i in a:
    print(i,end=" ")#无序性
print(string)
print(sorted(string))
print(sorted(string,reverse=True))
s3={1,2,3}
s4={3,4,5}
print("s3",s3)
print("s4",s4)
s5=s3|s4#并集，两者都包含
print("|",s5)
s6=s3-s4#差集，去除共有部分，输出前者
print("-",s6)
s7=s3&s4#交集，两个集合共有部分
print("&",s7)
s8=s3^s4#对称拆分，去除两者公共的，输出余下部分
print("^",s8)