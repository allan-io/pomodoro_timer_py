from tkinter import *
import math
from token import GREATER

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

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
        # if reps == 1:
        #     check_marks.config(text="✔️")
        # if reps == 3:
        #     check_marks.config(text="✔️✔️")
        # if reps == 5:
        #     check_marks.config(text="✔️✔️✔️")
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
tomato_img = PhotoImage(file="tomato.png")
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