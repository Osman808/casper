
print('Рады приветсвовать вас в нашем заведении \n Чего желаете?')

menupos = ['Стейк', 'Отбивная', 'Бифстроганов'] #Наименованию блюд
menuprice = [120, 550, 340] #Цены

for x in range(0,len(menupos)):
	print(str(x+1)+') '+menupos[x]+' Цена - '+str(menuprice[x])+'руб.')

def buy():
	print('Введите номер блюда, чтобы добавить его в заказ')
	print('Введите end сделать заказ')
	print('Введите ex чтобы отменить заказ')

	flag = True
	summ = 0

	while flag:
		command = input('... ')

		if command == 'end':
			print('Сумма вашего заказа составила: '+str(summ)+' руб.')
			print('Заказ готов')
			flag = False
		elif command == 'ex':
			print('Ваш заказ отменен')
			summ = 0
			flag = False
		else:
			summ = summ + menuprice[int(command)-1]
buy()



