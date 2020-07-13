# 讀取檔案
products = []
with open('products.csv', 'r', encoding= 'utf-8') as f:
    for line in f:
        if 'product name, price' in line:
            continue
        name, price = line.strip().split(',')
        products.append([name, price])
print(products)

#請使用輸入
while True:
    name = input('Please enter product name: ')
    if name == 'q':
        break
    price = input('Please enter price: ')
    products.append([name,price])
print(products)

# 印出所有購買紀錄
for p in products:
    print('the price of', p[0], 'is', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('product name, price\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')