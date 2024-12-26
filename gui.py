# Python program demonstrating
# ScrolledText widget in tkinter
import os
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext

win = tk.Tk()
win.title("ScrolledText Widget")
win.geometry('1250x700')
win.configure(background='#2e2e2e')
PATH = 'C:\\Users\\User\\vscode_project\\labs\\labs'


def run():
    code.config(state=NORMAL)
    code.delete("1.0", END)

    result = os.popen(f'python {PATH}\\lab{i.get()}\\lab.py').read()
    code.insert(END, result)


def display():

    code.config(state=NORMAL)
    code.delete("1.0", END)
    readme.delete("1.0", END)
    with open(f'{PATH}\\lab{i.get()}\\lab.py') as code_file:
        code_txt = code_file.read()

    code.insert(END, code_txt)

    with open(f'{PATH}\\lab{i.get()}\\README.md') as readme_file:
        readme_txt = readme_file.read()

    readme.insert(END, readme_txt)


display_frame = Frame(win, bg = '#2e2e2e')
radio_frame = Frame(win, height=700, bg = '#2e2e2e')

run_btn = Button(radio_frame, command=run, bg="red", text='RUN', width=10)
run_btn.grid(row=8, column=1)

i = IntVar()
r1 = Radiobutton(radio_frame, text="Lab1", value=1, variable=i, width=55, command=display, bg="#4d4d4d", fg="white")
r2 = Radiobutton(radio_frame, text="Lab2", value=2, variable=i, width=55, command=display, bg="#4d4d4d", fg="white")
r3 = Radiobutton(radio_frame, text="Lab3", value=3, variable=i, width=55, command=display, bg="#4d4d4d", fg="white")
r4 = Radiobutton(radio_frame, text="Lab4", value=4, variable=i, width=55, command=display, bg="#4d4d4d", fg="white")
r5 = Radiobutton(radio_frame, text="Lab5", value=5, variable=i, width=55, command=display, bg="#4d4d4d", fg="white")
r6 = Radiobutton(radio_frame, text="Lab6", value=6, variable=i, width=55, command=display, bg="#4d4d4d", fg="white")
r7 = Radiobutton(radio_frame, text="Lab7", value=7, variable=i, width=55, command=display, bg="#4d4d4d", fg="white")
r8 = Radiobutton(radio_frame, text="Lab8", value=8, variable=i, width=55, command=display, bg="#4d4d4d", fg="white")

r1.grid(column=1, pady=20, padx=20, row=0)
r2.grid(column=1, pady=20, padx=20, row=1)
r3.grid(column=1, pady=20, padx=20, row=2)
r4.grid(column=1, pady=20, padx=20, row=3)
r5.grid(column=1, pady=20, padx=20, row=4)
r6.grid(column=1, pady=20, padx=20, row=5)
r7.grid(column=1, pady=20, padx=20, row=6)
r8.grid(column=1, pady=20, padx=20, row=7)

code = scrolledtext.ScrolledText(display_frame,
                                      wrap=tk.WORD,
                                      width=95,
                                      height=15,
                                      font=("JetBrains Mono",
                                            11),
                                      fg='green',
                                      bg='black'
                                      )
code.grid(column=0, row=0, pady=10, padx=10)


readme = scrolledtext.ScrolledText(display_frame,
                                      wrap=tk.WORD,
                                      width=70,
                                      height=13,
                                      font=("JetBrains Mono",
                                            15),
                                      fg = 'black',
                                      bg="#9c9c9c"
                                        )
readme.grid(column=0, row=1, pady=10, padx=10)

radio_frame.grid(column=1, row=0)
display_frame.grid(column=0, row=0)


win.mainloop()

