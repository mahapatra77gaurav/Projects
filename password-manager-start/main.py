from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = ([choice(letters) for _ in range(randint(8, 10))] +
                     [choice(symbols) for _ in range(randint(2, 4))] +
                     [choice(numbers) for _ in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join(password_list)

    pwd_entry.delete(0, END)
    pwd_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = pwd_entry.get()

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any spaces empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Details Entered:\nEmail:{email_username}\n"
                                                              f"Password:{password}\nDo you want to save")
        if is_ok:
            with open("data.txt","a") as data:
                data.write(f"{website} | {email_username} | {password}\n")
            website_entry.delete(0,END)
            pwd_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo_img =PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1,columnspan=2,sticky='W')



website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

email_username_label = Label(text="Email/Username:   ")
email_username_label.grid(row=2,column=0)

pwd_label = Label(text="Password:")
pwd_label.grid(row=3,column=0)



website_entry = Entry(width=52)
website_entry.grid(row=1,column=1,columnspan=2,sticky='W')
website_entry.focus()

email_username_entry = Entry(width=52)
email_username_entry.grid(row=2,column=1,columnspan=2,sticky='W')
email_username_entry.insert(0,"mahapatragaurav77@gmail.com")

pwd_entry = Entry(width=33)
pwd_entry.grid(row=3,column=1,sticky='W')



generate_pwd_button = Button(text="Generate Password",command=generate_password)
generate_pwd_button.grid(row=3,column=2,sticky='E')

add_button = Button(text="Add",width=44,command=save)
add_button.grid(row=4,column=1,columnspan=2,sticky='W')

window.mainloop()