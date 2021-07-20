value = int(input("Enter the range of number :"))

flag = 0

for i in range(2,value):
    for j in range(2,i):
        if i%j == 0:
            flag = 1
            break

    if flag == 0:
        print(i,"prime number")
    flag = 0