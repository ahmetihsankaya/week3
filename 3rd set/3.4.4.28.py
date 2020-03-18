list_of_names = ["de gea", "brown", "ferdinand", "vidic", "evra", "sam", "carrick", "scholes", "ronaldo", "giggs", "rooney", "tevez"]

count_of_names = 0

for names in list_of_names:
    if names == "sam":
        break
    else:
        count_of_names += 1

print(count_of_names)