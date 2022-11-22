file_name = 'guest_10-3.txt'
try:
	with open(file_name) as file_object:
		lines_name = file_object.read()
		print(lines_name)
except FileNotFoundError:
	print(file_name + ' Not found!')

name = input("Введіть своє ім'я ")

with open(file_name, 'w') as file_object:
		file_object.write(name)

with open(file_name) as file_object:
	lines_name = file_object.read()

print(lines_name)