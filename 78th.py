# praticing binary to decimal


binary = input("Enter the number : ")


number = 0
number_valid = True
for digit in binary:
    if digit not in ('1','0'):
        number_valid = False
        break



if number_valid:
    number = int(binary,2)
    print(f"the decimal number is {number}")  
else:
    print("the number is invalid")
    