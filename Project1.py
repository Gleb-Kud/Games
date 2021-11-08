from tkinter import*
from tkinter import ttk, messagebox
import time
from random import*

    
    
def start(root, difficulty):
    mainframe = ttk.Frame(root)
    mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight = 1)
    
    time_left = 3
    while time_left > 0:
        ttk.Label(root, text = time_left).place(relx = 0.5, rely = 0.5, anchor = CENTER)
        time_left -= 1
        root.update()
        time.sleep(1)
    ttk.Label(root, text = "Go!").place(relx = 0.5, rely = 0.5, anchor = CENTER)
    for child in root.winfo_children(): 
        child.destroy()
    root.update()
    how_many_numbers = 1
    
    while True:
        time.sleep(1)
        string_of_numbers = ''
        for i in range(how_many_numbers):
            string_of_numbers += str(randint(0, 9))   
        ttk.Label(root, text = string_of_numbers).place(relx = 0.5, rely = 0.5, anchor = CENTER)
        root.update()
        time.sleep(difficulty / 5)
        
        for child in root.winfo_children(): 
            child.destroy()
        root.update()
        
        entered_numbers = StringVar()
        button_pressed = StringVar()
        ttk.Entry(root, width = 7, textvariable = entered_numbers).grid(column = 0, row = 0, padx = 30, pady = 30)
        button = ttk.Button(root, text = "Check!", command = lambda: button_pressed.set("button pressed")).grid(column = 0, row = 1, padx = 30, pady = 30)
        root.wait_variable(button_pressed)
        root.update()
        if button_pressed.get() == "button pressed":
            if entered_numbers.get() != string_of_numbers:
                for child in root.winfo_children(): 
                    child.destroy()
                print('Incorrect!')
                print("The correct was: " + string_of_numbers)
                break
            else:
                print("Correct!")
                how_many_numbers += 1
                for child in root.winfo_children(): 
                    child.destroy()
                root.update()
        
def play():
    frame.destroy()
    
    root = Tk()
    root.title("Speed")
    root.geometry("300x200")
    root.eval('tk::PlaceWindow . center')
    
    mainframe = ttk.Frame(root)
    mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight = 1)
    
    speed = IntVar()
    label = ttk.Label(mainframe, text = "Choose your speed").grid(column = 0, row = 0, padx=10, pady=10)
    
    s_2 = ttk.Radiobutton(mainframe, text='Easy', variable = speed, value = 3).grid(column = 0, row = 1, padx=30, pady=10)
    s_1 = ttk.Radiobutton(mainframe, text='Medium', variable = speed, value = 2).grid(column = 0, row = 3, padx=30, pady=10)
    s_half = ttk.Radiobutton(mainframe, text='Hard', variable = speed, value = 1).grid(column = 0, row = 5, padx=30, pady=10)
    go = ttk.Button(mainframe, text = "Let's go!", command = lambda: [mainframe.destroy(), start(root, speed.get())]).grid(column = 1, row = 1, rowspan = 4, padx=20, pady=10, sticky = 'sn')
    
   

frame = Tk()
frame.title("Welcome!")
frame.geometry("300x200")
frame.eval('tk::PlaceWindow . center')


button = ttk.Button(frame, text = "Play!", command = play)
button.place(x = 50, y = 100, width = 200, height = 80)
frame.mainloop()

