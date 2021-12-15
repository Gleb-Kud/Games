import subprocess
from tkinter import *
from tkinter import ttk, messagebox
from random import randint, choice
from random import *
from time import time, sleep
import time
from PIL import Image, ImageTk
from threading import Thread



mainframe = Tk()
mainframe.title('Menu')
mainframe.configure(bg = "azure")
mainframe.configure(borderwidth = 20)
mainframe.resizable(width=False, height=False)
#=======Sequence variables===============================================================================
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
cycles = 1
#=======Chimp variable=====================================================================
j = 1
k = 0
how_many_numbers = 1
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
        global sequence

        input_sequence.append(input_button)
        if len(input_sequence) == len(sequence):
            if sequence == input_sequence:
                input_sequence = []
                level += 1
                game()
            else:
                score_lable = Label(root, text="Level " + str(level), font = ('Arial', 9, 'bold'))
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
                sequence = []
                input_sequence = []
        

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
    
    mainframe.withdraw()
    root = Tk()
    root.resizable(width=False, height=False)

    

    def play():
        global time_1
        global reaction_button
        
        background_.configure(bg="#fa5c5c")
        root.update()
        reaction_button = Button(root, text="", command=react, width= 10)
        reaction_button.grid(row=0, column=0, padx=100, pady=100)
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
            foreground = 'black')
    info_label = Label(root, text="Kui värv muutub roheliseks, vajuta nuppu", bg='azure', font = ('Arial', 13, 'bold'))
    start_button.grid(row=0, column=0, padx=200, pady=100)
    info_label.grid(row=1, column=0, pady=10)



    root.mainloop()
    
#=======================================================================================

def run_verbal():

    mainframe.withdraw()
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
            word_label = Label(root, text=random_word, relief='sunk', width=50, height=5, bd=5, font = ('Arial', 15, 'bold'))
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
                print("Teie skoor oli:", str(score))
                score = 0
                words = []
                words_str = []
                appeared_words = []
                root.destroy()
                mainframe.deiconify()

                
        elif mode == 2:
            if random_word in appeared_words:
                score += 1
                game()
            else:
                print("Teie skoor oli:", str(score))
                score = 0
                words = []
                words_str = []
                appeared_words = []
                root.destroy()
                mainframe.deiconify()
               

    start_button = Button(root, text="Start!", command=start, padx=50, pady=20, font = ('Arial', 20, 'bold'))

    start_button.grid(row=0, column=0, padx=100, pady=100)


    root.mainloop()
    
#=======================================================================================
def run_number():
    
    cmd = subprocess.Popen('cmd.exe',stdin=subprocess.PIPE)
    cmd.stdin.write(b"python Project1.py\n")  

#=======================================================================================

def run_chimp():
    
    cmd = subprocess.Popen('cmd.exe',stdin=subprocess.PIPE)
    cmd.stdin.write(b"python Project2.py\n")   
    
#=======================================================================================

def run_visual():
    
    cmd = subprocess.Popen('cmd.exe',stdin=subprocess.PIPE)
    cmd.stdin.write(b"python Project3.py\n")   

#=======================================================================================

def exit_():
    mainframe.destroy()

#=======================================================================================    

button1 = Button(mainframe, text='Jada mälu', width=15, command=run_sequence)
button2 = Button(mainframe, text='Reaktsioonid', width=15, command=run_reaction)
button3 = Button(mainframe, text='Sõnaline mälu', width=15, command=run_verbal)
button4 = Button(mainframe, text='Numbriline mälu', width=15, command=run_number)
button5 = Button(mainframe, text='Ahvi test', width=15, command=run_chimp)
button6 = Button(mainframe, text='Visuaalne mälu', width=15, command=run_visual)
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