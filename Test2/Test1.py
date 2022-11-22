from random import random

my_list1 = [1, 2, 3]  # 1
my_list2 = ["a", "b", "c"]  # ТИПИ СПИСКІВ    СПИСОК []; КОРТЕЖ () СЛОВНИК {}
my_list3 = ["A", 11, "Python", 5]
list4 = [my_list1, my_list2, my_list3]
print(list4)

o1 = ["початок 1", "b", "c"]  # 2
o2 = ["початок 2", "e", "g"]  # ОБ'ЄДНАННЯ
li1 = o1 + o2
li1 = li1[0:5]  # перші 5 елементів
print(li1)

alpha_list = [34, 23, 67, 100, 88, 2]  # 3
alpha_list.sort()  # СОРТУВАННЯ
print(alpha_list)  # [2, 23, 34, 67, 88, 100]

my_dict = {}
another_dict = dict()

my_other_dict = {"one": 1, "two": 2, "three": 3}
print(my_other_dict)  # {'three': 3, 'two': 2, 'one': 1}

dict = {"one": 1, "two": 2, "three": 3}
print(dict["one"])  # 1
my_dict = {"name": "Mike", "address": "49 Happy Way"}
print(my_dict["address"])  # 'Mike'

text = 'Never forget what you are, for surely the world will not'
name = f'First: {text[0]}\nLast: {text[len(text) - 1]}'
print(name)

rand = round(random() * 10, 0)
print(rand)

def print_reversed_word_by_symbol(word):
    i = len(word) - 1
    while i >= 0:
        print(word[i])
        i -= 1


print_reversed_word_by_symbol('ON')

def count_chars(string, char):
    string = string.lower()
    char = char.lower()
    index = 0
    count = 0
    while index < len(string):
        if string[index] == char:
            # Считаем только подходящие символы
            count = count + 1
        # Счётчик увеличивается в любом случае
        index = index + 1
    return count

print(count_chars('Влада', 'В'))
# fastest way

input()
