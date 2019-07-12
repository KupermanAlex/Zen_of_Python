from tkinter import *
import random
from tkinter import messagebox as mb
# главное окно 
root = Tk()
root.title("! У ГА ГА ГА ДА Й КА !")
root.geometry("400x300+600+400")

answer = StringVar()
nummber = random.randint(1, 10)

clicks = 0
lbl_1text = StringVar()
lbl_1text.set( clicks)


def play():
    global clicks
    clicks += 1
    
    if  answer.get() == str(nummber):
        mb.showinfo("Поздравляю", "ты угадал")
    elif answer.get() > str (nummber) :
        mb.showerror("загаданое число " , "МЕНЬШЕ")
    else:
        mb.showerror("загаданое число", "БОЛЬШЕ")

    return lbl_1text.set( clicks )
    

lbl_1 = Label(root,textvariable = lbl_1text )
lbl = Label(root, text = "угадайте число от  1 до 10",font = "23")
user_input = Entry(root,textvariable=answer)
btn = Button(root,text="мне повезёт!",background="#555",foreground="#ccc",font="16",command =play) 

lbl_1.pack()                        
user_input.pack()
lbl.pack()
btn.pack() #Чтобы сделать элемент видимым, у него вызывается метод pack()
root.update()
root.mainloop()