from tkinter import *
from random import randint
import subprocess


root = Tk()
root.resizable(width=False, height=False)
sequence = []
input_sequence = []
level = 1

def exit_():
    root.destroy()

def button_press(input_button):
    global input_sequence
    global level

    input_sequence.append(input_button)
    if len(input_sequence) == len(sequence):
        if sequence == input_sequence:
            input_sequence = []
            level += 1
            game()
        else:
            button1.destroy()
            button2.destroy()
            button3.destroy()
            button4.destroy()
            button5.destroy()
            button6.destroy()
            button7.destroy()
            button8.destroy()
            button9.destroy()
            score_lable.destroy()
            root.update()
            end_label = Label(root, text="Vale järjekord", padx=100, pady=10)
            end_label.grid(row=0, column=0)
            exit_button = Button(root, text="Exit", padx=10, pady=10, command=exit_)
            exit_button.grid(row=1, column=0)
    

def start():
    button_start.destroy()
    game()

        
def game():
    global sequence
    global score_lable
    
    score_lable = Label(root, text="Level " + str(level))
    score_lable.grid(row=4, column=0, columnspan=3)

    choose_button = randint(1, 9)
    sequence.append(choose_button)
    for num in sequence:
        buttons[num - 1].configure(bg="gray")
        root.update()
        buttons[num - 1].after(500)
        buttons[num - 1].configure(bg="white")
        root.update()
        buttons[num - 1].after(100)

        

button1 = Button(root, command=lambda: button_press(1), padx=40, pady=40, bg="white", activebackground="gray")
button2 = Button(root, command=lambda: button_press(2), padx=40, pady=40, bg="white", activebackground="gray")
button3 = Button(root, command=lambda: button_press(3), padx=40, pady=40, bg="white", activebackground="gray")

button4 = Button(root, command=lambda: button_press(4), padx=40, pady=40, bg="white", activebackground="gray")
button5 = Button(root, command=lambda: button_press(5), padx=40, pady=40, bg="white", activebackground="gray")
button6 = Button(root, command=lambda: button_press(6), padx=40, pady=40, bg="white", activebackground="gray")

button7 = Button(root, command=lambda: button_press(7), padx=40, pady=40, bg="white", activebackground="gray")
button8 = Button(root, command=lambda: button_press(8), padx=40, pady=40, bg="white", activebackground="gray")
button9 = Button(root, command=lambda: button_press(9), padx=40, pady=40, bg="white", activebackground="gray")

button_start = Button(root, text="Start", command=start)

buttons = [button1, button2, button3, button4, button5,
           button6, button7, button8, button9]


button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

button_start.grid(row=4, column=0, columnspan=3)






root.mainloop()