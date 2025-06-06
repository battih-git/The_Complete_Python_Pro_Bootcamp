import math
from tkinter import *

from numpy.f2py.f90mod_rules import fgetdims2

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{str(count_sec).zfill(2)}")
    if count>0:
        window.after(1000, count_down,count-1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')

timer_label = Label( text="Timer", bg=YELLOW, font=(FONT_NAME, 48, 'bold'),fg=GREEN)
timer_label.grid(row=0,column=1,padx=5)

canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130, text='00:00',fill='white', font=(FONT_NAME,35,'bold'))
canvas.grid(row=1,column=1, pady=5, padx=5)
start_button = Button(text="Start",bg=YELLOW,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text='Reset',bg=YELLOW)
reset_button.grid(row=2,column=4)

check_marks = Label(text='🗸', bg=YELLOW, fg=GREEN)
check_marks.grid(row=3,column=1)
window.mainloop()