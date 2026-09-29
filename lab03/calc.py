a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
d=input()
if d == '+':
	print("Сумма:", a+b)
elif d== '-':
	print('Разность', a-b)
elif d== '*':
	print('Умножение', a*b)
elif d== '/':
	if b==0:
		print('Деление на ноль невозможно')
	else:
		print('Деление', a/b)
