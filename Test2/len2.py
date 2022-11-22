#https://youglinux.info/python/builtin-functions
#1
while True:
	a = input('До 10 символів: ')
	if len(a) > 10:
		print('Більше 10')
	else:
		q = 10 - len(a)
		print(a + '*' * q)
