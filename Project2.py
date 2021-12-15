from tkinter import*
from tkinter import ttk, messagebox
from random import randint
import time
from tkinter.ttk import*


j = 1
k = 0


def register_position_of_the_click(event):
    try:
        global k
        global j
        global how_many_numbers
        x, y = event.x, event.y
        if not(x in range(dict_of_coordinates[j][0] - 20, dict_of_coordinates[j][0] + 20) and y in range(dict_of_coordinates[j][1] - 20, dict_of_coordinates[j][1] + 20)):
            root.destroy()
            print("Olete jõudnud", str(j) + ". levelile")
            return False
        id = canvas.find_withtag(CURRENT)[0]
        canvas.delete(str(id))
        root.update()
        canvas.create_text(dict_of_coordinates[j][0], dict_of_coordinates[j][1], text = j, font=("Arial", 20))
        j += 1
        if j - 1 == how_many_numbers:
            how_many_numbers += 1
            root.destroy()
            create_canvas()
    except:
        pass

dict_of_coordinates = {}
how_many_numbers = 1

def create_canvas():
    global j
    global root
    global canvas
    j = 1
    root = Tk()
    root.title("Memory")
    canvas = Canvas(root, width = 500, height = 500, background = "azure", highlightthickness=5, highlightbackground="black")
    canvas.grid()
    canvas.bind('<1>', register_position_of_the_click)
    while True:
        for i in range(1, how_many_numbers + 1):
            while True:                              
                new_x = randint(30, 470)
                new_y = randint(30, 470)
                if (new_x, new_y) != (dict_of_coordinates.values()) :
                    break
            canvas.create_text(new_x, new_y, text = i, font=("Arial", 20))
            dict_of_coordinates[i] = (new_x, new_y)
        break
    root.update()
    time.sleep(5)
    canvas.delete("all")
            
    for i in range(1, how_many_numbers + 1):
        canvas.create_text(dict_of_coordinates[i][0], dict_of_coordinates[i][1], text = 'X', tags = str(i), font=("Arial", 20))
            
     

root = Tk()
root.title("Memory")
root.geometry("300x200")
    


mainframe = Frame(root)
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
    
style = ttk.Style()
style.configure('TButton', font =
            ('Arial', 20, 'bold'),
            foreground = 'black',
            background = 'black')
style.configure("TFrame", background = 'azure', borderwidth = 'black')


button_variable = IntVar()
button = ttk.Button(mainframe, text = "Start!", command = lambda: [root.destroy(), button_variable.set(1), create_canvas()]).place(relx = 0.5, rely = 0.5, anchor = CENTER)
mainframe.wait_variable()



root.mainloop()
