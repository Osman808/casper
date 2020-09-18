import conf 

menupos = ['Стейк', 'Отбивная', 'Бифстроганов'] #Наименованию блюд
menuprice = [120, 550, 340] #Цены
promolist = ['cafe', 'ncfu', 'rs3jf4']

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
				
			print('Оцените качество обслуживания по 5-ти бальной шкале')
			ocenka = input('5 - отлично, 0 - ужасно')
			file = open('оценки.txt', 'a+')
			file.write(ocenka+'\n')
			flag = False

		elif command == 'ex':
			print('Ваш заказ отменен')
			summ = 0
		else:
			summ = summ + menuprice[int(command)-1]


def autorize():
	print('Вы зарегестривроаны в нашей системе?')
	status = input('y/n: ')
	if status == 'y':
		login = input('Введите логин: ')
		for y in range(0,len(conf.loginlist)):
			if login == conf.loginlist[y]:
				login = True
				break
		pasword = input('Введите пароль')
		for q in range(0,len(conf.passwordlist)):
			if pasword == conf.passwordlist[y]:
				pasword = True
				break
		if login & pasword:
			print('Рады приветсвовать вас в нашем заведении \n Чего желаете?')
			for x in range(0,len(menupos)):
				print(str(x+1)+') '+menupos[x]+' Цена - '+str(menuprice[x])+'руб.')

			buy()
	if status == 'n':
		print('Посетите наш ресторан в живую, совершите заказ на минимальную сумму 500 руб. и получите доступ к нашей системе\n Кушайте много \n Кушайте вкусно')



autorize()
