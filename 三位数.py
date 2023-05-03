n=int(input())
count=0
for a in range(1,n+1):
    for b in range(n+1):
        for c in range(n+1):
            if c!=a and c!=b and a!=b:
                sum = a * 100 + b * 10 + c
                if sum % 2 != 0:
                    count += 1
                    # print(sum)
print(count)