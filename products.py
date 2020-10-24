shop_cart = [] #儲存商品名稱
while True:
	name = input('input product: ')
	if name == 'q':
		break
	price = int(input('inpit price: ')) #所以現在price都是整數的形式
	#有輸入商品時再輸入價格

	shop_cart.append([name, price])
	#pro_pri =[name, price]
	#pro_pri.append(name)
	#pro_pri.append(price)
	#shop_cart.append(pro_pri)
print (shop_cart)

for product in shop_cart:
	print (product[0], '價格是', str(product[1]))

with open('products.csv', 'w', encoding = 'utf-8') as f1: 
#只是打開檔案
	f1.writ('商品,價格\n')
	for product in shop_cart:
		f1.write(product[0] + ',' + str(product[1]) + '\n') #記得轉換整數與字串的形式
		#才真正有寫入檔案