numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for n in numbers:
    print(n)

for n in numbers:
    print(n,n**2)

total=0
for n in numbers:
    total=n+total
    print(total)

product=1
for n in numbers:
    product=n*product
print(product)
