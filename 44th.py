# find the missing number in the list from 1 to 7



numbers = [1, 2, 3, 5, 7]

i = 1
while i <= 7:
    if i not in numbers:
        print("Missing number:", i)
    i += 1
    

