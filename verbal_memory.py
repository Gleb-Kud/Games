from tkinter import *
from random import choice, randint


words = []
words_str = []
appeared_words = []
score = 0
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
root.resizable(width=False, height=False)

def game():
    global words_str
    global appeared_words
    global random_word
    
    if_existing = randint(1, 10)
    score_label = Label(root, text='Skoor: ' + str(score))
    score_label.grid(row=3, column=0, columnspan=3)
    if if_existing < 5 and len(appeared_words) > 1:
        random_word = choice(appeared_words)
        word_label = Label(root, text=random_word, relief='sunk', width=50, height=5, bd=5)
        word_label.grid(row=1, column=0, padx=200, pady=50, columnspan=3)
    else:
        random_word = choice(words_str)
        word_label = Label(root, text=random_word, relief='sunk', width=50, height=5, bd=5)
        word_label.grid(row=1, column=0, padx=200, pady=50, columnspan=3)

def start():
    start_button.destroy()
    button_new = Button(root, text='Uus sõna', command=lambda: button_press(1), pady=50, padx=50, bd=5)
    button_exsist = Button(root, text='Nähtud', command=lambda: button_press(2), pady=50, padx=50, bd=5)

    button_new.grid(row=2, column=0, pady=50)
    button_exsist.grid(row=2, column=2, pady=50)
    game()

def button_press(mode):
    global score
    
    if mode == 1:
        if random_word not in appeared_words:
            appeared_words.append(random_word)
            score += 1
            game()
        else:
            root.destroy()
    elif mode == 2:
        if random_word in appeared_words:
            score += 1
            game()
        else:
            root.destroy()
            


start_button = Button(root, text="Start", command=start, padx=50, pady=20)

start_button.grid(row=0, column=0, padx=100, pady=100)


root.mainloop()