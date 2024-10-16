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
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(text_timer, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    global REPS
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS+=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    # If it's the 8th rep
    if REPS%8 ==0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED)
    # If it's the 2nd/4th/6th rep
    elif REPS%2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break",fg=PINK)
    #If it's the 1st/3rd/5th/7th rep
    else:
        count_down(work_sec)
        timer_label.config(text="Work",fg=GREEN)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(text_timer,text=f"{count_min}:{count_sec}")
    if count>0:
        global TIMER
        TIMER = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text_timer = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)

timer_label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,"bold"))
timer_label.grid(row=0,column=1)

start_button = Button(text="Start",width=10,bg=GREEN,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",width=10,bg=GREEN,command=reset_timer)
reset_button.grid(row=2,column=2)

check_label =Label(fg=GREEN,bg=YELLOW)
check_label.grid(row=3,column=1)

window.mainloop()