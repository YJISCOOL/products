import os #operating system

shop_cart = [] #儲存商品名稱
if os.path.isfile('products.csv'):
#輸入檔名＝檢查檔案有沒有在相對路徑
	print ('yeah！找到檔案了！')

	#讀取檔案
	with open('products.csv' ,'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
				#跳過之後的指令，直接下一輪的for loop，沒有跳出迴圈，只是跳下一回
			name, price = line.strip().split(',')
			#strip()是要去除最後面的\n
			#split(',')是要去除逗號
			shop_cart.append([name, price])
	print (shop_cart)

else:
	print ('沒有檔案耶⋯⋯')

#讓使用者輸入
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

#印出所有購買紀錄
for product in shop_cart:
	print (product[0], '價格是', str(product[1]))

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f1: 
#只是打開檔案
	f1.write('商品,價格\n')
	#在第一列加上標題
	for product in shop_cart:
		f1.write(product[0] + ',' + str(product[1]) + '\n') #記得轉換整數與字串的形式
		#才真正有寫入檔案