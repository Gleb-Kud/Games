import subprocess
from tkinter import *

root = Tk()
root.resizable(width=False, height=False)

def run_game1():
    cmd = subprocess.Popen('cmd.exe',stdin=subprocess.PIPE)
    cmd.stdin.write(b"python sequence_memory.py\n")
    root.destroy()
    
def run_game2():
    cmd = subprocess.Popen('cmd.exe',stdin=subprocess.PIPE)
    cmd.stdin.write(b"python reaction_time_v2.py\n")
    root.destroy()
    
def run_game3():
    cmd = subprocess.Popen('cmd.exe',stdin=subprocess.PIPE)
    cmd.stdin.write(b"python verbal_memory.py\n")
    root.destroy()
    
def run_game4():
    cmd = subprocess.Popen('cmd.exe',stdin=subprocess.PIPE)
    cmd.stdin.write(b"python Project1.py\n")
    root.destroy()

def run_game5():
    cmd = subprocess.Popen('cmd.exe',stdin=subprocess.PIPE)
    cmd.stdin.write(b"python Project2.py\n")
    root.destroy()
    
def run_game6():
    cmd = subprocess.Popen('cmd.exe',stdin=subprocess.PIPE)
    cmd.stdin.write(b"python Project3.py\n")
    root.destroy()

button1 = Button(root, text='game1', width=10, command=run_game1)
button2 = Button(root, text='game2', width=10, command=run_game2)
button3 = Button(root, text='game3', width=10, command=run_game3)
button4 = Button(root, text='game4', width=10, command=run_game4)
button5 = Button(root, text='game5', width=10, command=run_game5)
button6 = Button(root, text='game6', width=10, command=run_game6)

button1.grid(row=0, column=0, padx=10, pady=10)
button2.grid(row=1, column=0, padx=10, pady=10)
button3.grid(row=2, column=0, padx=10, pady=10)
button4.grid(row=0, column=1, padx=10, pady=10)
button5.grid(row=1, column=1, padx=10, pady=10)
button6.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
    #subprocess.run('python C:\\Users\\Kevin\\Desktop\\Progeprojekt\\Games\\sequence_memory.py', shell=True)