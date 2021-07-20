number = input("Enter the number : ")

# converting string variable(number) into list of integer data type
list_num = list(map(int,number))

sum = 0

# find the sum of all digit in list_num
for i in list_num:
    sum += i

# printing the sum
print(sum)
