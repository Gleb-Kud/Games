from tkinter import *
from tkinter import ttk, messagebox
from random import randint, choice
from random import *
from time import time, sleep
import time
from PIL import Image, ImageTk
from threading import Thread



mainframe = Tk()
mainframe.resizable(width=False, height=False)
#=======Reaction variables===============================================================================
sequence = []
input_sequence = []
level = 1
#=======Verbal variables===============================================================================
words = []
words_str = []
appeared_words = []
score = 0
#=======Reaction variables===============================================================================
cond = True
#=====================================MÄNGUD=================================================

def run_sequence():
    mainframe.withdraw()
    root = Tk()
    root.resizable(width=False, height=False)

    def exit_():
        mainframe.deiconify()
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
                end_label = Label(root, text="Vale järjekord", padx=100, pady=10, font = ('Arial', 9, 'bold'))
                end_label.grid(row=0, column=0)
                print("Olete jõudnud", str(level) + ". levelile")
                exit_button = Button(root, text="Menu", padx=10, pady=10, command=exit_, font = ('Arial', 9, 'bold'))
                exit_button.grid(row=1, column=0)
                level = 1
        

    def start():
        button_start.destroy()
        game()

            
    def game():
        global sequence
        global score_lable
        
        score_lable = Label(root, text="Level " + str(level), font = ('Arial', 9, 'bold'))
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

    button_start = Button(root, text="Start!", command=start, font = ('Arial', 9, 'bold'))

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
    
#=======================================================================================    
    
def run_reaction():
    
    root = Tk()
    root.resizable(width=False, height=False)

    

    def play():
        global time_1
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
        time_1 = time.time()
        

    def start():
        start_button.destroy()
        info_label.destroy()
        play()
        
    def react():
        global time_2
        global react_time
        global time_1
        global cond
        global react_label
        
        if cond:
            time_2 = time.time()
            background_.configure(bg="#fa5c5c")
            root.update()
            react_time = (time_2 - time_1) * 1000
            react_label = Label(root, text=str(round(react_time))+" ms", font = ('Arial', 9, 'bold')) #
            print(round(react_time, 4))  #
            react_label.grid(row=1, column=0)
            reaction_button.configure(text="Uuesti!", font = ('Arial', 9, 'bold'))   #
            cond=False
        else:
            cond=True
            react_label.destroy()
            play()
        


    background_ = Canvas(root, width=500, height=500, background='azure')
    background_.grid(row=0, column=0, rowspan=2)
    
    style = ttk.Style()   #
    style.configure('TButton', font =
                ('Arial', 20, 'bold'),
                foreground = 'black',
                background = 'black')

    start_button = Button(root, text="Start!", command=start, font =
            ('Arial', 20, 'bold'),
            foreground = 'black')#
    info_label = Label(root, text="Kui värv muutub punaseks, vajuta nuppu", bg='azure', font = ('Arial', 13, 'bold'))
    start_button.grid(row=0, column=0, padx=200, pady=100)
    info_label.grid(row=1, column=0, pady=10)



    root.mainloop()
    
#=======================================================================================

def run_verbal():


    f = open("lemmad.txt", mode='rb')

    # Siin tekkis mingi jama, et ei saanud encoding='utf-8'-ga lugeda failist, niiet tegin nii
    # loeb bytes objektidena wordsi ja siis sõelub sealt ebasobilikud sõnad välja
    for word in f:
         words.append(word.strip())

    for word in words:
        try:
            words_str.append(word.decode('utf-8'))
        except:
            pass
        
    f.close()
        
    root = Tk()
    root.configure(bg = 'azure')
    root.resizable(width=False, height=False)

    def game():
        global words_str
        global appeared_words
        global random_word
        
        if_existing = randint(1, 10)
        score_label = Label(root, text='Skoor: ' + str(score), font = ('Arial', 9, 'bold'), bg = 'azure')
        score_label.grid(row=3, column=0, columnspan=3)
        if if_existing < 5 and len(appeared_words) > 1:
            random_word = choice(appeared_words)
            word_label = Label(root, text=random_word, relief='sunk', width=50, height=5, bd=5, font = ('Arial', 15, 'bold'))
            word_label.grid(row=1, column=0, padx=200, pady=50, columnspan=3)
        else:
            random_word = choice(words_str)
            word_label = Label(root, text=random_word, relief='sunk', width=50, height=5, bd=5)
            word_label.grid(row=1, column=0, padx=200, pady=50, columnspan=3)

    def start():
        start_button.destroy()
        button_new = Button(root, text='Uus sõna', command=lambda: button_press(1), pady=50, padx=50, bd=5, font = ('Arial', 9, 'bold'))
        button_exsist = Button(root, text='Nähtud', command=lambda: button_press(2), pady=50, padx=50, bd=5, font = ('Arial', 9, 'bold'))

        button_new.grid(row=2, column=0, pady=50)
        button_exsist.grid(row=2, column=2, pady=50)
        game()

    def button_press(mode):
        global score
        global appeared_words

        
        if mode == 1:
            if random_word not in appeared_words:
                appeared_words.append(random_word)
                score += 1
                game()
            else:
                root.destroy()
                root.destroy()
                print("Teie skoor oli:", str(score))
                words = []
                words_str = []
                appeared_words = []
                score = 0
        elif mode == 2:
            if random_word in appeared_words:
                score += 1
                game()
            else:
                root.destroy()
                print("Teie skoor oli:", str(score))
                words = []
                words_str = []
                appeared_words = []
                score = 0
                


    start_button = Button(root, text="Start!", command=start, padx=50, pady=20, font = ('Arial', 20, 'bold'))

    start_button.grid(row=0, column=0, padx=100, pady=100)


    root.mainloop()
    
#=======================================================================================
def run_game4():
    def start(root, difficulty):
        s = ttk.Style()
        s.configure('TButton', font =
                ('Arial', 10, 'bold'),
                foreground = 'black',
                background = 'black')
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
                    print("Olete jõudnud", str(how_many_numbers) + ". levelile")
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
        label = ttk.Label(mainframe, text = "Choose your speed", font = ('Arial', 10, 'bold')).grid(column = 0, row = 0, padx=10, pady=10)
        
        s_2 = ttk.Radiobutton(mainframe, text='Easy', variable = speed, value = 3).grid(column = 0, row = 1, padx=30, pady=10)
        s_1 = ttk.Radiobutton(mainframe, text='Medium', variable = speed, value = 2).grid(column = 0, row = 3, padx=30, pady=10)
        s_half = ttk.Radiobutton(mainframe, text='Hard', variable = speed, value = 1).grid(column = 0, row = 5, padx=30, pady=10)
        go = ttk.Button(mainframe, text = "Let's go!", command = lambda: [mainframe.destroy(), start(root, speed.get())]).grid(column = 1, row = 1, rowspan = 4, padx=20, pady=10, sticky = 'sn')
        s = ttk.Style()
        s.configure('TButton', font =
                ('Arial', 8, 'bold'),
                foreground = 'black',
                background = 'black')
       

    frame = Tk()
    frame.title("Welcome!")
    frame.geometry("300x200")
    frame.eval('tk::PlaceWindow . center')
    frame.configure(background = 'azure')
    
    style = ttk.Style()
    style.configure('TButton', font =
                ('Arial', 20, 'bold'),
                foreground = 'black',
                background = 'black')

    button = ttk.Button(frame, text = "Play!", command = play)
    button.place(x = 50, y = 100, width = 200, height = 80)
    frame.mainloop()  

#=======================================================================================

def run_game5():
    j = 1
    k = 0

    def register_position_of_the_click(event):
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
    
#=======================================================================================

def run_game6():
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
                        print("Olete jõudnud", str(size - 2) + ". levelile")
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

#=======================================================================================

def exit_():
    mainframe.destroy()

#=======================================================================================    

button1 = Button(mainframe, text='Jada mälu', width=15, command=run_sequence)
button2 = Button(mainframe, text='Reaktsioonid', width=15, command=run_reaction)
button3 = Button(mainframe, text='Sõnaline mälu', width=15, command=run_verbal)
button4 = Button(mainframe, text='game4', width=15, command=run_game4)
button5 = Button(mainframe, text='game5', width=15, command=run_game5)
button6 = Button(mainframe, text='game6', width=15, command=run_game6)
button_exit = Button(mainframe, text='Exit', width=15, command=exit_)


button1.grid(row=0, column=0, padx=10, pady=10)
button2.grid(row=1, column=0, padx=10, pady=10)
button3.grid(row=2, column=0, padx=10, pady=10)
button4.grid(row=0, column=2, padx=10, pady=10)
button5.grid(row=1, column=2, padx=10, pady=10)
button6.grid(row=2, column=2, padx=10, pady=10)
button_exit.grid(row=2, column=1, padx=10, pady=10)

mainframe.mainloop()
    #subprocess.run('python C:\\Users\\Kevin\\Desktop\\Progeprojekt\\Games\\sequence_memory.py', shell=True)
