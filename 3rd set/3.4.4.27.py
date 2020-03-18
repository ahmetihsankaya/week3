#full_numbers = [1,3,5,7,10,15,18,28,32,33,45,46,49]
full_numbers = [1,3,5,7,15,33,45,49]


sum_odd_number = 0

for number in full_numbers:
    if number % 2 == 0:
        break
    else:
        sum_odd_number += number

print(sum_odd_number)