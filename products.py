products = []
while True:
    name = input('Please enter product name: ')
    if name == 'q':
        break
    price = input('Please enter price: ')
    products.append([name,price])
print(products)

for p in products:
    print('the price of', p[0], 'is', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('product name, price\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')