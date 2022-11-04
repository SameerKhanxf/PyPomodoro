from tkinter import *
import math

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
checkmark_text = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def timer_reset():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    global checkmark_text
    reps = 0
    checkmark_text = ""
    checkmark.config(text=checkmark_text)



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 != 0:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    else:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minute = math.floor(count / 60)
    second = count % 60
    if minute < 10:
        minute = f"0{minute}"
    if second < 10:
        second = f"0{second}"

    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global reps
        global checkmark_text
        if reps % 2 == 0:
            checkmark_text += "✔"
            checkmark.config(text=checkmark_text)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)


title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)
checkmark = Label(font=(FONT_NAME, 15, "normal"), fg=GREEN, bg=YELLOW)
checkmark.grid(row=2, column=1)


start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", command=timer_reset)
reset_button.grid(row=2, column=2)


window.mainloop()