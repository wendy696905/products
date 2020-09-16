
import os #operating system
products = []
# 讀取檔案
def read_file(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if 'product name, price' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
    return products

#請使用輸入
def user_input(products):
    while True:
        name = input('Please enter product name: ')
        if name == 'q':
            break
        price = input('Please enter price: ')
        products.append([name,price])
    print(products)
    return products

# 印出所有購買紀錄
def print_products(products):
    for p in products:
        print('the price of', p[0], 'is', p[1])

# 寫入檔案
def write_file(filename,products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('product name, price\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')


def main():
    filename = 'products.csv'
    if os.path.isfile(filename): #check if the file exists
        print('Yeah! Find the file!')
        products = read_file(filename)
    else:
        print('Cannot find the file!')
    products = user_input(products)
    print_products(products)
    write_file(filename, products)

main()
