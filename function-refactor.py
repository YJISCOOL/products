#refactor重構：將程式重新
import os #operating system

#讀取檔案（本來這一個函式中不只做一件事，因此需要重構）
def read_file(filename): 
    items = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            items.append([name, price])
    return items

#讓使用者輸入
def user_input(items):
    while True:
        name = input('input product: ')
        if name == 'q':
            break
        price = int(input('inpit price: '))
        items.append([name, price]) 
    return items

#印出所有購買紀錄
def print_items(items):
    for i in items:
        print (i[0], '價格是', str(i[1]))

#寫入檔案
def write_file(filename, items):
    with open(filename, 'w', encoding = 'utf-8') as f: 
        f.write('商品,價格\n')
        for i in items:
            f.write(i[0] + ',' + str(i[1]) + '\n')

def main(): #只有這一段是真的在執行程式因此定義為main()函式，前面def都是在定義而已
    items = []
    filename = 'products.csv'
    if os.path.isfile(filename):
        print ('找到檔案了！')
        items = read_file(filename)
    else:
        print ('沒有檔案耶⋯')

    items = user_input(items)
    print_items(items)
    write_file('products.csv', items)


main()