koloda = [6,7,8,9,10,2,3,4,11] * 4
import random
random.shuffle(koloda)
print("Let's play '21' ?")
count = 0
current = koloda.pop()
while True:
    choice = input("Do you want to play ? y/n\n")
    if choice == "y":
        print("You have point %d" %current)
        count += current
        if count > 21:
            print("Sorry, you are fail :(")
            break
        elif count == 21:
            print("You are winner :)")
            break
        elif count < 21:
            continue
        else:
            print("You have %d points" %current)
    elif choice == "n":
        print("You have %d points and you stopped the game" %current)
        break
    print("See you later. Good bye!")