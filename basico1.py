
num = 0
for num in range(0, 151, 1):
    print(num)

num = 0
for num in range(0, 1005, 1):
    if num %5 !=0:
        continue
    print(num)
    

for num in range(1, 101, 1):
    if num %5 !=0:
        print(num)
    elif num %10 ==0:
        print("CodingDojo")
    else:
        print("Coding")


total = 0
for i in range(1, 500000, 1):
    if i % 2 ==1:
        total += i
print(total)     


for num in range(2018, -1, -4):
    print(num)


lownum = 10
highnum=25
mult = 3

for num in range(lownum, highnum, 1):
    if num % mult !=0:
        continue
    else:
        print(num)