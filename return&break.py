def a():
    for i in range(10):
        if i==1:
            print(i)
            break
    print("!")
a()
def b():
    for i in range(10):
        if i==1:
            print(i)
            return
    print("!!")
b()