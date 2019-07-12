#Написати скрипт, який обчислить факторіал введеного числа.
num = int(input("Enter a number: "))
i = 1 
fact = 1
while i <= num :
    fact *= i
    i += 1
print("Factorial {}!".format (num),fact)
