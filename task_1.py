# Cтворіть скрипт, який би запитував у користувача:
# Його ім'я: "What is your name?"
# Вік: "How old are you?"
# Місце проживання: "Where do you live?"
# А потім виводив наступні рядки
# “Hello, ім'я!"
# “Your age is вік"
# “You live in місце проживання"
# (замість слів ім'я, вік, місце проживання повинні бути відповідні дані, що введені користувачем).
name = input("What is you name?: ")
age = input("How old old are you?: ")
city = input("where do you live?: ")

print("Hello " + name)
print("Your age is", age)
print("You live in " + city)