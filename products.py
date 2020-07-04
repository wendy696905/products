products = []
while True:
    name = input('Please enter product name: ')
    if name == 'q':
        break
    price = input('Please enter price: ')
    products.append([name,price])
print(products)