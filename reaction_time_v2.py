from tkinter import *
from time import time, sleep
from random import randint


root = Tk()

cond = True

def play():
    global time_1
    global background_
    global reaction_button
    
    background_.configure(bg="#fa5c5c")
    root.update()
    reaction_button = Button(root, text="", command=react, width= 10)
    reaction_button.grid(row=0, column=0, padx=200, pady=100)
    root.update()
    random_wait = randint(3, 8)
    sleep(random_wait)
    background_.configure(bg="#77ff5c")
    root.update()
    time_1 = time()
    

def start():
    start_button.destroy()
    info_label.destroy()
    play()
    
def react():
    global time_2
    global background_
    global react_time
    global time_1
    global cond
    global react_label
    
    if cond:
        time_2 = time()
        background_.configure(bg="#fa5c5c")
        root.update()
        react_time = (time_2 - time_1) * 1000
        react_label = Label(root, text=str(round(react_time))+" ms")
        react_label.grid(row=1, column=0)
        reaction_button.configure(text="Uuesti")
        cond=False
    else:
        cond=True
        react_label.destroy()
        play()
    


background_ = Canvas(root, width=500, height=500, background='white')
background_.grid(row=0, column=0, rowspan=2)

start_button = Button(root, text="Start", command=start)
info_label = Label(root, text="Kui värv muutub punaseks, vajuta nuppu", bg='white')
start_button.grid(row=0, column=0, padx=200, pady=100)
info_label.grid(row=1, column=0, pady=10)



root.mainloop()