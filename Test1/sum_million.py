from datetime import datetime
import time



lst = []
for num in range(1, 1000001):
	lst.append(num) # add new nubmer
print(lst)
print(f'Сумма чисел {sum(lst)}')
print(f'Макс число {max(lst)}')

input()
