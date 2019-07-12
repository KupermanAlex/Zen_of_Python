# number = int(input("Please enter a number: "))
# if number == 0 :
#     print ("0 is ZERO")
# elif number % 2 == 0 :
#     print("{} is even number".format(number))
# else :
#     print("{} is odd number".format(number))
##############################################
# class Number :
#     def __init__(self,some_number):
#         self.some_number = some_number
#         # int(input("Please enter a number: "))

#     def check(self):
#         if self.some_number == 0 :
#             print ("0 is ZERO")
#         elif self.some_number % 2 == 0 :
#             print("{} is even number".format(self.some_number))
#         else :
#             print("{} is odd number".format(self.some_number))   
################################################

# try:
#     number = int(input("Please enter a number: "))
#     if number == 0 :
#         print ("0 is ZERO")
#     elif number % 2 == 0 :
#         print("{} is even number".format(number))
#     else :
#         print("{} is odd number".format(number))
# except TypeError:
#     print("Caught TypeError Exception")
# except ValueError:
#     print ("Invalid Literal for int ")
# else :
#     print("no exception")    
######################################################

try:
    number = int(input("Please enter a number: "))
except TypeError:
    print("Caught TypeError Exception")
except ValueError:
    print ("Invalid Literal for int ")
else :
    print("no exception")
if number == 0 :
    print ("0 is ZERO")
elif number % 2 == 0 :
    print("{} is even number".format(number))
else :
    print("{} is odd number".format(number))
