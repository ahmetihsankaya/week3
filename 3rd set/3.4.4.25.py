full_numbers = [-2,3,5,8,-10,-15,18,28,32,-33,45,46,49]

sum_negative_number = 0

for number in full_numbers:
    if number < 0:
        sum_negative_number += number

print(sum_negative_number)