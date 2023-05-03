n = int(input(":"))
count = 0
for i in range(100, n + 1):
    a = i // 100
    b = i // 10 - a * 10
    c = i - a * 100 - b * 10
    if a ** 3 + b ** 3 + c ** 3 == i:
        count += 1
        print(i)
print(count)
