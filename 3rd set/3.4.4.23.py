full_numbers = [2,3,5,8,10,15,18,28,32,33,45,46,49]

odd_number = 0

for number in full_numbers:
    if number % 2 !=0:
        odd_number = odd_number + 1

print(odd_number)