for i in range(1,10):
    for a in range(1,i+1):
       print(a,"* {0} = {1}".format(i,a*i),end="        ")
    print("")
