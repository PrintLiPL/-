import turtle as t
def nbx(num):
    for i in range(num):
        t.forward(1000/num)
        t.left(180 - (num*180-360)/num)
if __name__ == '__main__':
    nbx(6)