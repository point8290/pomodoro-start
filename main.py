from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT = (FONT_NAME, 16, "bold")
FONT_T = (FONT_NAME, 30, "normal")
FONT_B = ("Arial", 9, "bold")
CHECKMARK = "✔"
CHECKMARK_STRING = ""
time = "00:00"
reps = 0
STOP = True


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(total_second, check):
    global STOP, CHECKMARK_STRING, CHECKMARK

    if not STOP:
        second = total_second % 60
        minutes = total_second // 60

        if second <= 9:
            second = f"0{second}"
        if minutes <= 9:
            minutes = f"0{minutes}"

        if total_second >= 0:
            canvas.itemconfig(timer, text=f"{minutes}:{second}")
            total_second -= 1
            window.after(1000, countdown, total_second, check)
        else:
            STOP = True
            if check:
                CHECKMARK_STRING += CHECKMARK
                check_mark.config(text=CHECKMARK_STRING)
            start_clock()


def start_clock():
    global reps, STOP, CHECKMARK_STRING
    check = True
    reps = (reps + 1) % 8
    if STOP:
        STOP = False
        if reps == 0:
            CHECKMARK_STRING = ""
            check_mark.config(text=CHECKMARK_STRING)
            check = False
            label.config(text="BREAK", bg=YELLOW, font=FONT_T, fg=PINK)
            total_second = LONG_BREAK_MIN * 60
        elif reps % 2 != 0:
            label.config(text="WORK", bg=YELLOW, font=FONT_T, fg=GREEN)
            total_second = WORK_MIN * 60
            check = True
        else:
            label.config(text="BREAK", bg=YELLOW, font=FONT_T, fg=RED)
            total_second = SHORT_BREAK_MIN * 60
            check = False

        countdown(total_second, check)


def reset():
    global reps, STOP, CHECKMARK_STRING
    CHECKMARK_STRING = ""
    reps = 0
    STOP = True
    canvas.itemconfig(timer, text=f"00:00")
    label.config(text="TIMER", bg=YELLOW, font=FONT_T, fg="#FF0000")
    check_mark.config(text=CHECKMARK_STRING)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("TIME WATCH")
window.config(bg=YELLOW, padx=40, pady=20)
label = Label(text="TIMER", bg=YELLOW, font=FONT_T, fg="#FF0000")
label.grid(row=0, column=1)
canvas = Canvas(width=205, height=225, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=image)
timer = canvas.create_text(100, 130, text=time, font=FONT)
canvas.grid(row=1, column=1)
start_button = Button(text="START", padx=2, bg="#FFE5B4", font=FONT_B, width=5, highlightthickness=0,
                      command=start_clock)
start_button.grid(row=2, column=0)
reset_button = Button(text="RESET", padx=2, bg="#FFE5B4", font=FONT_B, width=5, highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)
check_mark = Label(text=CHECKMARK_STRING, font=FONT, fg=GREEN)
check_mark.grid(row=2, column=1)
window.mainloop()
