print('Рады приветсвовать вас в нашем заведении \n Чего желаете?')

menupos = ['Стейк', 'Отбивная', 'Бифстроганов'] #Наименованию блюд
menuprice = [120, 550, 340] #Цены
promolist = ['cafe', 'ncfu', 'rs3jf4']

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
			print('Введите промокод')

			promo = input('N - если у вас нет промокода: ')

			if promo == 'N':
				print('Заказ готов')
				flag = False
			else:
				for n in range(0, len(promolist)):
					if promo == promolist[n]:
						print('Вы получили скидку в 50%')
						print('Сумма вашего заказа составила: '+str(summ/2)+' руб.')
				print('Заказ готов')
				flag = False

		elif command == 'ex':
			print('Ваш заказ отменен')
			summ = 0
		else:
			summ = summ + menuprice[int(command)-1]
buy()

