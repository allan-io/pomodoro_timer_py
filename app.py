from tkinter import *
import math
from playsound import playsound
import threading
import sys
import os

# Determine the path to the file
if getattr(sys, 'frozen', False):  # Running in a bundle
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

# Use the base path to reference the image file
image_path = os.path.join(base_path, "tomato.png")


from token import GREATER

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- PLAY SOUND ------------------------------- #

def play_sound():
    # This will run in a separate thread
    playsound('./alarm.mp3')  # Custom alarm sound

def start_playing_sound():
    # Start a new thread to play the sound
    sound_thread = threading.Thread(target=play_sound)
    sound_thread.start()

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps == 8:
        count_down(LONG_BREAK_MIN)
        check_marks.config(text="✔️✔️✔️✔️️")
        reps = 0
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 1:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time_left):

    min_count = math.floor(time_left / 60)
    sec_count = time_left % 60
    time_display = f"{min_count:02}:{sec_count:02}"
    canvas.itemconfig(timer_text, text=time_display)

    if time_left > 0:
        global timer

        timer = window.after(1000, count_down, time_left -1)
    else:
        window.attributes("-topmost", True)
        window.lift()
        window.focus_force()
        start_playing_sound()
        start_timer()
        marks = ""
        work_session = math.floor((reps / 2))
        for _ in range(work_session):
            marks += "✔️"
        check_marks.config(text=marks)
    #   reset_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=image_pathgit )
canvas.create_image(100, 112, image= tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)




window.mainloop()