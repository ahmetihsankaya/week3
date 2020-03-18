list_of_names = ["ahmet", "mehmet", "ali", "mustafa", "furkan", "ülkü", "eyüp", "can", "said", "bahadır", "meliha", "gürcan"]

count_of_names = 0

for names in list_of_names:
    if len(names) >= 5:
        count_of_names += 1

print(count_of_names)