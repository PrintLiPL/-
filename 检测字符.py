line=input(":")
st = 0
intt = 0
space = 0
mark = 0
def inspecter(x):
    st = 0
    intt = 0
    space = 0
    mark = 0
    if x.isalpha():#判断字符
        st+=1
    elif x.isspace():#判断空格
        space+=1
    elif x.isdigit():#判断数字
        intt+=1
    else:
        mark+=1
    return st,intt,space,mark
for i in range(0,len(line)):
    st+=inspecter(line[i])[0]
    intt+=inspecter(line[i])[1]
    space+=inspecter(line[i])[2]
    mark+=inspecter(line[i])[3]
print(st,'\n',intt,'\n',space,'\n',mark,'\n')
#isalnum全部由数字或字母构成
#islower全部由小写字母
#isupper全部由大写字母
#istittle首字母是否大写