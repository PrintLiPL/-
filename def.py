def area(width,height):
    are=width*height
    return are
print("长方形面积={0}*{1}={2:.2f}".format(320,480,area(320,480)))
def sum(*numbers):
    total=0.00000
    for numbers in numbers:
        total+=numbers
    return total
print(sum(1,2,3,4,5,6,7,8,9,10))
def info(**info):
    print("++信息展示--")
    for k,v in info.items():
        print("{0}-{1}".format(k,v))
info(name="Tony",age=19)