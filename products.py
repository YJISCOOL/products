shop_cart = [] #儲存商品名稱
while True:
	name = input('input product: ')
	if name == 'q':
		break
	price = input('inpit price: ') 
	#有輸入商品時再輸入價格
	pro_pri =[]
	pro_pri.append(name)
	pro_pri.append(price)
	shop_cart.append(pro_pri)
print (shop_cart)

print (shop_cart[0][0])
print (shop_cart[0][1])