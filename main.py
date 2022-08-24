from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
HEADER_FONT = (FONT_NAME, 30, "normal")
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.25
LONG_BREAK_MIN = 0.40
FG = GREEN
reps = 1
symbol = ""
after_ID = 0


# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_function():
    start_button.config(state=DISABLED)
    reset_button.config(state=NORMAL)
    global reps, symbol
    if len(symbol) < 4:
        if reps % 2 == 1 and reps < 9:
            header_label.config(text="WORK", fg=GREEN)
            Count_function(floor(WORK_MIN * 60))
        elif reps % 2 == 0 and reps < 8:
            header_label.config(text="BREAK", fg=RED)
            Count_function(floor(SHORT_BREAK_MIN * 60))
        elif reps == 8:
            header_label.config(text="BREAK", fg=PINK)
            Count_function(floor(LONG_BREAK_MIN * 60))
            reps = 1

        reps += 1
    else:
        reset_function()


def reset_function():
    start_button.config(state=NORMAL)
    reset_button.config(state=DISABLED)
    global reps, symbol
    header_label.config(text="TIMER")
    canvas.itemconfig(timer_canvas, text=f"00:00")
    reps = 1
    symbol = ""
    check_marks_label.config(text=symbol)
    window.after_cancel(after_ID)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def Count_function(count):
    global reps, symbol, after_ID
    count_min = f"0{floor(count / 60)}" if floor(count / 60) < 10 else f"{floor(count / 60)}"
    count_sec = f"0{count % 60}" if count % 60 < 10 else f"{count % 60}"
    canvas.itemconfig(timer_canvas, text=f"{count_min}:{count_sec}")
    if count > 0:
        after_ID = window.after(1000, Count_function, count - 1)
    else:
        if reps % 2 == 0:
            symbol += "✔"
            check_marks_label.config(text=symbol)
        start_function()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

header_label = Label(window, text="TIMER", bg=YELLOW, font=HEADER_FONT)
header_label.config(fg=FG)
header_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo_tomato)
timer_canvas = canvas.create_text(102, 130, text=f"00:00", fill="white", font=(FONT_NAME, 24, "normal"))
canvas.grid(column=1, row=1)

start_button = Button(window, text="Start", command=start_function, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(window, text="Reset", command=reset_function, highlightthickness=0, state=DISABLED)
reset_button.grid(column=2, row=2)
check_marks_label = Label(window, text=symbol, bg=YELLOW, fg=FG)
check_marks_label.grid(column=1, row=2)
window.mainloop()
