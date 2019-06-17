#Вивести весь текст у верхньому регістрі (всі великі літери)
#Знайти в заданій стрічці кількість входжень слів (better, never, is)
#Замінити всі входження символу “і” на “&”

zen = """ text """
zen=zen.upper()
print(zen)
#######################
print (zen.upper())
################################# 
number_better=zen.count('better')
number_is=zen.count('is')
number_never=zen.count('never')
print (number_better + number_is + number_never)
##############################################
zen=zen.replace('i' , '&')
print(zen)
####################################
print(zen.replace('i' , '&'))
