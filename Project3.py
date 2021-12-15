from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from random import randint
import time

width = 600
height = 600


clicked_correctly = set()

def click(event):
    global size
    global clicked_correctly
    global canvas
    global weird_thing
    picture_id = canvas.find_withtag(CURRENT)[0]
    for i in range(size):
        for j in range(size):
            if picture_id == id_table[i][j]:
                if (j + 1, i + 1) not in active_images_set:
                    root.destroy()
                    print("Olete jõudnud", str(size - 2) + ". levelile")  #
                if (j + 1, i + 1) in active_images_set:
                    clicked_correctly.add((j + 1, i + 1))
                    y = j * (width / size) + weird_thing         #if some more difficulty wanted then swap x and y
                    x = i * (width / size) + weird_thing
                    canvas.create_image(x, y, image = new_active)
                    root.update()
                    if len(clicked_correctly) == len(active_images_set):
                        if clicked_correctly == active_images_set:
                            clicked_correctly = set()
                            size += 1
                            canvas.delete("all")
                            #print("Level", str(size))
                            canvas_function()
                    break
                break



def canvas_function():
    global id_table
    global active_images_set
    global new_active
    global weird_thing                        #idk why but it works
    resized_not_active = not_active.resize((int(width / size), int(height / size)), Image.ANTIALIAS)
    new_not_active = ImageTk.PhotoImage(resized_not_active)
    resized_active = active.resize((int(width / size), int(height / size)), Image.ANTIALIAS)
    new_active = ImageTk.PhotoImage(resized_active)
    weird_thing = int((width / size) / 2)
    
    for i in range(size):
        for j in range(size):
            x = int(weird_thing + (width / size) * i)
            y = int(weird_thing + (height / size) * j)
            canvas.create_image(x, y, image = new_not_active)
    
    root.update()
    time.sleep(2)
    active_images_set = set()
    
    for k in range(int(0.4 * (size ** 2))):
        while True:
            x, y = randint(1, size), randint(1, size)
            if (x, y) not in active_images_set:
                active_images_set.add((x, y))
                break
        
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if (i, j) in active_images_set:
                x = int(weird_thing + (j - 1) * (width / size))
                y = int(weird_thing + (i - 1) * (height / size))
                canvas.create_image(x, y, image = new_active)
                continue
    
    root.update()
    
    time.sleep(3)

    
    id_table = []
    for i in range(size):
        id_row = []
        for j in range(size):
            x = int(weird_thing + (width / size) * i)
            y = int(weird_thing + (height / size) * j)
            picture_id = canvas.create_image(x, y, image = new_not_active)
            canvas.tag_bind(picture_id, '<1>', click)
            id_row.append(picture_id)
        id_table.append(id_row)
    root.update()
    root.wait_variable()
    

root = Tk()
root.title("Squares")
canvas = Canvas(root, width = 600, height = 600, background = "white")
canvas.grid()

not_active = (Image.open("pic1.png"))
active = (Image.open("pic2.png"))

size = 3
canvas_function()
root.mainloop()   
