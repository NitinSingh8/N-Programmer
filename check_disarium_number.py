value = int(input("Enter the number : "))

disarium = 0

temp = value

# function to find the length of last digit
def find_position(data):
    str_data = str(data)
    return len(str_data)


# Using loop to do calculation and to find final answer after the calculation
while temp!=0:
    disarium += (temp%10) ** find_position(temp)
    temp = temp//10


# At last checking the calculated value and original number
if disarium == value:
    print(f"{value} is a disarium number ")
else:
    print(f"{value} is not a disarium number")