# Program to check whether the number is harshad number or not.

number = input("Enter the number : ")

list_num = list(map(int,number))

sum = sum(list_num)

if int(number)%sum == 0:
    print(f"{number} is a harshad number")
else:
    print(f"{number} is not a harshad number")