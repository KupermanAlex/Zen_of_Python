#	Спробуйте переписати наступний код через map. Він приймає список реальних імен і замінює їх прізвищами, використовуючи  більш надійний метод.

# names = ['Sam', 'Don', 'Daniel'] 
# for i in range(len(names)): 
#     names[i] = hash(names[i]) 
# print(names)

# names = ['Sam', 'Don', 'Daniel']

# secret_name = map (lambda x:hash(x), names)
# print (list(secret_name))

#//////////////////////////

# Всі ці числа в списку мають стрічковий тип даних, наприклад  [‘1’,’2’,’3’,’4’,’5’,’7’], перетворити цей список  в список, всі числа якого мають тип даних integer:
# 1)	використовуючи метод  append
# 2)	використовуючи метод  map

# list_old = ['2','3','4','5']

# list_new =list( map(lambda x: int (x) ,list_old))
# print (list_new)

# list_old = ['2','3','4','5']
# list_new =[]
# for i in list_old:
#     i = int(i)
#     list_new.append(i)
# print(list_new)
#///////////////////////////////
# . Перетворити список, який містить милі ,  в список, який містить кілометри (1 миля=1.6 кілометра)
#  	a) використовуючи функцію map
# 	b) використовуючи функцію map та lambda

# list_mile = [12,10,1]

# list_km = list(map(lambda x:x*1.6 ,list_mile))
# print (list_km)

# def f(x):
#     return 1.6 * x
# list_km = list(map(f,list_mile))
# print (list_km)

############################################################################

#  Знайти найбільший елемент в списку  використовуючи функцію reduce
# from functools import reduce

# nums =[2,3,4,5,6,8,7,7,123]
# max_num = reduce(lambda x,y:x if (x>y) else y , nums)
# print (max_num)
##############################################################################
# Перепишіть наступний код, використовуючи map, reduce і filter. Filter приймає функцію і колекцію. Повертає колекцію тих елементів, для яких функція повертає True.
# people = [{'name': 'Sam', 'height': 160}, {'name': 'Alex', 'height': 80}, {'name': 'Jack'}] 
# height_total = 0 
# height_count = 0 
# for person in people: 
#     if 'height' in person: 
#         height_total += person['height'] 
#         height_count += 1 
# print(height_total)
# => 240

from functools import reduce

people = [{'name': 'Sam', 'height': 160}, {'name': 'Alex', 'height': 80}, {'name': 'Jack'}] 

rost = list(map(filter(lambda x:x=='height',people)))
print(rost)