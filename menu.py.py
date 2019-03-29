menu ={'sharwarma':1200,'semovita and egusi':1600,'afang soup':1400,'coke':300,}
order_made =[]
cost_of_each =[]
delivery_fee =900
name =str(input("\nwhat is your name"))
location =input("\nwhat is your location")
phone_number =int(input("\nwhat is your phone number"))
numbering = 0
print('\n\nHello ' + name + 'Welcome to Fruittie Kitchen' + '\nhere is our menu')
for food, price in menu.items():
	while range(len(menu)):
		numbering+=1

		print('\n' + str(numbering) +'. ' + food + ' at ' + str(price) + ' naira\n')
		break

print('input a number and click enter to select an item.')	
print('\ninput done to finish your order and see your total bill.')
print('\ninput exit to log out of the system')
while True:
	order = input('\nplease type, 1, 2, 3, 4, done or exit following;\
		the instruction above...').lower()
	if order == '1':
		order_made.append('sharwarma at 1200 naira')
		cost_of_each.append(1200)
		print('you selected sharwama at 1200 naira')
	elif order == '2':
		order_made.append('semovita and egusi at 1600 naira')
		cost_of_each.append(1600)
		print('you selected semovita and egusi at 1600 naira')
	elif order == '3':
		order_made.append('afang soup')
		cost_of_each.append(1400)
		print('you selected afang soup at 1400 naira')
	elif order == '4':
		order_made.append('coke at 300 naira')
		cost_of_each.append(300)
		print('you selected coke at 300 naira')

	elif order =='exit':
		break

	elif order == 'done':
		total_cost = delivery_fee + sum(cost_of_each)
		print('\nbelow is the list of your order and the total cost.\n\n')
		for i in order_made:
			print(i)
			pass
		print('\nthe total cost of selected item is '+ str(total_cost))
		print('we will deliver your food in the next 30 minutes. Type exit to log out')
	else:
		print('Goodbye.it looks like you didnt follow instruction. try some other time')
		break













