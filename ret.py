#Задано чотирицифрове натуральне число. 
#Знайти добуток цифр цього числа.
#Записати число в реверсному порядку.
#Посортувати цифри, що входять в дане число
###########################################################
#num = int(input("Enter four-digit positive integer: "))
#a = num % 10
#b= num  % 100 //10 
#c = num % 1000 //100
#d = num // 1000
#print (a+b+c+d)
###########################################################1
#num = int(input("Enter four-digit positive integer: "))
#a = num % 10
#b = num  % 100 //10 
#c = num % 1000 //100
#d = num // 1000
#print (a,b,c,d)
#########################################################2
# num = int(input("Enter four-digit positive integer: "))
# a = num % 10
# b = num  % 100 //10 
# c = num % 1000 //100
# d = num // 1000
# number_list=[a,b,c,d]
# order_list=[]
# for i in range(4):
#     x=min(number_list)
#     order_list.append(x)
#     number_list.remove(x)
# print("Sorted numbers: ", order_list)